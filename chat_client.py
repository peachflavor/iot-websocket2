
import asyncio
import websockets

async def send_message(websocket):
        while True:
                message = input("Enter Message : ")
                await websocket.send(message)

async def recieve_message(websocket):
        async for message in websocket:
                print(f"Recieve : {message}")

async def main():
        uri = "ws://192.168.188.143:8765"
        async with websockets.connect(uri) as websocket:
                await asyncio.gather(
                        send_message(websocket),
                        recieve_message(websocket)
                )

if __name__== "__main__":
        asyncio.run(main())
