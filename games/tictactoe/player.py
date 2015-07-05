from games.commons.player import Player


class TicTacToePlayer(Player):

    def __init__(self, piece):
        self._piece = piece

    def get_piece(self):
        return self._piece
