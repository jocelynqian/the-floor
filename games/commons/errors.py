"""Contains the custom error classes used by the application

Error Types:

    InvalidActionError -- Occurs when the user attempts an invalid action.

"""


class InvalidActionError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
