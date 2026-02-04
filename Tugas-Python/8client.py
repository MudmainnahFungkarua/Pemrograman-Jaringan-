import asyncio
import sys

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)


    while True:
        pesan = input("Client > ")
        if pesan.lower() == "exit":
            break

        writer.write((pesan + "\n").encode())
        await writer.drain()

        data = await reader.read(100)

        # Cetak server reply rapi
        print(f"\rServer > {data.decode().strip()}")
        sys.stdout.flush()

    writer.close()
    await writer.wait_closed()

asyncio.run(main())
