def div_v1(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")

    except ZeroDivisionError:
        print('try中发生了除数为0的异常')

    except:
        print('发生了除0以外的异常')

    else:
        print('try中没有异常')


def div_v2(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")

    # e：ZeroDivisionError('division by zero')
    except ZeroDivisionError as e:
        print(isinstance(e, ZeroDivisionError))
        print(e)
        print(ZeroDivisionError('dived by zero'))
    finally:
        print("发生啥我都会执行.")


class MyError:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class MyError2(Exception):
    def __init__(self, message):
        self.message = message


def define_exception():
    print(MyError("发生了一个异常"))
    print(MyError2("发生了一个异常"))


import traceback


def div_v3(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    except:
        print("异常发生啦！！！")
        # traceback.print_exc() #打印异常信息的 traceback  将 traceback 打印到控制台中，以便我们查看应用程序执行时发生的异常信息。
        # print(res := traceback.format_exc())# 返回一个字符串，其中包含完整的异常信息的 traceback。这允许我们将 traceback 存储在日志文件中，或者将其以其他格式发送到远程服务器等。
        # print(type(res)) # 字符串
    finally:
        print("肯定执行我")


def func2():
    import traceback

    def func1():
        func2()

    def func2():
        func3()

    def func3():
        try:
            x = 1 / 0
        # except:
        #     tb = traceback.format_exc()
        #     traceback.print_tb(tb) # print_tb() 方法会将完整的 traceback 打印到控制台中。
        finally:
            print("==============")

    func1()


if __name__ == "__main__":
    # div_v2(2, 1)
    # div_v2(2, 0)
    # div('2', 2)
    # define_exception()
    # div_v3('3', 54)
    func2()
    print("run exception_demo.py successfully !!!")
