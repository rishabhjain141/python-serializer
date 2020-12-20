import classes
from serializer import *
from tests import *

if __name__ == '__main__':
    run_all_tests()

    b = classes.B(2, "b", True)
    a = classes.A(1, "is", False, b)
    a.double_int_val()
    a.flip_bool_val()

    print("Creating a complex obj which contains variables which are custom classes itself")
    print(a)

    print("Serializing complex obj")
    serialize(a, "s1")

    with open("s1", "r") as fp:
        data = fp.read()
        print("Serialized data", data)

    print("Returned obj after deserialization")
    print(deserialize("s1"))
