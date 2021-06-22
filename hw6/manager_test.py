from p2 import *


def test():
    manager = NounManager()
    # f for fruit
    # a for animal
    manager.add("f", "apple")
    manager.add("f", "banana")
    manager.add("f", "cherry")
    manager.add("f", "dragonfruit")
    manager.add("f", "elderberry")
    manager.add("a", "ant")
    manager.add("a", "bear")
    manager.add("a", "cow")
    manager.add("a", "dog")
    manager.add("a", "eagle")
    print(manager.get_random())
    print(manager.get_random())
    print(manager.get_type("a"))
    print(manager.get_type("b"))
    print(manager.get("ant"))
    print(manager.get("wrong"))
    print(manager.is_type("ant", "a"))
    print(manager.is_type("ant", "b"))
    print(manager.remove("ant"))
    print(manager.get("ant"))


if __name__ == '__main__':
    test()
