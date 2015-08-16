import json
import random


from games.commons.game import Game
from games.commons.errors import InvalidActionError
from games.liars_poker import combos
from games.liars_poker.cards import Card, Deck
from games.liars_poker.player import LiarsPokerPlayer


class LiarsPoker(Game):

    def __init__(self):
        self._deck = None
        self._turn = None
        self._new_round = True  # True if turn is first of new round
        self._last_turn = None  # Only None at start
        self._last_combo = None  # Only None at start
        self._players = {}
        self._player_ordering = []

        self._min_seats = 2
        self._max_seats = 6
        self._hand_limit = 5

        self._started = False

    def _cards_to_json(self, cards):
        return [card.tuple() for card in cards]

    def _json_to_cards(self, cards):
        return [Card(card[0], card[1])for card in cards]

    def get_state(self, player_id):
        """Returns JSON containing current state of game visible to player.

        Contains:

            hand
                The given player's hand.
                It is a list of card symbols like ['10S', 'KD', 'QC']
            counts
                The number of cards each player that's still in the game has.
                It is a mapping from player ids to counts like
                {
                    '645102efdd8847b686b60df724d2fb73': 3,
                    'bed8e452dc2649a2b00741462119f78b': 2
                }
            new_round
                True if current turn is the first of a new round.
            turn
                The current turn's player's index in player_ordering.
            last_combo
                The last combo claimed.
            last_hands
                Hands last revealed. A mapping from player id to hand.
            player_ordering
                List of player ids representing the turn ordering.
            started
                Whether the game has started.
            error
                Contains None if there is no error, an Exception when an
                error has occurred.
        """
        if self._started:
            hand = self._cards_to_json(self._players[player_id].hand)
            counts = dict([
                (uuid, player.num_cards)
                for uuid, player in self._players.items() if not player.lost
            ])
            last_hands = dict([
                (uuid, self._cards_to_json(player.last_hand))
                for uuid, player in self._players.items()
            ])

            state = {
                'hand': hand,
                'counts': counts,
                'turn': self._turn,
                'new_round': self._new_round,
                'last_hands': last_hands,
                'last_combo': self._last_combo,
                'player_ordering': self._player_ordering,
                'started': self._started
            }
        else:
            state = {'started': self._started}

        return json.dumps(state)

    def update_state(self, player_id, update_json):
        """Updates game state based on player and update_json.

        update_json should contain:

            move
                This should be either 'challenge' or 'claim'.
            combo
                If the 'move' is 'combo', this should be the claimed combo.

        Returns:

            InvalidActionError
                If the update was invalid.
            None
                If the update was successful.
        """
        assert player_id == self._player_ordering[self._turn], 'Not your turn'
        update = json.loads(update_json)
        if update['move'] == 'challenge':
            if self._new_round:
                return InvalidActionError('No claim to challenge.')
            dealt_cards = []
            for p in self._players.values():
                dealt_cards.extend(p.hand)
            if combos.exists(dealt_cards, self._last_combo):
                losing_player_id = player_id
            else:
                losing_player_id = self._player_ordering[self._last_turn]
            losing_player = self._players[losing_player_id]
            losing_player.num_cards += 1
            if losing_player.num_cards > self._hand_limit:
                losing_player.lost = True
            self._deal()
            self._new_round = True
        elif update['move'] == 'claim':
            combo = update['combo']
            if not self._new_round and \
               not combos.greater_than(combo, self._last_combo):
                return InvalidActionError('Does not beat previous combo.')
            self._last_combo = combo
            self._new_round = False
        else:
            return InvalidActionError('Unknown action.')

        self._last_turn = self._turn
        num_players = len(self._players)
        for i in range(1, num_players):
            idx = (self._turn + i) % num_players
            if not self._players[self._player_ordering[idx]].lost:
                self._turn = idx
                break

    def _deal(self):
        for player in self._players.values():
            if player.lost:
                self.update_hand(None)
            else:
                hand = self._deck.draw(player.num_cards)
                player.update_hand(hand)

    def start(self):
        """Starts the game.

        Sets a player as the current turn and sets each player's hand.

        Errors if the number of players is not in the legal range.
        """
        assert not self._started, "Game already started"
        assert len(self._players) <= self._max_seats, "Too many players"
        assert len(self._players) >= self._min_seats, "Too few players"
        self._deck = Deck()
        self._player_ordering = list(self._players.keys())
        random.shuffle(self._player_ordering)
        self._turn = 0
        self._deal()
        self._new_round = True
        self._started = True

    def done(self):
        """Checks if the game is complete.

        The game is done if all but one player has lost.
        Returns the winning player id or None.
        """
        players_in_game = [
            player for player in self._players.values()
            if not player.lost
        ]
        if len(players_in_game) > 1:
            return None
        return players_in_game[0]

    def add_player(self):
        """Adds player to the game.

        Returns player_id of new player.
        """
        assert len(self._players) < self._max_seats, "This game is full."
        new_player = LiarsPokerPlayer()
        player_id = new_player.uuid.hex
        self._players[player_id] = new_player
        return player_id
