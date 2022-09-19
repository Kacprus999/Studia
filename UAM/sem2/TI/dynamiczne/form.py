from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from pyramid.view import view_config
import re
from marshmallow import Schema, fields, validates, validates_schema, ValidationError
import os

uppercaseAndDigits = re.compile(r'^[A-Z0-9]*$')

class KeySchema(Schema):
    key = fields.String(required=True)
    payload = fields.String(required=True)

    @validates('key')
    def valid_key(self, value):
        if not value or len(value) > 10:
            raise ValidationError('Key must be nonempty an at most 10 characters long.')
        if not uppercaseAndDigits.match(value):
            raise ValidationError('Key must contain only uppercase letters and digits.')

    @validates('payload')
    def valid_dat(self, value):
        if not value or len(value) > 30:
            raise ValidationError('Payload must be nonempty and at most 30 characters long.')

    @validates_schema
    def valid_schema(self, data, **kwargs):
        if not data['key'][0] == data['payload'][0]:
            raise ValidationError('First letters of key and payload must be the same.')

@view_config(route_name='form', renderer='form.jinja2', request_method='GET')
def form(request):
    return {}

@view_config(route_name='form', renderer='form.jinja2', request_method='POST')
def handle(request):
    # Data that comes from the client must always be thoroughly checked
    # as they can be easily spoofed
    try:
        schema = KeySchema()
        pair = schema.load(request.POST)
        request.session[pair['key']] = pair['payload']
        return {}
    except ValidationError as err:
        return { 'error': err.messages,
                 'values': request.POST }

@view_config(route_name='delete', renderer='form.jinja2')
def delete(request):
    key = request.matchdict['key']
    if key in request.session:
        del request.session[key]
    return {}

config = Configurator()
config.add_route('form', '/')
config.add_route('delete', '/delete/{key}')
config.include('pyramid_jinja2')
thisDirectory = os.path.dirname(os.path.realpath(__file__))
config.add_jinja2_search_path(thisDirectory)
config.include('pyramid_debugtoolbar')
session_factory = SignedCookieSessionFactory('tajneHaslo')
config.set_session_factory(session_factory)
config.scan()

app = config.make_wsgi_app()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 6543, app)
    server.serve_forever()