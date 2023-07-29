# super 有三种使用方式
# super()
# super(class1, class2)
# super(class, instance)
# super（超） 的作用: 找 那个 父类中的方法

#          A
#         / \
#        B   C
#         \  /
#           D

class A(object):
    def __init__(self, a):
        print("A init")
        self.a = a
        self.n = 2

    def add(self, m):
        print("A")
        self.n += m


class B(A):
    def __init__(self, c, b, a):
        print("B init")
        self.b = b
        # A.__init__(self, a)
        super().__init__(c, a)  # 不一定走到 A的 __init__ 内
        self.n = 3

    def add(self, m):
        print("B")
        # D 确定继承顺序
        super(B, D).add(self, m)  # mro 表根据D 来确定
        self.n += 3


class C(A):
    def __init__(self, c, a):
        print("C init")
        self.c = c
        # A.__init__(self, 2 * a)
        super().__init__(a)
        self.n = -1000

    def add(self, m):
        print("C")
        super(C, C).add(self, m)
        self.n += 4

    def show(self):
        print(self.d)
        print("~~~~~~~~~~~~~~~~~~***************~~~~~~~~~~~~~")


class D(B, C):
    def __init__(self, d, c, b, a):
        print("D init")
        self.d = d
        # B.__init__(self, b, a)
        # C.__init__(self, c, a)
        # super(B, D).__init__(self, c, a) # 跳过了B的初始化函数, D --> 确定我们的mro表的
        super(B, self).__init__(c, a) # 跳过了B的初始化函数, D --> 确定我们的mro表的
        self.n = 5
        # super(B, self).__init__()

    def add(self, m):
        print("D")
        super(D, D).add(self, m)
        self.n += 5
        self.n += 5

class Apple:
    def change(self):
        return '啊~ 我变成了苹果汁!'


class Banana:
    def change(self):
        return '啊~ 我变成了香蕉汁!'


class Mango:
    def change(self):
        return '啊~ 我变成了芒果汁!'


class Juicer:
    def work(self, fruit):
        print(fruit.change())

def func_demo():

    apple = Apple()
    banana = Banana()
    mongo = Mango()
    juicer = Juicer()

    while True:
        a = input("请输入一个整数:")
        a = int(a)

        if a > 100:
            juicer.work(apple)
        elif a > 50:
            juicer.work(mongo)
        elif a > 0:
            juicer.work(banana)
        else:
            print("请输入大于0 的整数")

        if a == -1:
            break


if __name__ == "__main__":
    func_demo()
    # b = B(2, 3)
    # print(B.__mro__)
    # print(D.__mro__)
    # d = D(4, 3, 2, 1)
    # super(B, d).show()
    # print("=============: ")
    # print(d.a)
    # # print(d.b)
    # print(d.c)
    # print(d.d)
    # print(D.__mro__)
    # print(B.__mro__)
    # d = D()
    # super(B, D).add(d, 10)  # B 找索引的起始位置， D 确定mro 表
    # super(B, d).add(10)  # d 表示直接传入一个instance，同时确定mro表
