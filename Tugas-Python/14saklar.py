# latihan_14_mqtt_pub.py
import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_BASE = "kampus/iot"

client = mqtt.Client()
print(f"Publisher terhubung ke {BROKER}...")
client.connect(BROKER, PORT, 60)

client.loop_start() # Jalankan background thread untuk networking

try:
    while True:
        # Simulasi 2 sensor berbeda
        suhu_lab = random.uniform(20.0, 25.0)
        suhu_kantin = random.uniform(28.0, 32.0)

        # Publish ke topik spesifik
        # QoS=1 berarti "Pastikan sampai"
        client.publish(f"{TOPIC_BASE}/lab_komputer", f"{suhu_lab:.2f}", qos=1)
        print(f"Mengirim {suhu_lab:.2f} ke Lab Komputer")

        client.publish(f"{TOPIC_BASE}/kantin", f"{suhu_kantin:.2f}", qos=1)
        print(f"Mengirim {suhu_kantin:.2f} ke Kantin")

        time.sleep(2)

except KeyboardInterrupt:
    print("Stop Publisher")
    client.loop_stop()
    client.disconnect()