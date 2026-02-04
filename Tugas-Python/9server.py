import socket
import select

HOST = '0.0.0.0'
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

sockets = [server_socket]
clients = {}  # socket : (ip, port)

print(f"=== Select Server berjalan di port {PORT} ===")

while True:
    read_sockets, _, _ = select.select(sockets, [], [])

    for sock in read_sockets:

        # Client baru masuk
        if sock == server_socket:
            client_socket, addr = server_socket.accept()
            sockets.append(client_socket)
            clients[client_socket] = addr
            print(f"[JOIN] Client {addr} masuk")

        # Pesan dari client
        else:
            data = sock.recv(1024)

            # Client keluar
            if not data:
                print(f"[LEAVE] Client {clients[sock]} keluar")
                sockets.remove(sock)
                del clients[sock]
                sock.close()
                continue

            message = data.decode().strip()
            sender_ip = clients[sock][0]

            # PRIVATE MESSAGE
            if message.startswith("@"):
                try:
                    target_ip, msg = message[1:].split(" ", 1)
                    for c in clients:
                        if clients[c][0] == target_ip:
                            c.send(f"[PM dari {sender_ip}] {msg}\n".encode())
                            break
                except:
                    sock.send(b"[SERVER] Format PM salah. Gunakan @ip pesan\n")

            # BROADCAST
            else:
                for c in clients:
                    if c != sock:
                        c.send(f"[{sender_ip}] {message}\n".encode())
