from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='index')
def index(request):
    return Response('Welcome to the index!')

@view_config(route_name='hello', renderer='string')
def hello(request):
    return 'Hello World!'

@view_config(route_name='hello_name', renderer='string')
def hello_name(request):
    return 'Hello ' + request.matchdict['name'] + '!'

config = Configurator()
config.add_route('index', '/')
config.add_route('hello', '/hello')
config.add_route('hello_name', '/hello/{name}')
config.scan()
app = config.make_wsgi_app()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 6543, app)
    server.serve_forever()