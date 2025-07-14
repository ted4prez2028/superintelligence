import asyncio
import websockets

async def send_message(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"✅ Sent: {message}")
        try:
            response = await websocket.recv()
            print(f"📥 Response: {response}")
        except:
            pass

def hyperlink_send(text: str) -> str:
    uri = "ws://localhost:8765"
    asyncio.get_event_loop().run_until_complete(send_message(uri, text))
    return "📡 Message dispatched to Hyperlink network."