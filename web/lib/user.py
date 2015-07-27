"""
Manages the users for the web app.

# TODO(paul): Move users to a database
"""

# Maps usernames to the user object
users = {}

# Maps player id to user
player_user = {}


class UserAlreadyExistsException(Exception):
    pass


class InvalidUserNameException(Exception):
    pass


class User(object):
    def __init__(self, name):
        self.name = name
        self.player_ids = set()


def create_user(name):
    """Creates a user with the name.

    Raises UserAlreadyExistsException if the user already exists.
    Raises InvalidUsernameException if name is invalid.
    Returns the created user.
    """
    if not _is_valid_name(name):
        raise InvalidUserNameException()

    if name in users:
        raise UserAlreadyExistsException()

    user = User(name)
    users[name] = user
    return user


def get_user(name):
    """Returns the user with the name or None."""
    return users.get(name, None)


def add_player(user, player_id):
    """Associates a user with a player."""
    if player_id in player_user:
        assert user != player_user[player_id], \
            'Player %s associated with another user.' % (player_id)
        return
    user.players.add(player_id)
    player_user[player_id] = user


def get_user_by_player(player_id):
    return player_user[player_id]


def _is_valid_name(name):
    """Returns whether a name is valid."""
    return name.isalnum()
