# latihan_14_mqtt_sub.py
import paho.mqtt.client as mqtt

# 1. Konfigurasi
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "kampus/iot/+" # + adalah Wildcard satu level

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[SUKSES] Terhubung ke Broker!")
        # Langsung subscribe setelah connect
        client.subscribe(TOPIC)
    else:
        print(f"[GAGAL] Error Code: {rc}")

def on_message(client, userdata, msg):
    # msg.topic = "kampus/iot/lab_komputer"
    # msg.payload = b"25.5"
    lokasi = msg.topic.split("/")[-1]
    nilai = msg.payload.decode()

    print(f"📡 Data Masuk dari [{lokasi}]: {nilai}°C")

# 2. Setup Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print(f"Menghubungkan ke {BROKER}...")
client.connect(BROKER, PORT, 60)

# 3. Blocking Loop (Standby selamanya)
client.loop_forever()