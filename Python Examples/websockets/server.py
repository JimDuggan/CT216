# http://developer.mbed.org/cookbook/Websockets-Server#1-hello-world

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("Hello World")
        self.write_message("Another message...")

    def on_message(self, message):
        print 'message received %s' % message

    def on_close(self):
      print 'connection closed'


application = tornado.web.Application([
    (r'/ws', WSHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
