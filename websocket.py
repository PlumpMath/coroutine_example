import eventlet
from eventlet import wsgi
from eventlet import websocket
from eventlet.support import six

# Demo app
import os
import random


@websocket.WebSocketWSGI
def handle(ws):
    '''This is the web socket handler function. Note that we can
    dispatch based on path in here,too.Why?
    '''
    print 'ws.path', ws.path
    if ws.path == '/echo':
        while True:
            m = ws.wait()
            print m
            if m is None:
                break
            ws.send(m)

    elif ws.path == '/data':
        for i in six.moves.range(10000):
            ws.send("0 %s %s \n" % (i, random.random()))
            eventlet.sleep(0.1)


def dispacth(environ, start_response):
    """This resolves to the web page or the websocket depending on this path.
    """
    if environ['PATH_INFO'] == '/data':
        return handle(environ, start_response)
    else:
        start_response('200 OK', [('content-type', 'text/html')])
        return [open(os.path.join(
            os.path.dirname(__file__), 'websocket.html')).read()]


def main():
    listener = eventlet.listene(('127.0.0.1', 7000))
    print "\nVisit http://localhost:7000/ in your websocket-capable browser."
    wsgi.server(listener, dispacth)


if __name__ == '__main__':
    main()
