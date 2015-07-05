import tornado.ioloop
import tornado.web

from games.tictactoe.tictactoe import TicTacToe

my_game = None


class TicTacToeHandler(tornado.web.RequestHandler):
    def get(self):
        # takes you to tictactoe landing page? how
        pass


class CreateHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        global my_game
        my_game = TicTacToe()
        my_game.start()


class UpdateHandler(tornado.web.RequestHandler):
    def post(self):
        update_json = self.get_argument('update_json')
        my_game.update_state(update_json)


class StateHandler(tornado.web.RequestHandler):
    def get(self):
        global my_game
        info = my_game.get_state()
        self.write(info)

application = tornado.web.Application([
    (r"/tictactoe", TicTacToeHandler),
    (r"/api/create", CreateHandler),
    (r"/api/update", UpdateHandler),
    (r"/api/state", StateHandler),
    (r"/static/(.*)",
     tornado.web.StaticFileHandler,
     {'path': 'web/static'}),
    (r"/(.*)",
     tornado.web.StaticFileHandler,
     {'path': 'web',
      'default_filename': 'index.html'}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
