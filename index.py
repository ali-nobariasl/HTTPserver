import tornado.web            
import tornado.ioloop        # thread waiting for result


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("this if from backend :D ")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
         self.render('index.html')

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animal", listRequestHandler),

    ])
    
    port = 8882
    app.listen(port)
    print(f'Application is listening on port: {port}')
    tornado.ioloop.IOLoop.current().start()