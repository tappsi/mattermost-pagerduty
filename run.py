from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.options import options

from handlers.PagerDutyHandler import PagerDutyHandler
import opt

application = Application(
    [
        (r'/PagerDutyNotification', PagerDutyHandler),
    ]
)

if __name__ == '__main__':
    http_server = HTTPServer(application)
    http_server.listen(options.port)
    IOLoop.instance().start()
