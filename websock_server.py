#!/usr/bin/env python

# from http://autobahn.ws/python/tutorials/echo/

from twisted.internet import reactor
from autobahn.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

class EchoServerProtocol(WebSocketServerProtocol):
    def onMessage(self, msg, binary):
        self.sendMessage(msg, binary)

if __name__ == '__main__':
    import os
    factory = WebSocketServerFactory("ws://{}:8123".format(os.uname()[1]), debug=False)
    factory.protocol = EchoServerProtocol
    listenWS(factory)
    reactor.run()
