import socket

# 1. Membuat socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect ke server
print("Menghubungi server...")
client.connect(('localhost', 5000))

# 3. Kirim pesan ke server
client.send("Halo Server\n".encode('utf-8'))
client.send("Ini pesan kedua\n".encode('utf-8'))

# 4. Terima balasan dari server
balasan = client.recv(1024).decode('utf-8')
print("Balasan dari server:", balasan)

# 5. Tutup koneksi
client.close() 