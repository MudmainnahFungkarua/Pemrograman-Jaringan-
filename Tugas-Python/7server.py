import socket
import json

# Database Mahasiswa (Dummy)
DATABASE = {
    "2314010200": {"nama": "Mutma", "prodi": "Teknik Informatika", "ipk": 3.85},
    "1302020238": {"nama": "Azizah", "prodi": "Sistem Informasi", "ipk": 3.90},
    "1302020242": {"nama": "Dwingka", "prodi": "Teknik Komputer", "ipk": 3.90}
}

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 6000))
    server.listen(5)

    print("=== Database Server (JSON) Berjalan di Port 6000 ===")

    while True:
        client, addr = server.accept()
        print(f"[KONEKSI] Dari {addr}")

        try:
            request_bytes = client.recv(4096)
            if not request_bytes:
                break

            request_str = request_bytes.decode('utf-8')
            request_data = json.loads(request_str)

            command = request_data.get("command")
            nim = request_data.get("nim")

            response = {}

            if command == "GET_MHS":
                if nim in DATABASE:
                    response = {
                        "status": "SUKSES",
                        "data": DATABASE[nim]
                    }
                else:
                    response = {
                        "status": "GAGAL",
                        "pesan": "NIM tidak ditemukan"
                    }
            else:
                response = {
                    "status": "ERROR",
                    "pesan": "Perintah tidak dikenali"
                }

            client.send(json.dumps(response).encode('utf-8'))

        except json.JSONDecodeError:
            error = {
                "status": "ERROR",
                "pesan": "Format JSON tidak valid"
            }
            client.send(json.dumps(error).encode('utf-8'))

        finally:
            client.close()

if __name__ == "__main__":
    run_server()