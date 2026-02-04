import socket
import select
import sys

SERVER_IP = "127.0.0.1"
PORT = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
client_socket.setblocking(False)

print("===Terhubung ke server===")
print("Ketik pesan lalu ENTER")
print("ctrl + enter untuk keluar \n")

while True:
    sockets = [sys.stdin, client_socket]
    read_sockets, _, _ = select.select(sockets, [], [])

    for sock in read_sockets:

        # Pesan dari server
        if sock == client_socket:
            data = sock.recv(1024)
            if not data:
                print("\nServer terputus")
                sys.exit()
            print("\n" + data.decode(), end="")
            print("> ", end="", flush=True)

        # Input user
        else:
            msg = sys.stdin.readline().strip()
            if msg.lower() == "bye":
                client_socket.close()
                sys.exit()

            client_socket.send(msg.encode())
            print("> ", end="", flush=True)