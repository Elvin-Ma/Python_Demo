# 类的定义: 高内聚，低耦合
class Compute:
    '''
    # 类中的函数 --> 方法;
    # 主要的一个功能：设置类的初始化状态，--> 设置类的属性
    # (姓名、性别、年龄) --> 属性；（eat sleep）--> 方法
    '''

    def __init__(mmm, input1, input2):
        mmm.a = input1
        mmm.b = input2

    # 理解一些self
    def add(mmm):
        return mmm.a + mmm.b
    #
    # # self : 自己 --> 将来实例化之后的对象自己
    # def mul(self):
    #     return self.a * self.b
    #
    # def div(self):
    #     return self.a / self.b
    #
    # def minus(self):
    #     return self.a - self.b


def class_demo():
    # 实例化一个类
    computor1 = Compute(4, 5)  # 调用 __init__ 方法 --> 构造一个类的实例
    print("computor1 attr: ", computor1.__dict__)
    computor2 = Compute(40, 50)  # 调用 __init__ 方法 --> 构造一个类的实例
    print("computor2 attr: ", computor2.__dict__)

    # 调用类里面的具体的方法
    output = computor1.add()
    # output = computor.minus()
    # output = computor.mul()
    # output = computor1.div()

    print("=========output: ", output)


# 默认继承自object
# 类 : 属性 + 方法
# 属性: 类属性(类变量) + 实例属性(实例变量)
# 方类: 实例方法 + 类方法 + 静态方法
# Teacher : 类的名称 ---> instance = Teacher(name, age, address)
class Teacher(object):
    count = 0  # 类属性 --> 注意定义的位置

    def __init__(self, name, age, address):
        self.name = name  # self --> 实例
        self.age = age  # 实例属性
        self.address = address  # 实例变量：实例的属性
        self.show_time()
        self.data = 100  # __dict__
        self.count = 100  # 与 类属性 count 同时存在，只是查找顺序不一样
        Teacher.count += 1

    # 实例方法
    def show_time(self):
        print(f"大家好! 我是{self.name}, 今年{self.age}岁, 家住在{self.address}, 欢迎大家有空来玩哦!")

    def add_data(self, data):
        self.data += data

    # 实例方法
    def get_up(self):
        print(f"{self.name}起床")

    # 实例方法
    def wash(self):
        print(f"{self.name}刷牙")
        print(f"{self.name}洗脸")

    # 实例方法
    def eat(self):
        print(f"{self.name}吃菜")
        print(f"{self.name}扒饭")

    # 实例方法
    def clock_in(self):
        print(f"{self.name}今日打卡成功")

    def work(self):
        print(f"{self.name}授课")
        print(f"{self.name}答疑")
        print(f"{self.name}写代码")

    def sleep(self):  # self 表示的是一个实例化之后的对象
        self.age = 100
        self.data = [1, 2, 3]
        print(f"{self.name}睡觉")

    # 装饰器
    @classmethod
    def counter(cls):
        print(f"当前统计的老师人数是: {cls.count} 人")

    @staticmethod
    def counter_v1():
        print(f"Teacher static method !!!")


def attr_control():
    '''
    setattr:
    delattr:
    hasattr:
    getattr:
    '''
    teacher = Teacher("ma lao shi", 30, "陆家嘴")
    Teacher.count = 100
    print(getattr(Teacher, "aaa", -1))
    # result = teacher.name
    # setattr(teacher, "age", 100)
    # # delattr(teacher, "age")
    # if (hasattr(teacher, "age")):
    #     result = getattr(teacher, "age")
    # print("~~~~~~~: ", result)


def class_demo():
    teacher = Teacher("ma lao shi", 30, "陆家嘴")
    teacher2 = Teacher("mmm", 18, "陆家嘴")
    # teacher.age = 18
    # teacher.sleep()
    # print("teacher's data: ", teacher.data)

    Teacher.count = 100
    Teacher.data = [10, 20, 30]  # 类变量 --> 公用的
    print("teacher data: ", teacher.data)  #
    print("teacher2 data: ", teacher2.data)  #


def teacher_demo():
    teacher1 = Teacher("老王", 40, "人民广场")  # 定义了一个具体的teacher
    teacher2 = Teacher("ma lao shi", 40, "人民广场")  # 定义了一个具体的teacher
    teacher1.sleep()  # 实例方法的调用
    Teacher.sleep(teacher2)  #
    # Teacher.counter() # 类方法的调用
    # Teacher.counter_v1(Teacher) # 静态方法的调用 --> 和类没有任何关系 -->
    # counter_v1(Teacher)

    # 实例方法、静态方法、类方法 --> 方法 --> 只不是是调用方式不同而已
    # teacher1.sleep()
    # Teacher.sleep(teacher1) # 通过类名直接调用
    #
    # Teacher.counter()

    # teacher1.counter_v1(teacher2)
    # teacher1.counter_v1(teacher1)
    # teacher1.counter_v1(Teacher)
    # Teacher.counter_v1(teacher1)
    # Teacher.counter_v1(teacher2)
    # Teacher.counter_v1(Teacher)

    # teacher2.get_up() # get_up 是一个实例方法 --> 隐式的

    # teacher2.count = -100
    # teacher2.count = 100 # 只有teacher2 变了 --> 在这个teacher1 里面新建了一个 count
    # Teacher.count = 100 #
    # print("count : ", Teacher.count)
    # print("count : ", teacher2.count)  # 先查找自己的属性，再查找 类属性
    # name = teacher1.name
    # age = teacher1.age
    #
    # teacher1.get_up()
    # teacher1.wash()
    # teacher1.eat()
    # teacher1.clock_in()
    # teacher1.work()
    # teacher1.eat()
    # teacher1.work()
    # teacher1.eat()
    # teacher1.wash()
    # teacher1.sleep()
    # teacher1.counter()


# 属性和方法标识符含义
# 不带下划线: public
# 带一个下划线: 这个属性或方法 是私有的，不推荐用户直接访问，但用户也可以直接访问
# 带两个下划线: 强制性的将一个属性或方法变为私有的属性或方法，从语法上约束用户不能直接访问
class Person:
    def __init__(self, name, age):
        # self._name = name
        self.__name = name  # 私有属性
        if age <= 0:
            self.__age = "年龄必须大于0"  # 私有属性
        else:
            self.__age = age  # 私有属性

    # 利用非私有方法访问私有属性
    def show_info(self):
        print(f"姓名:{self.__name}\n年龄:{self.__age}")

    # 私有方法
    def __sleep(self):
        print("我要睡觉了, 晚安!")

    # 利用非私有方法调用私有方法
    def sleep(self):
        self.__sleep()


def person_demo():
    ps = Person("赵六", 26)
    # ps.sleep()
    # ps._Person__sleep()  # AttributeError: 'Person' object has no attribute '__sleep'. Did you mean: 'sleep'?
    # name = ps._Person__name
    # print(name)


# 父类
class Person:
    state = "China"
    score = 0

    def eat(self):
        print("score: ", self.score)
        print('吃饭')

    def speak(self):
        print('说话')


# person的子类
class Student(Person):
    score = 100

    def study(self):
        print('读书')

    # def eat(self):
    #     print("Student eat.")


class Worker(Person):
    def work(self):
        print('搬砖')


def inher_demo():
    ps = Person()
    ps.eat()
    stu = Student()
    print(Student.state)  # 子类调用父类的属性
    stu.study()  # 子类调用自己的方法
    stu.eat()  # 子类调用父类的方法
    stu.speak()  # 子类调用父类的方法

    # wk = Worker()
    # print(Worker.state)
    # wk.work()  # 子类调用自己的方法
    # wk.eat()  # 子类调用父类的方法
    # wk.speak()  # 子类调用父类的方法


class Animal:
    def eat(self):
        print('吃东西')


class Cat:
    def catch_mouse(self):
        print('抓老鼠')

    def eat(self):
        print('cat 吃东西')


class Ragdoll(Cat, Animal):  # 继承多个父类
    def cute(self):
        print('卖萌')


def multi_inher_demo():
    c1 = Ragdoll()
    # c1.cute()  # 子类调用自己的方法
    # c1.catch_mouse()  # 子类调用Cat父类的方法
    c1.eat()  # 子类调用Animal父类的方法


class A(object):
    def __init__(self, a, n):
        self.a = a  # 设置属性 : self.__dict__["a"] = a
        self.n = n  # 设置属性 : self.__dict__["n"] = n

    def add(self, m):
        self.n += m


class B(A):
    def __init__(self, b, a, n):
        # A.__init__(self, a, n)  # 子类中构造父类
        super().__init__(a, n)  # 子类中构造父类
        self.n += 4
        self.b = b

    def add(self, m):
        # super(B, C).add(self, m)
        self.n += 2


def func():
    data = B(5, 6, 9)
    # print("===========: ", data.b)
    print("===========: ", data.a)


# class C(B):
#     def __init__(self):
#         self.n = 3
#
#     def add(self, m):
#         # super(C, C).add(self, m)  # B 代表什么
#         self.n += 3


if __name__ == "__main__":
    func()
    # multi_inher_demo()
    # inher_demo()
    # class_demo()
    # teacher_demo()
    # class_demo()
    # attr_control()
    # person_demo()
    print("run my_add successfully !!!")
