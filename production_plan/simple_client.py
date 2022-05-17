import asyncio
import socketio

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connected to server')


@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def production_plan(production_plan):
    print(production_plan)


async def start_server():
    await sio.connect('http://localhost:8888')
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(start_server())

