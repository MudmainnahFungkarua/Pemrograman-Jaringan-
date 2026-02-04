import socket
import threading

# Shared Resource: daftar client aktif
clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_conn):
    """Mengirim pesan ke semua client kecuali pengirim"""
    with clients_lock:
        for client in clients:
            if client != sender_conn:
                try:
                    client.send(message)
                except:
                    client.close()

def handle_client(conn, addr):
    """Fungsi yang dijalankan oleh setiap thread"""
    print(f"[NEW CONNECTION] {addr} connected.")

    with clients_lock:
        clients.append(conn)

    try:
        conn.send("Selamat datang di Chat Room!\n".encode('utf-8'))

        while True:
            message = conn.recv(1024)
            if not message:
                break

            msg = message.decode('utf-8')
            output = f"[Client {addr[1]}]: {msg}"
            print(output.strip())

            broadcast(output.encode('utf-8'), conn)

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")

    finally:
        print(f"[DISCONNECT] {addr} keluar.")
        with clients_lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen()

    print("[SERVER STARTED] Menunggu koneksi di port 5555...")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        )
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()