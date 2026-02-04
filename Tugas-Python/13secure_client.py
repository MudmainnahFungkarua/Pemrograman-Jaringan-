import socket
import ssl

def run_secure_client():
    # 1. Konteks SSL (Client)
    # Gunakan create_default_context tapi matikan verifikasi karena sertifikat kita self-signed
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # 2. Socket Biasa
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 3. WRAP Socket SEBELUM connect
    # Client membungkus socket dulu, baru connect
    secure_sock = context.wrap_socket(sock, server_hostname='localhost')

    try:
        print("Menghubungkan ke Secure Server...")
        secure_sock.connect(('localhost', 10023))
        print(f"Terhubung dengan Cipher: {secure_sock.cipher()}")

        secure_sock.send(b"Halo, ini pesan rahasia CIA.")
        response = secure_sock.recv(1024)
        print(f"Balasan Server: {response.decode()}")

    finally:
        secure_sock.close()

if __name__ == "__main__":
    run_secure_client()