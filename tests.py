import classes
from serializer import *
import os

__all__ = ["run_all_tests"]


def test_basic_variables(filename: str):
    a = 1
    serialize(a, filename)
    b = deserialize(filename)
    assert a == b

    a = "some_string"
    serialize(a, filename)
    b = deserialize(filename)
    assert a == b

    a = True
    serialize(a, filename)
    b = deserialize(filename)
    assert a == b


def test_simple_obj(filename: str):
    a = classes.B(int_val=1, str_val="b", bool_val=True)
    serialize(a, filename)

    b = deserialize(filename)

    assert a.str_val == b.str_val
    assert a.int_val == b.int_val
    assert a.bool_val == b.bool_val
    assert id(a) != id(b)


def test_nested_obj(filename: str):
    temp = classes.B(int_val=1, str_val="b", bool_val=True)
    a = classes.A(int_val=1, str_val="b", bool_val=True, class_val=temp)
    serialize(a, filename)

    b = deserialize(filename)

    assert a.str_val == b.str_val
    assert a.int_val == b.int_val
    assert a.bool_val == b.bool_val

    assert a.class_val.str_val == b.class_val.str_val
    assert a.class_val.int_val == b.class_val.int_val
    assert a.class_val.bool_val == b.class_val.bool_val

    assert id(a) != id(b)


def run_all_tests():
    filename = "f1"
    test_basic_variables(filename)
    test_simple_obj(filename)
    test_nested_obj(filename)
    os.remove(filename)


if __name__ == '__main__':
    run_all_tests()
