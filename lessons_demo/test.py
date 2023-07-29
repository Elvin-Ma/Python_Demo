def demo_type():
    a = True
    print(type(a))


def type_infer():
    a = 10
    b = int(10.1)
    c = int('10')
    d = float("10.1")
    print("===value b: ", b)
    print("===type b : ", type(b))


def int_base():
    a = int('0x18', base=16)
    print("======== value a: ", a)


def float_demo():
    data = 10.0
    print("data type: ", type(data))
    # data_2 = float("123")
    data_2 = 123.0
    print("data2 type: ", type(data_2))
    print("data2 value: ", data_2)


def bool_demo():
    bool_data = bool(-0.003)
    bool_str = bool(" ")
    bool_value = bool(0)
    bool_value2 = bool("False")
    bool_value3 = bool([])
    bool_value4 = bool(None)
    # print("bool_data value: ", bool_data)
    print("bool_str value: ", bool_str)


def if_demo():
    a = "0"
    if a:
        print("test.py : 32")


def complex_demo():
    """complex() can't take second arg if first is a string"""
    print("value0: ", complex(3, 4))
    # print("value1: ", complex("3"))
    print("value2: ", complex("4+5j"))


def string_demo():
    string_val = str(True)
    print("=====: string_val type: ", type(string_val))
    print("=====: string_val value: ", string_val)
    string_1 = 'hello  world'
    string_2 = "hello \\\n world"
    string_3 = '''hello world'''
    string_4 = """hello\tworld"""
    # print(string_1)
    print(string_4)


class A:
    def __init__(self):
        self.a = 10
        self.b = 100

    def add(self):
        return self.a + self.b

    def __dir__(self):
        return ["__add__"]


def dir_demo():
    a = A()
    b = dir(a)
    print(b)
    print("~~~~~~~~~~~~~~~~~~~~~`")
    c = a.__dict__
    print(c)


def my_function(a, b, c):
    d = a + b
    # pdb.set_trace()  # 设置断点
    e = d * c
    return e


def pdb_demo():
    import pdb
    result = pdb.runeval("1 + 2")
    print(result)
    # result = pdb.run("my_function(1, 2, 3)")
    # print(result)

import function_demo


if __name__ == "__main__":
    output = function_demo.my_div(3, 4)
    print(output)
    print("run test.py successfully !!!")
