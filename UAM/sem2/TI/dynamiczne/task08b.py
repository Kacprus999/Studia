def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [b'REQUEST_METHOD: %s\nSCRIPT_NAME: %s\nPATH_INFO: %s' %
            (environ.get('REQUEST_METHOD', '').encode('utf-8'),
             environ.get('SCRIPT_NAME', '').encode('utf-8'),
             environ.get('PATH_INFO', '').encode('utf-8'))]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 6543, app)
    server.serve_forever()