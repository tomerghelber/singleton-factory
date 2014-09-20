__version__ = "1.0"


class SingletonFactory(type):
    """
    Singleton Factory - keeps one object with the same hash
        of the same cls.

    Returns:
        An existing instance.
    """
    __instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = dict()
        new_obj = super(SingletonFactory, cls).__call__(*args, **kwargs)
        if hash(new_obj) not in cls.__instances[cls]:
            cls.__instances[cls][hash(new_obj)] = new_obj
        return cls.__instances[cls][hash(new_obj)]

    def _unregiter(cls, obj):
        cls.__instances[cls].pop(hash(obj))
        if len(cls.__instances[cls]) == 0:
            cls.__instances.pop(cls)
