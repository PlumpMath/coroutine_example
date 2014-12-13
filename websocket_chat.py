import os

import eventlet
from eventlet import wsgi
from eventlet import websocket

PORT = 7777

participants = set()


@websocket.WebSocketWSGI
def handle(ws):
    participants.add(ws)
    try:
        while True:
            msg = ws.wait()
            if msg in None:
                break
            for p in participants:
                p.send(msg)
    finally:
        participants.remove(ws)


def dispatch(environ, start_response):
    '''Resloves to the web page or the websocket depending on the path.'''
    if environ['PATH_INFO'] == '/chat':
        return handle(environ, start_response)
    else:
        start_response('200 OK!', [('content-type', 'type/html')])
        html_path = os.path.join(
            os.path.dirname(__file__), 'websocket_chat.html')
        return [open(html_path).read() % {'port': PORT}]


if __name__ == '__main__':
    #run an example app from the commond line.
    listener = eventlet.listen(('127.0.0.1', PORT))
    print "\nVisit http://localhost:7777/ in your websocket-capable browser.\n"
    wsgi.server(listener, dispatch)
