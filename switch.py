from greenlet import greenlet

def test1():
    print "first test1 printing "
    gr2.switch()
    print "second test1 printing "


def test2():
    print "first test2 printing "
    gr1.switch()
    print "second test2 printing "

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
gr2.switch()
