import asyncio
import sys

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"\nServer > Koneksi dari {addr}")

    try:
        while True:
            data = await reader.read(100)
            if not data:
                print(f"\nServer > {addr} disconnect")
                break

            message = data.decode().strip()

            # Cetak TANPA pindah baris aneh
            print(f"\rServer > [{addr}] {message}")
            sys.stdout.flush()

            response = f"Echo: {message}\n"
            writer.write(response.encode())
            await writer.drain()

    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"=== Sedang berada di Async Server yang Berjalan di {addrs} ===")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer Dimatikan.")
