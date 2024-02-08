import tornado.web            
import tornado.ioloop        # thread waiting for result
import json

class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('bonus.html')


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        file = open('list.txt', 'r')
        numbers = file.read().splitlines()
        file.close()
        self.write(json.dumps(numbers)) 
    
    def post(self):
        number = self.get_argument('number')
        numbers = open('list.txt', 'a')
        numbers.write(f'{number}\n')
        numbers.close()
        self.write(json.dumps({'message':'added successfully'}))



if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/',mainRequestHandler),
        (r'/list',listRequestHandler),
    ])

    port = 8882
    app.listen(port)
    print(f'Application is listening on port: {port}')
    tornado.ioloop.IOLoop.current().start()