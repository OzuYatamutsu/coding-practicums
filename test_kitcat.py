from unittest import TestCase
from kitcat import Kitcat


class TestKitcat(TestCase):
    def test_serialize(self):
        test_cat = Kitcat(name='Jinhai', age=24)

        assert test_cat.serialize() == {
            'name': 'Jinhai',
            'age': 24,
            'state': 'SLEEPING'
        }
