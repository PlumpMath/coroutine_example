import eventlet
from eventlet.green import urllib2

urls = [
    "http://www.muzixing.com",
    "http://www.baidu.com", ]


def fetch(url):
    return urllib2.urlopen(url).read()

pool = eventlet.GreenPool(200)


def task():
    print "run task"


for body in pool.imap(fetch, urls):
    print "got body", len(body)
    print pool.free()
    print pool.running()

print pool.spawn(task)

for body in pool.imap(task,):
    print body
