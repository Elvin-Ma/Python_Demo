def my_add(a):
    print("my_add 1")
    return a

# a = 100

#闭包函数的实例
def outer(a):
    b = 100
    li = [100]
    def inner():
        nonlocal b
        b +=1
        li[0] +=1
        print(li)
        return a + b

    print(b)
    print(li)
    return inner

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
