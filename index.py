import tornado.web            
import tornado.ioloop        # thread waiting for result


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("this if from backend :D ")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if(num.isdigit()):
            result = 'even' if int(num) %2 else 'odd'
            self.write(f'{num} integer is : {result}')
        else:
            self.write(f'{num} is not a number')

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self,studentname, corseid):
        self.write(f'welcome {studentname}, the course is {corseid}')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animal", listRequestHandler),
        (r"/iseven", queryParamRequestHandler),
        (r'/student/([a-z]+)/([0-9]+)', resourceParamRequestHandler), 
    ])
    
    port = 8882
    app.listen(port)
    print(f'Application is listening on port: {port}')
    tornado.ioloop.IOLoop.current().start()