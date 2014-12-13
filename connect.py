"""Spawn multiple workers and collect their results.

Demonstrates how to use the eventlet.green.socket module.
"""
#from __future__ import print_function
import eventlet
from eventlet.green import socket


def geturl(url):
    con = socket.socket()
    ip = socket.gethostbyname(url)
    con.connect((ip, 80))
    print('%s connected' % url)
    con.sendall('GET /\r\n\r\n')
    return con.recv(1024)


urls = ['www.souhu.com', 'www.baidu.com', 'www.muzixing.com']
pile = eventlet.GreenPile()
for x in urls:
    pile.spawn(geturl, x)

for url, result in zip(urls, pile):
    print('%s: %s' % (url, repr(result)[:100]))
