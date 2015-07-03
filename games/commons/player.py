import uuid


class Player:

    @property
    def uuid(self):
        if not getattr(self, "_uuid"):
            self._uuid = uuid.uuid4()
        return self._uuid
