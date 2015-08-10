import json

from unittest import TestCase

from games.commons.errors import InvalidActionError
from games.liars_poker.liars_poker import LiarsPoker


class LiarsPokerTest(TestCase):
    def test_init_state(self):
        game = LiarsPoker()
        p1_id = game.add_player()
        p2_id = game.add_player()
        game.start()
        p1_state = json.loads(game.get_state(p1_id))
        p2_state = json.loads(game.get_state(p2_id))

        assert not game.done()
        assert 1 == len(p1_state['hand'])
        assert p1_state['new_round']
        assert p1_state['last_combo'] is None
        ordering = p1_state['player_ordering']
        assert 2 == len(ordering)
        assert ordering[p1_state['turn']] in (p1_id, p2_id)
        assert p1_state['last_hands'][p1_id] == []
        assert p1_state['last_hands'][p2_id] == []
        assert p2_state['hand'] != p1_state['hand']
        assert p1_state['counts'][p1_id] == 1
        assert p1_state['counts'][p2_id] == 1

    def test_challenge(self):
        game = LiarsPoker()
        p1_id = game.add_player()
        game.add_player()
        game.start()

        p1_state = json.loads(game.get_state(p1_id))
        ordering = p1_state['player_ordering']

        update = dict(move='challenge')
        result = game.update_state(ordering[0], json.dumps(update))
        assert type(result) == InvalidActionError

        update = dict(move='claim', combo=['triple', 3])
        assert not game.update_state(ordering[0], json.dumps(update))

        update = dict(move='challenge')
        assert not game.update_state(ordering[1], json.dumps(update))

        s = json.loads(game.get_state(ordering[0]))
        assert s['counts'][ordering[0]] == 2
        assert s['counts'][ordering[1]] == 1

        update = dict(move='claim', combo=['single', s['hand'][0][0]])
        assert not game.update_state(ordering[0], json.dumps(update))

        update = dict(move='challenge')
        assert not game.update_state(ordering[1], json.dumps(update))

        s = json.loads(game.get_state(ordering[0]))
        assert s['counts'][ordering[0]] == 2
        assert s['counts'][ordering[1]] == 2

    def test_claim(self):
        game = LiarsPoker()
        p1_id = game.add_player()
        game.add_player()
        game.start()

        p1_state = json.loads(game.get_state(p1_id))
        ordering = p1_state['player_ordering']

        update = dict(move='claim', combo=['pair', 3])
        assert not game.update_state(ordering[0], json.dumps(update))
        update = dict(move='claim', combo=['pair', 10])
        assert not game.update_state(ordering[1], json.dumps(update))
        update = dict(move='claim', combo=['single', 13])
        result = game.update_state(ordering[0], json.dumps(update))
        assert type(result) == InvalidActionError
        update = dict(move='claim', combo=['triple', 3])
        assert not game.update_state(ordering[0], json.dumps(update))
