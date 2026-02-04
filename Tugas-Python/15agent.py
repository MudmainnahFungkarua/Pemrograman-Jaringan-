# agent.py
import paho.mqtt.client as mqtt
import psutil
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_BASE = "distributed_smart_system"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        cpu_usage = psutil.cpu_percent()
        suhu = random.uniform(25.0, 35.0)

        client.publish(f"{TOPIC_BASE}/cpu", f"{cpu_usage:.2f}")
        print(f"[Agent] CPU Usage: {cpu_usage:.2f}% terkirim")

        client.publish(f"{TOPIC_BASE}/suhu", f"{suhu:.2f}")
        print(f"[Agent] Suhu: {suhu:.2f}°C terkirim")

        time.sleep(2)

except KeyboardInterrupt:
    print("Agent berhenti.")
    client.loop_stop()
    client.disconnect()
