import tornado.ioloop
import tornado.web
import json
import logging
from collections import defaultdict

from games.tictactoe.tictactoe import TicTacToe

from lib.user import (
    create_user,
    get_user,
    InvalidUserNameException,
    UserAlreadyExistsException,
)

from lib.message_utils import generate_messages_html

logging.basicConfig(format='%(asctime)-15s %(message)s', level='INFO')
games = {}
user_messages = defaultdict(list)


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
        error = games[game_id].update_state(player_id, update_json)
        if error:
            user = self.get_cookie('user_name')
            user_messages[user] = str(error)


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


class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        user = get_user(name)
        if not user:
            try:
                create_user(name)
            except UserAlreadyExistsException:
                self.set_status(403)
            except InvalidUserNameException:
                self.set_status(400)
            else:
                self.set_cookie('user_name', name)


class MessageHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_cookie('user_name')
        messages = user_messages[user]
        # TODO: check if user is there?
        messages_html = generate_messages_html(messages)
        self.write(messages_html)  # TODO: check that this works


application = tornado.web.Application([
    (r"/api/login", LoginHandler),
    (r"/api/create", CreateHandler),
    (r"/api/update", UpdateHandler),
    (r"/api/state", StateHandler),
    (r"/api/join", JoinHandler),
    (r"/api/messages", MessageHandler),
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
