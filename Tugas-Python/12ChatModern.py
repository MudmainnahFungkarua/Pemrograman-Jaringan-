import asyncio
import websockets
import json
import random
from datetime import datetime

CONNECTED_CLIENTS = set()
USERNAMES = dict()

# -----------------------
# Handler tiap client
# -----------------------
async def handler(websocket):
    # Minta username
    await websocket.send(json.dumps({"msg": "Masukkan username Anda dulu."}))
    try:
        username = await websocket.recv()
        USERNAMES[websocket] = username
        CONNECTED_CLIENTS.add(websocket)
        print(f"[NEW] {username} connected.")

        join_msg = f"[Server] {username} has joined the chat."
        websockets.broadcast(CONNECTED_CLIENTS, join_msg)

        async for message in websocket:
            timestamp = datetime.now().strftime("%H:%M:%S")
            formatted_msg = f"[{timestamp}] {username}: {message}"
            websockets.broadcast(CONNECTED_CLIENTS, formatted_msg)
            print(f"[CHAT] {formatted_msg}")

    except websockets.exceptions.ConnectionClosed:
        print(f"[CLOSED] {username} disconnected.")
        if websocket in CONNECTED_CLIENTS:
            CONNECTED_CLIENTS.remove(websocket)
            leave_msg = f"[Server] {username} has left the chat."
            websockets.broadcast(CONNECTED_CLIENTS, leave_msg)
        if websocket in USERNAMES:
            del USERNAMES[websocket]

# -----------------------
# Broadcast harga saham BBCA
# -----------------------
async def broadcast_stock():
    while True:
        price_data = {
            "symbol": "BBCA",
            "price": random.randint(8000, 8500),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        message = json.dumps(price_data)
        if CONNECTED_CLIENTS:
            websockets.broadcast(CONNECTED_CLIENTS, message)
        await asyncio.sleep(1)  # update tiap detik

# -----------------------
# Main server
# -----------------------
async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("=== WebSocket Dashboard Server running on ws://localhost:6789 ===")
        await broadcast_stock()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server Stopped.")