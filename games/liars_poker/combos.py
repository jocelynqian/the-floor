from collections import defaultdict

from games.liars_poker.cards import Card


class IllegalCombo(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Illegal combo: %s' % (self.value,)

COMBO_TYPES = {
    'single': ('rank',),
    'pair': ('rank',),
    'two-pair': ('rank', 'rank',),
    'triple': ('rank',),
    'straight': ('rank',),
    'flush': ('suit', 'rank',),
    'fullhouse': ('rank', 'rank',),
    'four-of-a-kind': ('rank',),
    'straight-flush': ('suit', 'rank',),
}


def _list_to_idx_lookup(l):
    return dict([(l[i], i) for i in range(len(l))])

RANK_ORDER = range(2, 14) + [1]
TYPE_ORDER = ['single', 'pair', 'two-pair', 'triple', 'straight', 'flush',
              'fullhouse', 'four-of-a-kind', 'straight-flush']

# Mappings to power values
RANK = _list_to_idx_lookup(RANK_ORDER)
SUIT = _list_to_idx_lookup(['D', 'C', 'H', 'S'])
TYPE = _list_to_idx_lookup([c for c in TYPE_ORDER])


def greater_than(combo1, combo2):
    type1 = combo1[0]
    type2 = combo2[0]

    if type1 != type2:
        return TYPE[type1] > TYPE[type2]

    params = COMBO_TYPES[type1]
    for param, v1, v2 in zip(params, combo1[1:], combo2[1:]):
        print params
        print param, v1, v2
        assert param in ['rank', 'suit']
        if v1 == v2:
            continue
        if param == 'rank':
            return RANK[v1] > RANK[v2]
        else:
            return SUIT[v1] > SUIT[v2]


def rank_counts(cards):
    result = defaultdict(int)
    for card in cards:
        result[card.rank] += 1
    return result


def suit_counts(cards):
    result = defaultdict(int)
    for card in cards:
        result[card.suit] += 1
    return result


def exists(cards, combo):
    t = combo[0]
    r_counts = rank_counts(cards)
    s_counts = suit_counts(cards)
    if t == 'single':
        return r_counts[combo[1]] > 0
    elif t == 'pair':
        return r_counts[combo[1]] > 1
    elif t == 'two-pair':
        if combo[1] == combo[2]:
            raise IllegalCombo('Need different ranks for two-pair.')
        return r_counts[combo[1]] > 1 and r_counts[combo[2]] > 1
    elif t == 'triple':
        return r_counts[combo[1]] > 2
    elif t == 'straight':
        if combo[1] != 2 and combo[1] < 11:
            raise IllegalCombo('Illegal straight')
        for i in range(5):
            if r_counts[combo[1] + i] == 0:
                return False
        return True
    elif t == 'flush':
        return s_counts[combo[1]] > 4
    elif t == 'fullhouse':
        if combo[1] == combo[2]:
            raise IllegalCombo('Need different ranks for fullhouse.')
        return r_counts[combo[1]] > 2 and r_counts[combo[2]] > 1
    elif t == 'four-of-a-kind':
        return r_counts[combo[1]] == 4
    elif t == 'straight-flush':
        if combo[1] != 2 and combo[1] < 11:
            raise IllegalCombo('Illegal straight-flush')
        suit = combo[1]
        rank = combo[2]
        for i in range(5):
            if not cards.contains(Card(rank + i, suit)):
                return False
        return True
    else:
        raise IllegalCombo('Unknown combo name %s' % (combo[0],))
