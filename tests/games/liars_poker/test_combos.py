from unittest import TestCase

from games.liars_poker.cards import Card
from games.liars_poker import combos


class ComboExistsTest(TestCase):
    def test_single(self):
        cards = [Card(13, 'S'), Card(2, 'H')]
        assert combos.exists(cards, ('single', 13))
        assert not combos.exists(cards, ('single', 6))

    def test_pair(self):
        cards = [Card(13, 'S'), Card(2, 'H'), Card(13, 'D')]
        assert combos.exists(cards, ('pair', 13))
        assert not combos.exists(cards, ('pair', 2))
        assert not combos.exists(cards, ('pair', 6))

    def test_two_pair(self):
        cards = [Card(13, 'S'), Card(13, 'D'), Card(13, 'C'),
                 Card(2, 'H'), Card(2, 'C'),
                 Card(3, 'H')]
        assert combos.exists(cards, ('two-pair', 13, 2))
        assert not combos.exists(cards, ('two-pair', 13, 3))
        assert not combos.exists(cards, ('two-pair', 6, 2))

        with self.assertRaises(combos.IllegalCombo):
            assert combos.exists(cards, ('two-pair', 13, 13))

    def test_triple(self):
        cards = [Card(13, 'S'), Card(2, 'H'), Card(2, 'D'),
                 Card(13, 'D'), Card(13, 'C')]
        assert combos.exists(cards, ('triple', 13))
        assert not combos.exists(cards, ('triple', 2))
        assert not combos.exists(cards, ('triple', 6))

    def test_straight(self):
        pass

    def test_flush(self):
        pass

    def test_fullhouse(self):
        pass

    def test_four_of_a_kind(self):
        pass

    def test_straight_flush(self):
        pass

    def test_unknown_combo(self):
        cards = [Card(13, 'S'), Card(13, 'D')]
        with self.assertRaises(combos.IllegalCombo):
            assert combos.exists(cards, ('blah', 4))


class GreaterThanTest(TestCase):
    def test_sample(self):
        ordered_combos = [
            ('single', 4),
            ('single', 7),
            ('pair', 3),
            ('pair', 13),
            ('two-pair', 4),
            ('two-pair', 9),
            ('triple', 3),
            ('triple', 10),
            ('straight', 3),
            ('straight', 8),
            ('flush', 'D'),
            ('flush', 'S'),
            ('fullhouse', 3, 7),
            ('fullhouse', 4, 7),
            ('four-of-a-kind', 3),
            ('four-of-a-kind', 8),
            ('straight-flush', 'D', 5),
            ('straight-flush', 'D', 7),
            ('straight-flush', 'H', 3),
        ]

        num_combos = len(ordered_combos)
        for i in range(num_combos):
            c1 = ordered_combos[i]
            if i == num_combos:
                break
            for c2 in ordered_combos[i + 1:]:
                assert combos.greater_than(c2, c1)
                assert not combos.greater_than(c1, c2)
