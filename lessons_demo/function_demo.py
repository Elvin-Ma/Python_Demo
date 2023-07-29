import module_demo


# function definition
def my_div(a, b):
    c = a / b
    print(f"{a} / {b} = {c}")
    return c


# function name assign
# new_div = my_div

def trigon(sign, layer):
    # output = my_div(3, 4)
    width = 2 * layer - 1
    for i in range(1, width + 1, 2):
        print((sign * (width + 1 - i)).center(width))


def return_demo(left, right):
    sum = left + right
    factor = left * right
    return sum, factor


def print_demo():
    print("print_demo()")


def func_demo():
    for i in range(5):
        print(i)
        return  # 函数立马结束


def my_abs(data):
    """
    return abs value of input
    :param data: input data
    :return: absolute value
    """
    return abs(data)


def max_demo():
    a = [-10, -2, 3, 5]

    def square(input):
        return input * input

    result = min(a, key=square)  #
    output = sorted(a, key=square, reverse=True)
    print(output)
    # print(f"result value: {result}")


def sum_demo():
    a = {x: x * x for x in range(10)}
    output = sum(a.values(), 100)
    print(output)


def func_type(a: int, b: list, c: tuple) -> tuple:
    print(a)
    print(b)
    print(c)
    return a, b, c


def type_demo():
    from typing import List, Dict

    def func(a: int, b: List[int]):
        print(a)
        print(b)

    func(8, [1, 2])


def my_sort_demo():
    from typing import List, Callable
    def my_sort(a: list, f: Callable[[int], int], c: bool) -> List[int]:
        return sorted(a, key=f, reverse=c)

    print(my_sort([-3, -2, 4, -10], abs, True))


def func_input_arg_demo():
    a = 10

    def func(a: int) -> None:
        a = 100

    li = [2, 3, 4]

    def func2(li: list):
        li.pop()
        li.append(100)
        # li = [20, 30, 40]

    # func(a)  # 函数的调用
    func2(li)
    print(li)


def arguments_demo():
    def func1(a=100, b=100):
        print(f"{a}, {b}")
        return a, b

    # func1(b=20, a=10)
    # func1()
    # func1(100) # SyntaxError

    def func2(b=10, *args):
        print(b)
        print(f"======: {args[0]}")
        print(type(args))
        # print(args)

    def func3(**aa):  # key world args
        print(type(aa))
        print(aa)

    def func4(*args, **kwargs):
        print(args)
        print(kwargs)

    # def func5(**kwargs, *args): # SyntaxError: invalid syntax
    #     print(args)
    #     print(kwargs)
    # func5(a=10, b=20, c=30, 1, 2, 3)

    def func6(*args, b=100):
        print(b)
        print(args)

    def func7(*args, b=100, **kwargs):
        print(b)
        print(kwargs)

    def func8(*args, **kwargs):  # a, b, c, *args, d = 1000, f = 100, **kwargs
        print(b)
        print(kwargs)

    # func6(1, 2, 3, b=-100)
    func8(1, 2, 3, c=100, d=100, f=300, b=-100)

    # func2(3, 4, 5)
    # func3()
    # func3(a=10, b=20, c=30)
    # func3(10, 20, 30)
    # func4(1, 2, 3, a=10, b=20, c=30)


def special_args_demo():
    def func(a, b, /):
        print("func argument / demo")
        return a + b

    # func(b=3, a=4) # TypeError: got some positional-only arguments passed as keyword arguments: 'a, b'

    def func1(*, a, b):
        print("func argument * demo")

    # func1(1, 3) # TypeError: takes 0 positional arguments but 2 were given
    # func1(b=3, a=4)

    def func2(a, b, /, c):
        print(a, b, c)

    func2(23, 4, c=100)

    def func3(a, b, /, *, c, d):
        print(a, b)
        print("~~~~~~~~~~~~~~~~~")
        # print(args)
        print("~~~~~~~~~~~~~~~~~")
        print(c, d)

    func3(4, 5, d=200, c=-100)
    func3(4, 5)

    # def func4(**kwargs, **worlds):
    #     print(kwargs)

    # def func5(*args, *arg):
    #     print(args)

    # 位置参数 vs 关键字参数
    # *args vs **kwargs
    # /, vs *
    # 位置参数，*args，关键字参数， **kwargs
    # 默认实参


def lambda_demo():
    # func1 = lambda a, b: a + b

    # func1(100, [i for i in range(10)])
    li = [-10, -5, 10, 4, 3]
    result = min(li, key=lambda a: a * a)  #
    # print(result)
    #
    # output = sorted(li, key=lambda a: a * a)
    # print(output)

    # dict2 = {"a": 10, "b": -10, "c": 4, "d": -5, "e": 3}
    # result = sorted(dict2)
    # def dict_value_abs(v):
    #     return abs(dict2[v])

    # output = sorted(dict2, key=lambda v: (dict2[v])**2)
    # output = sorted(dict2, key=dict_value_abs)

    # print(result)
    # print(output)

    ## 封包
    # return 1, 2, 3, 4
    # *args
    # a = 1, 2, 3, 4

    ##解包
    # a, b , c , d = (1, 2, 3, 4)
    # a, b , c , d, _ = (1, 2, 3, 4, 5)
    # a, b, *c, d, e = (1, 2, 3, 4, 5)
    # print(type(c))
    # print(c)
    # print(locals())
    # print(globals())


def pack_unpack_demo():
    # a = [1, 2, 3]
    # a, _, _, = (1, 2, 3) # 解包1
    # print(a)
    # print(*a)  # 解包2 --> 并没有复值给另外一些变量

    dict1 = {'a': 1, 'b': 2, 'c': 3}

    # a, b, c = dict1
    # print(a, b, c)
    # print(**dict1) # TypeError: print 不支持 可变的 kwargs的传参方式

    def dict_unpack(**kwargs):
        print(kwargs)

    def dict_unpack2(b, c, a):
        print(a)

    # dict_unpack(a=1, b=2, c=3)
    dict_unpack2(**dict1)


# def my_add(a):
#     print("my_add 1")
#     return a

# from module_demo import my_add # 我就import 进来一个函数
from module_demo import *

import module_demo

module_demo.my_add(100)


def my_add(a, b=10):
    print("my_add 2")
    return a + b


def list_demo():
    # list = [1, 2, 3] # overwrite list
    tu1 = (1, 2, 3)
    print(list(tu1))  # TypeError: 'list' object is not callable


# a = 100
# list（
# list = -100
# a = 100

def namespace_demo():
    list = 100
    print(list)


def eval_exec_demo():
    # print(eval("3 + 4"))

    # str1 = """a = 100; b = 100; print(a+b)"""
    str2 = """
a = 100
b = 10
print(a+b)
"""
    # str2 = """
    # ai
    # world
    # """
    # print(str2)
    # exec("""a = 100; b = 200; print(a+b)""")
    exec(str2.strip())


a = 100


# a += 10
# def outer():
#     # a += 10 # 报错的原因: a = 10; a = 它就觉得已经有了a了，--> 不会去查找全局变量了-->
#     # b = a + 10
#     # a = 100
#     # global a
#     a = -100
#     def inner():
#         # nonlocal a
#         global a
#         a = a + 10  # a += 10
#         print(a)  # UnboundLocalError: local variable 'a' referenced before assignment
#
#     inner()

# def variable_demo():
#     # global a #
#     a = -10000
#     def inner():
#         nonlocal a
#         a = a + 1
#         print(a)

def outer(li):
    # li = [2, 3]

    def inner():
        li2 = li.append(4)
        # li = li.append(10)
        print(li)

    inner()


def filter_demo():
    li1 = [x for x in range(10)]

    # def func(input):
    #     return input > 5  # 指定过滤的规则

    # output = filter(lambda input: False, li1)
    output = filter(None, li1)
    # print(li1)
    print(list(output))


def map_demo():
    li1 = [x for x in range(10)]

    output = map(lambda input: input * 2, li1)
    # print(li1)
    print(list(output))


def reduce_demo():
    from functools import reduce
    li1 = [x for x in range(1, 10)]  # [1, 2, ... 9] --> 1 * 2 = 2 * 3 = 6 * 4 = 24 * 5
    # def func(input1, input2):
    #     return input1 * input2
    output = reduce(lambda input1, input2: input1 * input2, li1)
    # output = reduce(func, li1)
    print(output)

# value_caching.get()
def recursive_demo(m):
    value_caching = {}

    # def func(m):
    #     m0 = 1
    #     m1 = 1
    #
    #     for _ in range(m-1):
    #         # 1: m0 = 1, m1 = 1 --> m0 = 1, m1 = 2
    #         # 2: m0 = 1, m1 = 2 --> m0 = 2, m1 = 3
    #         m0, m1 = m1, m0+m1 # 1 : 1 + 1 = 2() -->
    #
    #     print(m1)

    def func2(m):
        if m < 2:
            value_caching[m] = 1
            return 1

        if value_caching.get(m):
            return value_caching[m]

        output = func2(m -1) + func2(m -2) # func(50) --> func(51), func(52)--> func(51) + func(50)
        value_caching[m] = output

        return output # func(5) --> func(4) + func(3) --> func(3) + func(2) + func(2) + func(1)(

    print(func2(m))

if __name__ == "__main__":
    a = list([1, 2, 3])
    recursive_demo(100)
    # reduce_demo()
    # filter_demo()
    # map_demo()
    # outer([2, 3])
    # variable_demo()
    # outer()
    # eval_exec_demo()
    # namespace_demo()
    # list_demo()
    # output = my_div(10, 2)  # call function
    # result = my_div(12, 4)
    # trigon('*', 10)
    # sum, factor = return_demo(4, 5)
    # print(print_demo())
    # print(func_demo())
    # print(my_abs.__doc__)
    # help(my_abs)
    # print(abs.__doc__)
    # max_demo()
    # sum_demo()
    # output = func_type(10, [20], (30,))
    # type_demo()
    # my_sort_demo()
    # func_input_arg_demo()
    # arguments_demo()
    # special_args_demo()
    # lambda_demo()
    # pack_unpack_demo()
    # module_demo.my_add(10)  # 有效的避免命名空间冲突
    # print(func_type.__annotations__)
    print("run function_demo.py successfully !!!")
