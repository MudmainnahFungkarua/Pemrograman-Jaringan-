import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(('localhost', 5555))
    server.listen(5)
    print("=== Server Framing Siap (Port 5555) ===")

    while True:
        try:
            conn, addr = server.accept()
            print(f"[!] Koneksi dari {addr}")

            with conn:
                stream = conn.makefile('r', encoding='utf-8')

                for line in stream:
                    line = line.strip()
                    if not line:
                        break

                    print(f"Terima Pesan Utuh: {line}")
                    conn.send(f"ACK: {line}\n".encode('utf-8'))

            print(f"[!] {addr} terputus.")

        except Exception as e:
            print(f"Error Server: {e}")

if __name__ == "__main__":
    run_server()