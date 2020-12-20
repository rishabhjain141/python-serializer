class B(object):
    def __init__(self, int_val: int, str_val: str, bool_val: bool):
        self.int_val = int_val
        self.str_val = str_val
        self.bool_val = bool_val

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class A(object):
    def __init__(self, int_val: int, str_val: str, bool_val: bool, class_val: object):
        self.int_val = int_val
        self.str_val = str_val
        self.bool_val = bool_val
        self.class_val = class_val

    def double_int_val(self) -> int:
        self.int_val *= 2
        return self.int_val

    def flip_bool_val(self) -> bool:
        self.bool_val = not self.bool_val
        return self.bool_val

    def append_str_val(self, new_str) -> str:
        self.str_val += new_str
        return self.str_val

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
