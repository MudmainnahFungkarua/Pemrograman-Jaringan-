import socket
import ssl

def run_secure_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")

    bindsocket = socket.socket()
    bindsocket.bind(('localhost', 10023))
    bindsocket.listen(5)
    print("Secure Server listening on port 10023...")

    while True:
        try:
            newsocket, fromaddr = bindsocket.accept()
            print(f"[NEW] Koneksi TCP dari {fromaddr}")

            # Bungkus socket dengan SSL (Handshake otomatis)
            conn = context.wrap_socket(newsocket, server_side=True)
            print(f"[SECURE] SSL Handshake sukses dengan {fromaddr}")

            # Komunikasi terenkripsi
            data = conn.recv(1024)
            print(f"Pesan (Decrypted): {data.decode()}")

            conn.send(b"Pesan Anda aman bersama kami.")

        except ssl.SSLError as e:
            print(f"[ERROR] Masalah SSL: {e}")
        except Exception as e:
            print(f"Error lain: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

if __name__ == "__main__":
    run_secure_server()
