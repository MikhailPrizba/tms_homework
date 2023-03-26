from views import handler

def setup_routes(app):
    app.router.add_post('/', handler),
    