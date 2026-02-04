# core_server.py
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import paho.mqtt.client as mqtt
import asyncio
import websockets
import json
import threading

app = Flask(__name__)
CORS(app)  # biar HTML bisa fetch login
USERS = {"admin":"1234"}
DATA_STORE = {}

# --- MQTT Subscriber ---
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "distributed_smart_system/#"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[Server] Terhubung ke Broker MQTT")
        client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    sensor = msg.topic.split("/")[-1]
    value = msg.payload.decode()
    DATA_STORE[sensor] = value
    print(f"[MQTT] {sensor}: {value}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(BROKER, PORT, 60)
mqtt_client.loop_start()

# --- REST API Login ---
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if USERS.get(username) == password:
        return jsonify({"status":"success"})
    return jsonify({"status":"failed"}), 401

# --- Serve HTML ---
@app.route("/")
def index():
    return send_from_directory(".", "monitor.html")  # simpan monitor.html di folder sama

# --- WebSocket ---
CONNECTED_CLIENTS = set()
async def ws_handler(websocket):
    CONNECTED_CLIENTS.add(websocket)
    try:
        while True:
            await asyncio.sleep(1)
            if DATA_STORE:
                await websocket.send(json.dumps(DATA_STORE))
    except:
        pass
    finally:
        CONNECTED_CLIENTS.remove(websocket)

async def ws_server():
    async with websockets.serve(ws_handler, "localhost", 6789):
        await asyncio.Future()  # loop selamanya

if __name__ == "__main__":
    # Jalankan Flask
    threading.Thread(target=lambda: app.run(port=5000)).start()
    # Jalankan WebSocket
    asyncio.run(ws_server())
