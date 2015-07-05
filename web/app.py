import tornado.ioloop
import tornado.web
import json

from games.tictactoe.tictactoe import TicTacToe

games = {}


class TicTacToeHandler(tornado.web.RequestHandler):
    def get(self):
        # takes you to tictactoe landing page? how
        pass


class CreateHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        new_game = TicTacToe()
        game_id = new_game.uuid().hex
        games[game_id] = new_game
        new_game.start()
        self.write(json.loads({'game_id': game_id}))
        # need to pass uuid of game somehow?


class UpdateHandler(tornado.web.RequestHandler):
    def post(self):
        game_id = self.get_argument('game_id')
        update_json = self.get_argument('update_json')
        games[game_id].update_state(update_json)


class StateHandler(tornado.web.RequestHandler):
    def get(self):
        game_id = self.get_argument('game_id')
        info = games[game_id].get_state()
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
     {'path': 'web/static',
      'default_filename': 'index.html'}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
