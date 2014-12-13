##Coroutine

Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes.

##Eventlet

Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

* It uses epoll or kqueue or libevent for highly scalable non-blocking I/O.
* Coroutines ensure that the developer uses a blocking style of programming that is similar to threading, but provide the benefits of non-blocking I/O.
* The event dispatch is implicit, which means you can easily use Eventlet from the Python interpreter, or as a small part of a larger application.

It's easy to get started using Eventlet, and easy to convert existing applications to use it. Start off by looking at examples, common design patterns, and the list of the basic API primitives.

##Example

They are some easy example of eventlet for learning. You can also find it at:http://eventlet.net/doc/examples.html


