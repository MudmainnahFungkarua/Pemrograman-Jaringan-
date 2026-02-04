import socket
import json

def cek_mahasiswa(nim):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 6000))

    request = {
        "command": "GET_MHS",
        "nim": nim
    }

    print(f"Mengirim request NIM: {nim}")
    client.send(json.dumps(request).encode('utf-8'))

    response_bytes = client.recv(4096)
    response = json.loads(response_bytes.decode('utf-8'))

    print("Respon Server:")
    print(json.dumps(response, indent=2))
    print("-" * 40)

    client.close()

if __name__ == "__main__":
    cek_mahasiswa("2314010200")
    cek_mahasiswa("1302020238")
    cek_mahasiswa("1302020242")