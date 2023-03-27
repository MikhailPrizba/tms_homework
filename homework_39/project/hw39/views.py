from aiohttp import web
from hw39 import service
import aiohttp_jinja2

routes = web.RouteTableDef()

@routes.get('/v1')
@aiohttp_jinja2.template("index.html")
async def index(request):
    print(request.app)
    data = await service.get_comment(app =request.app)
    print(data)
    test1 = data.fetchall()
    texts = [row[0].text for row in test1]
    print(texts)
    if not data:
        return web.Response(text='Hi')
    return {'title': 'hi', 'data': texts}

@routes.post('/v1')
@aiohttp_jinja2.template("index.html")
async def create_comment(request):
    data = await request.post()
    coment_text = data['comment']
    print(coment_text)
    await service.create_comment(app = request.app, text= coment_text)
    return web.Response(text='Done')

