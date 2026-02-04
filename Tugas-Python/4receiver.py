import socket

# 1. Membuat socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind ke semua IP dan port 9999
sock.bind(('0.0.0.0', 9999))

print("=== UDP Monitoring Server Berjalan ===")
print("Menunggu data sensor...")

while True:
    # 3. Menerima data dari sensor
    data, addr = sock.recvfrom(1024)

    pesan = data.decode('utf-8')
    print(f"[Sensor {addr}] Melaporkan: {pesan}")