from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the index!'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 6543, app)
    server.serve_forever()