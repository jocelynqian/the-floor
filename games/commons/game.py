import uuid

class Game:

    
    def get_state(self):
        raise NotImplementedError

    def update_state(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    @property
    def uuid(self):
        if not getattr(self, "_uuid"):
            self._uuid = uuid.uuid4()
        return self._uuid


    def done(self):
        raise NotImplementedError



    
