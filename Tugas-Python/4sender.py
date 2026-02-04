import socket
import time
import random

# 1. Membuat socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Alamat server
TARGET_IP = 'localhost'  # ganti jika beda komputer
TARGET_PORT = 9999
TARGET_ADDR = (TARGET_IP, TARGET_PORT)

print(f"=== Sensor Aktif. Mengirim data ke {TARGET_ADDR} ===")

try:
    while True:
        suhu = random.randint(20, 35)
        kelembaban = random.randint(40, 90)

        payload = f"TEMP:{suhu}C|HUM:{kelembaban}%"

        sock.sendto(payload.encode('utf-8'), TARGET_ADDR)
        print(f"Mengirim -> {payload}")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nSensor dimatikan.")
    sock.close()