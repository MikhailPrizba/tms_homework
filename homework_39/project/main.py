import aiohttp_jinja2
import jinja2
from aiohttp import web
from hw39.db import db_init
from hw39.views import routes

app = web.Application(debug=True)
app.router.add_routes(routes)
app.cleanup_ctx.append(db_init)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=9999)