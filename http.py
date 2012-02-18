from tornado import httpserver
from tornado import ioloop

from pymongo import Connection
import datetime

def handle_request(request):
    # connection = Connection('localhost', 27017)
    # 
    # db = connection.oosy
    # collection = db.test
    # 
    # post = {"author": "Mike",
    #          "text": "My first blog post!",
    #          "tags": ["mongodb", "python", "pymongo"],
    #          "date": datetime.datetime.utcnow()}
    # 
    # posts = db.posts
    # print posts.insert(post)
    
    from Index from modules.web
    
    Index.Index.get()
    
    message = "You requested %s\n" % request.uri
    request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (len(message), message))
    request.finish()

http_server = httpserver.HTTPServer(handle_request)
http_server.listen(8889)
ioloop.IOLoop.instance().start()