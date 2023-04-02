import logging
import random
import aiohttp
import aiohttp_jinja2
from aiohttp import web
from uuid import uuid4

log = logging.getLogger(__name__)

def get_random_name():
    return str(uuid4())

# Generate a random number when the application starts
random_number = random.randint(1,100)

async def index(request):
    ws_current = web.WebSocketResponse()
    ws_ready = ws_current.can_prepare(request)
    global random_number
    if not ws_ready.ok:
        return aiohttp_jinja2.render_template('index.html', request, {})
    await ws_current.prepare(request)
    name = get_random_name()
    log.info('%s joined.', name)
    await ws_current.send_json({'action': 'connect', 'name': name})
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'join', 'name': name})
    request.app['websockets'][name] = ws_current
    while True:
        msg = await ws_current.receive()
        
        if msg.type == aiohttp.WSMsgType.text:
            print (random_number, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            if int(msg.data) == random_number:
                answer = 'win, restart game'
                random_number = random.randint(1,100)  # generate a new random number
            elif int(msg.data) < random_number:
                answer = 'загаданное число больше '
            else: 
                answer = 'загаданное число меньше'
            for ws in request.app['websockets'].values():
                if ws is ws_current:
                    await ws_current.send_json(
                        {'action': 'sent', 'name': 'You', 'text': msg.data, 'answer' : answer})
                else:
                    await ws.send_json(
                        {'action': 'sent', 'name': name, 'text': msg.data, 'answer' : answer})
        else:
            break
    del request.app['websockets'][name]
    log.info('%s disconnected.', name)
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'disconnect', 'name': name})
    return ws_current