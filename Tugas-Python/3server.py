import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("Server berjalan... menunggu client...")

conn, addr = server.accept()
print("Client terhubung:", addr)

# Kirim permintaan password
conn.send("Masukkan password: ".encode('utf-8'))

password = conn.recv(1024).decode('utf-8')
print("Password diterima:", password)

# Validasi password
if password != "12345":
    conn.send("Password salah!".encode('utf-8'))
    conn.close()
    print("Client ditolak")
else:
    conn.send("Login sukses! Selamat datang.".encode('utf-8'))
    print("Client login berhasil")

# INTI CHAT
while True:
    msg = conn.recv(1024).decode('utf-8')
    print(f"Client > {msg}")

    if msg.lower() == 'bye':
        conn.send("bye".encode('utf-8'))
        break

    balasan = input("Server > ")
    conn.send(balasan.encode('utf-8'))

    if balasan.lower() == 'bye':
        break

conn.close()
server.close()
print("=== Server Ditutup ===")