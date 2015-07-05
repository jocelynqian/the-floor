import json

from games.commons.game import Game
from games.tictactoe.player import TicTacToePlayer


class TicTacToe(Game):

    def __init__(self):
        self._board = self.create_board()
        self._turn = None
        self._finished = 'e'
        self._players = {}
        self._seats = 2
        # add an error?

    def get_state(self, player_id):
        return json.dumps({'board': self._board,
                           'turn': self._turn,
                           'state': self._finished})

    def update_state(self, player_id, update_json):
        # update contains move location
        update = json.loads(update_json)
        # checks validity of move
        assert self.is_valid(player_id, update['square']), "Invalid move"
        # makes move, finishes turn, checks if the game is over
        self.mark_square(self._turn, update['square'])
        self.finish_turn()
        self._finished = self.done()

    def start(self):
        self._turn = 'x'

    def done(self):
        e = 'e'
        # returns x, o for victory, e for unfinished, and t? for tie
        has_empty = False
        line_1 = set()
        line_2 = set()
        # check horizontals and verticals
        for i in range(3):
            for j in range(3):
                # check to see if board is filled
                if self._board[i][j] == e:
                    has_empty = True
                # horizontals
                line_1.add(self._board[i][j])
                # verticals
                line_2.add(self._board[j][i])
            # check lines for victory
            if self.check_line(line_1):
                return self.check_line(line_1)
            if self.check_line(line_2):
                return self.check_line(line_2)
            # clear and check next set
            line_1.clear()
            line_2.clear()
        # check diagonals
        for i in range(3):
            line_1.add(self._board[i][i])
            line_2.add(self._board[i][2 - i])
        if self.check_line(line_1):
            return self.check_line(line_1)
        if self.check_line(line_2):
            return self.check_line(line_2)
        # indicate whether or not the game is finished
        if has_empty:
            return 'e'
        else:
            return 't'

    def create_board(self):
        e = 'e'
        return [[e, e, e], [e, e, e], [e, e, e]]

    # TODO: modify to output specific errors
    def is_valid(self, player_id, square):
        if self._finished != 'e':
            assert False, "The game is already finished"
        if self._players[player_id].get_piece() != self._turn:
            assert False, "Not your turn"
        if self._board[square[0]][square[1]] != 'e':
            assert False, "Not an empty square"
        return True

    def mark_square(self, symbol, square):
        self._board[square[0]][square[1]] = symbol

    def finish_turn(self):
        if self._turn == 'x':
            self._turn = 'o'
        else:
            self._turn = 'x'

    def check_line(self, line):
        if 'e' not in line and 'o' not in line:
            return 'x'
        elif 'e' not in line and 'x' not in line:
            return 'o'
        else:
            return None

    def add_player(self):
        assert self._seats > 0, "This game is full."
        if self._seats == 1:
            new_player = TicTacToePlayer('o')
        else:
            new_player = TicTacToePlayer('x')
        player_id = new_player.uuid.hex
        self._players[player_id] = new_player
        return player_id
