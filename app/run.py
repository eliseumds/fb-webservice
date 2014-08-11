from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application
from fb_webservice.routes import routes

application = Application(routes,debug=options.debug)

if __name__ == "__main__":
    application.listen(options.rest_port)
    print 'Server running at http://localhost:%s' % options.rest_port

    try:
        IOLoop.instance().start()
    except KeyboardInterrupt:
        IOLoop.instance().stop()
    except:
        pass
