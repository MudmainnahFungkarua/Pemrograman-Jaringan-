import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

print("Terhubung ke server. Ketik pesan, ketik 'bye' untuk keluar.")

while True:
    pesan = input(">> ")
    if pesan.lower() == 'bye':
        break

    client.send(pesan.encode('utf-8'))
    balasan = client.recv(1024).decode('utf-8')
    print("Server:", balasan)

client.close()
print("Koneksi ditutup")