import random

RANKS = set(range(1, 14))
SUITS = {'D', 'C', 'H', 'S'}


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def tuple(self):
        return (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = [
            Card(rank, suit)
            for rank in RANKS
            for suit in SUITS
        ]
        random.shuffle(self.cards)

    def draw(self, n):
        return [self.cards.pop() for i in range(n)]
