import eventlet
from eventlet import wsgi


def hello_world(env, start_response):
    if env['PATH_INFO'] != '/':
        start_response('404 Not Found', [('Content-type', 'text/plain')])
        return ['Not Found\r\n']
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hello world!\r\n']


wsgi.server(eventlet.listen(('127.0.0.1', 8090)), hello_world)
