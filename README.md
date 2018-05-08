# Unit testing
So, like, when you write code and stuff, sometimes it's useful to verify your assumptions. Even better, sometimes it's better to verify your assumptions _before_ running your actual application.

Here's a **simple class.**

TODO
```python
class Kitcat:
    """A simulation of a cat bot."""

    def __init__(self, name=None, )
```

Say we're about to integrate this class into another API project -- the **serialize** method sounds pretty important!

Okay, so our _assumption_ is that when I call `serialize()` on an instance of `Kitcat`, it'll return a dict representation of all of the fields of our object.

Let's test it _before_ integrating into our API!

TODO TEST CASE

No matter what test framework you use (we're using `unittest` here) all test frameworks operate on a basic principle called **assertions.**

```python
assert function_call() == some_value
```

_The value on the left should equal the value on the right. If it doesn't, raise an error._

TODO TEST OUTPUT

We have an error. Our `serialize()` method isn't returning a field that we expected to see.

Oooops, we forgot to include the `` field!

TODO TEST OUTPUT

Good thing we caught it before integrating the code into another project, huh?

### Cool activity??
Some dork is tryin' to merge his changes in the `feature/jinhai/enhanced-pounce` branch into `api`. As can be seen from the CI build, the tests are failing, which is a good indication that merging his changes will break the API. **Can you fix his feature branch and merge it once CI passes?**

## Test-Driven Development (TDD)
A common modern coding practice is to _invert_ this pattern. Like, instead of using automated tests to verify your assumptions, people use them to _create a standard

