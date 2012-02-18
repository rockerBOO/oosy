import tornado.web

class Index(tornado.web.RequestHandler):
    def get(self):
        template_file = 'templates/home.html'
        html          = ''
        
        infile        = open(template_file, "r")
        
        for line in infile.readlines():
            html += line
        
        infile.close()
        
        css = """<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
        <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">"""
        
        self.write(css + html)