import tornado.ioloop
import tornado.web
import json
import logging

from games.tictactoe.tictactoe import TicTacToe

logging.basicConfig(format='%(asctime)-15s %(message)s', level='INFO')
games = {}


class CreateHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        new_game = TicTacToe()
        game_id = new_game.uuid.hex
        games[game_id] = new_game
        new_game.start()
        self.write(json.dumps({'game_id': game_id}))


class UpdateHandler(tornado.web.RequestHandler):
    def post(self):
        game_id = self.get_argument('game_id')
        player_id = self.get_argument('player_id')
        update_json = self.get_argument('update_json')
        games[game_id].update_state(player_id, update_json)


class StateHandler(tornado.web.RequestHandler):
    def get(self):
        game_id = self.get_argument('game_id')
        player_id = self.get_argument('player_id')
        info = games[game_id].get_state(player_id)
        self.write(info)


class JoinHandler(tornado.web.RequestHandler):
    def post(self):
        game_id = self.get_argument('game_id')
        player_id = games[game_id].add_player()
        self.write(json.dumps({'player_id': player_id}))

application = tornado.web.Application([
    (r"/api/create", CreateHandler),
    (r"/api/update", UpdateHandler),
    (r"/api/state", StateHandler),
    (r"/api/join", JoinHandler),
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
    logging.info("Server started at port 8888.")
    tornado.ioloop.IOLoop.current().start()
