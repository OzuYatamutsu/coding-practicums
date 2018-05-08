# Unit testing
So, like, when you write code and stuff, sometimes it's useful to verify your assumptions. Even better, sometimes it's better to verify your assumptions _before_ running your actual application.

Here's a **simple class.**

TODO
```python
from logging import getLogger
from random import randint
from enum import Enum

class Kitcat:
    """A simulation of a cat bot."""

    def __init__(self, name='', age=0, starting_state=Kitcat.States.SLEEPING):
        self.name = name
        self.age = age
        self.state = starting_state

        if not self.name:
            self.name = 'mini_jinhai_{rand}'.format(rand=str(randint(0, 10000)))
        self._log = getLogger('Kitcat_{name}'.format(name=self.name))

    def hunt() -> None:
        """Transitions this Kitcat into a PATROLLING or ATTACCING state."""

        if self.state is Kitcat.States.PATROLLING:
            self.state = Kitcat.States.ATTACCING
        else:
            self.state = Kitcat.States.PATROLLING

    def serialize(self) -> dict:
        """Returns a dict representation of a Kitcat object (e.g. to pass into Flask's jsonify())"""

        return {
            'name': self.name,
            'age': age
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
```

Say we're about to integrate this class into another API project -- the **serialize** method sounds pretty important!

Okay, so our _assumption_ is that when I call `serialize()` on an instance of `Kitcat`, it'll return a dict representation of all of the fields of our object.

Let's test it _before_ integrating into our API!

```python
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
```

No matter what test framework you use (we're using `unittest` here) all test frameworks operate on a basic principle called **assertions.**

```python
assert function_call() == some_value
```

_The value on the left should equal the value on the right. If it doesn't, raise an error._

```
F
======================================================================
FAIL: test_serialize (test_kitcat.TestKitcat)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/secollin/personal-dev/coding-practicums/test_kitcat.py", line 12, in test_serialize
    'state': 'SLEEPING'
AssertionError

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

We have an error. Our `serialize()` method isn't returning a field that we expected to see.

```python
# ...serialize()
return {
    'name': self.name,
    'age': self.age
}
```

Oooops, we forgot to include the `state` field!

```diff
diff --git a/kitcat.py b/kitcat.py
index 723966a..8af5fc8 100644
--- a/kitcat.py
+++ b/kitcat.py
@@ -35,7 +35,8 @@ class Kitcat:
 
         return {
             'name': self.name,
-            'age': self.age
+            'age': self.age,
+            'state': self.state.name
         }
```

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Good thing we caught it before integrating the code into another project, huh?

### Cool activity??
Some dork is tryin' to merge his changes in the `feature/jinhai/enhanced-pounce` branch into `api`. As can be seen from the CI build, the tests are failing, which is a good indication that merging his changes will break the API. **Can you fix his feature branch and merge it once CI passes?**

## Test-Driven Development (TDD)
A common modern coding practice is to _invert_ this pattern. Like, instead of using automated tests to verify your assumptions, people use them to _create a standard
