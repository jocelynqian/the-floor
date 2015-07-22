import uuid


class Game(object):

    def get_state(self, player_id):
        """Returns JSON containing current state of game visible to player"""
        raise NotImplementedError

    def update_state(self, player_id):
        """Updates the state after player action"""
        raise NotImplementedError

    def start(self):
        """Begins the game"""
        raise NotImplementedError

    @property
    def uuid(self):
        if not getattr(self, "_uuid", None):
            self._uuid = uuid.uuid4()
        return self._uuid

    def done(self):
        """Checks if the game has been completed"""
        raise NotImplementedError

    def add_player(self):
        """Adds a player to the game"""
        raise NotImplementedError
