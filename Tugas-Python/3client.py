import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

# Terima permintaan password
msg = client.recv(1024).decode('utf-8')
print(msg) 

password = input("Password > ")
client.send(password.encode('utf-8'))

# Respon autentikasi
response = client.recv(1024).decode('utf-8')
print(response)

if "salah" in response.lower():
    client.close()
    exit()

# INTI CHAT
while True:
    try:
        message = input("Client > ")
        client.send(message.encode('utf-8'))

        if message.lower() == 'bye':
            break

        reply = client.recv(1024).decode('utf-8')
        print(f"Server > {reply}")

        if reply.lower() == 'bye':
            break

    except Exception as e:
        print("Error:", e)
        break

client.close()
print("=== Client Ditutup ===")