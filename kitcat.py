from logging import getLogger
from random import randint
from enum import Enum


class Kitcat:
    """A simulation of a cat bot."""

    def __init__(self, name='', age=0, starting_state=None):
        self.name = name
        self.age = age
        self.state = starting_state

        if not self.name:
            self.name = 'mini_jinhai_{rand}'.format(
                rand=str(randint(0, 10000))
            )
        if not self.state:
            self.state = Kitcat.States.SLEEPING
        self._log = getLogger('Kitcat_{name}'.format(name=self.name))

    def hunt(self) -> None:
        """Transitions this Kitcat into a PATROLLING or ATTACCING state."""

        if self.state is Kitcat.States.PATROLLING:
            self.state = Kitcat.States.ATTACCING
        else:
            self.state = Kitcat.States.PATROLLING

    def serialize(self) -> dict:
        """
        Returns a dict representation of a Kitcat object
        (e.g. to pass into Flask's jsonify())
        """

        return {
            'name': self.name,
            'age': self.age
        }

    def __str__(self):
        return "Kitcat {name} (age {age}) is {state}!".format(
            name=self.name,
            age=self.age,
            state=self.state.name
        )

    class States(Enum):
        SLEEPING = 0
        PATROLLING = 1
        ATTACCING = 2
        PROTECCING = 3
