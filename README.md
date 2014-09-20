[![Build Status](https://travis-ci.org/tomerghelber/singleton_factory.svg)](https://travis-ci.org/tomerghelber/singleton_factory/)
[![Coverage Status](https://coveralls.io/repos/tomerghelber/singleton_factory/badge.png)](https://coveralls.io/r/tomerghelber/singleton_factory)

singleton_factory
=================
Python implements for singleton factory pattern.

As it's sound, an object that can create a lot of instance but each instance is a singleton (can be created only once).
Requiring the same object with the same parameters on `__init__` will return the existing object.

Usage
=====
SingletonFactory is a type so we need to put it as metaclass:

``` python
from singleton_factory import SingletonFactory


class SingletonFactoryA(object, metaclass=SingletonFactory):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)
```

Additional, we want to override the function of hash so we will control when  to instances are equals.
We are doing that in case that an object can get some arguments in init and create the same objects (or wanted object).
That means the object will be created twice but only the oldest one will be returned.
The use is regularly. See the tests for more data.