'''
telnet localhost:6000
'''
from __future__ import print_function
import eventlet


def handle(fd):
    print("Client connected")
    while True:
        msg = fd.readline()
        if not msg:
            break
        fd.write(msg)
        fd.flush()
        print("echoed", msg, end=' ')
    print('client disconnected')


print("server socket listening on port 6000")
server = eventlet.listen(('127.0.0.1', 6000))
pool = eventlet.GreenPool()
while True:
    try:
        new_sock, address = server.accept()
        print('accepted', address)
        pool.spawn_n(handle, new_sock.makefile('rw'))
    except (SystemExit, KeyboardInterrupt):
        break
