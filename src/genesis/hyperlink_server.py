import asyncio
import websockets
import json

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"🌐 Received: {message}")
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("🔗 Hyperlink server running at ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())