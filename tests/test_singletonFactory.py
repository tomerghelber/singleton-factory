from unittest import TestCase

from singleton_factory import SingletonFactory


class SingletonFactoryA(object, metaclass=SingletonFactory):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)


class SingletonFactoryB(object, metaclass=SingletonFactory):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)


class TestSingletonFactory(TestCase):
    def setUp(self):
        SingletonFactory._SingletonFactory__instances = dict()

    def test_same_type_same_hash(self):
        instance1 = SingletonFactoryA("name")
        instance2 = SingletonFactoryA("name")
        self.assertEqual(instance1, instance2)
        self.assertEqual(hash(instance1), hash(instance2))
        self.assertEqual(id(instance1), id(instance2))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances[SingletonFactoryA]))

    def test_same_type_different_hash(self):
        instance1 = SingletonFactoryA("name")
        instance2 = SingletonFactoryA("name1")
        self.assertNotEqual(instance1, instance2)
        self.assertNotEqual(hash(instance1), hash(instance2))
        self.assertNotEqual(id(instance1), id(instance2))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances))
        self.assertEqual(2, len(SingletonFactory._SingletonFactory__instances[SingletonFactoryA]))

    def test_different_type_same_hash(self):
        instance1 = SingletonFactoryA("name")
        instance2 = SingletonFactoryB("name")
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(hash(instance1), hash(instance2))
        self.assertNotEqual(id(instance1), id(instance2))
        self.assertEqual(2, len(SingletonFactory._SingletonFactory__instances))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances[SingletonFactoryA]))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances[SingletonFactoryB]))

    def test__unregiter_removed_object(self):
        instance1 = SingletonFactoryA("name")
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances[SingletonFactoryA]))
        SingletonFactoryA._unregiter(instance1)
        self.assertEqual(0, len(SingletonFactory._SingletonFactory__instances))

    def test__unregiter_let_create_same_hash(self):
        instance1 = SingletonFactoryA("name")
        SingletonFactoryA._unregiter(instance1)
        instance2 = SingletonFactoryA("name")
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(hash(instance1), hash(instance2))
        self.assertNotEqual(id(instance1), id(instance2))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances))
        self.assertEqual(1, len(SingletonFactory._SingletonFactory__instances[SingletonFactoryA]))
