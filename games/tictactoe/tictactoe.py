import json

from games.commons.game import Game


class TicTacToe(Game):

    e = 'e'
    x = 'x'
    o = 'o'
    t = 't'

    def __init__(self):
        self._board = self.create_board()
        # self._player_x = TicTacToePlayer(x)
        # self._player_y = TicTacToePlayer(y)
        self._turn = None
        self._finished = 'e'
        # add an error?

    def get_state(self):
        return json.dumps({'board': self._board,
                           'turn': self._turn,
                           'state': self._finished})

    def update_state(self, update_json):
        # update should be json construct containing move location
        update = json.loads(update_json)
        # checks move location, displays error
        if self.is_empty(update['square']):
            self.mark_square(self._turn, update['square'])
            self.finish_turn()
            self._finished = self.done()
        else:
            # should modify state to display some kind of error
            pass

    def start(self):
        self._turn = self.x

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

    def is_empty(self, square):
        if self._board[square[0]][square[1]] == 'e':
            return True
        return False

    def mark_square(self, symbol, square):
        self._board[square[0]][square[1]] = symbol

    def finish_turn(self):
        if self._turn == 'x':
            self._turn = 'y'
        else:
            self._turn = 'x'

    def check_line(self, line):
        if 'e' not in line and 'o' not in line:
            return 'x'
        elif 'e' not in line and 'x' not in line:
            return 'o'
        else:
            return None
