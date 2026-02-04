import socket
import datetime

HOST = '0.0.0.0'
PORT = 8080

def log_request(ip, file, status):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("server.log", "a") as log:
        log.write(f"[{waktu}] {ip} {file} {status}\n")

def content_type(file):
    if file.endswith(".html"):
        return "text/html"
    elif file.endswith(".jpg"):
        return "image/jpeg"
    else:
        return "text/plain"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Server jalan di http://localhost:8080")

while True:
    client, addr = server.accept()
    request = client.recv(1024).decode()

    if not request:
        client.close()
        continue

    filename = request.split()[1]
    if filename == "/":
        filename = "/index.html"

    try:
        with open(filename.lstrip("/"), "rb") as f:
            data = f.read()

        header = "HTTP/1.1 200 OK\r\n"
        header += f"Content-Type: {content_type(filename)}\r\n"
        header += f"Content-Length: {len(data)}\r\n\r\n"

        client.send(header.encode() + data)
        log_request(addr[0], filename, 200)

    except FileNotFoundError:
        body = "<h1>404 Not Found</h1>".encode()
        header = "HTTP/1.1 404 Not Found\r\n"
        header += f"Content-Length: {len(body)}\r\n\r\n"

        client.send(header.encode() + body)
        log_request(addr[0], filename, 404)

    client.close()
