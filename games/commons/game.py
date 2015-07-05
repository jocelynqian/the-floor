import uuid


class Game(object):

    def get_state(self, player_id):
        raise NotImplementedError

    def update_state(self, player_id):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    @property
    def uuid(self):
        if not getattr(self, "_uuid", None):
            self._uuid = uuid.uuid4()
        return self._uuid

    def done(self):
        raise NotImplementedError

    def add_player(self):
        raise NotImplementedError
