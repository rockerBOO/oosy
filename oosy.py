import tornado.ioloop
import tornado.web

import modules.Index

application = tornado.web.Application([
    (r"/", modules.Index.Index),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()