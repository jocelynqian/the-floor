from games.commons.player import Player


class LiarsPokerPlayer(Player):

    def __init__(self):
        self.hand = []
        self.last_hand = []
        self.num_cards = 1
        self.lost = False

    def update_hand(self, new_hand):
        self.last_hand = self.hand
        self.hand = new_hand
