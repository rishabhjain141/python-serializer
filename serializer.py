import importlib

STANDARD_DATA_TYPES = {str, bool, int}
STANDARD_DATA_TYPES_NAMES = {"str", "bool", "int"}

__all__ = ["serialize", "deserialize"]


def serialize(obj, filename: str = None) -> str:
    if type(obj) in STANDARD_DATA_TYPES:
        data = str({"module": type(obj).__module__, "class": type(obj).__name__, "val": obj})
    else:
        attributes = obj.__dict__.copy()
        for key, val in attributes.items():
            if type(val) in STANDARD_DATA_TYPES:
                attributes[key] = {"module": type(val).__module__, "class": type(val).__name__, "val": val}
            else:
                attributes[key] = serialize(val)
        data = str({"class": type(obj).__name__, "module": obj.__module__, "attributes": attributes})
    if filename:
        with open(filename, "w") as fp:
            fp.write(data)
    return data


def deserialize(filename: str = None, obj_data: object = None):
    if filename:
        with open(filename, "r") as fp:
            data = eval(fp.read())
    else:
        data = obj_data

    class_ = getattr(importlib.import_module(data["module"]), data["class"])

    if data["class"] in STANDARD_DATA_TYPES_NAMES:
        return eval(data["class"])(data["val"])

    kwargs = dict()
    for key, val in data["attributes"].items():
        if type(val) == str:
            val = eval(val)
        kwargs[key] = deserialize(obj_data=val)

    return class_(**kwargs)
