import tornado.web

class Index(tornado.web.RequestHandler):
    def get(self):
        
        css = """<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
        <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">"""
        
        html = "Hello world"
        
        self.write(html + css)