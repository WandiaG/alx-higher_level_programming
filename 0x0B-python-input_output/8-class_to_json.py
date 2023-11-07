#!/usr/bin/python3

def class_to_json(obj):
    """Returns the dictionary description with simple data structure,
    of an object.

    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """
    # print("type of obj --> {}".format(type(obj)))
    return obj.__dict__
