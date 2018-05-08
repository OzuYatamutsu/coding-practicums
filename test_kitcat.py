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

    def test_dangling_string_has_an_effect(self):
        test_cat = Kitcat(name='Kourii', age=22)

        test_cat.dangle_string()
        assert test_cat.state is Kitcat.States.ATTACCING

