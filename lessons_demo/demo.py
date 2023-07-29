"""a = 10
b = 11.0

print("ren gong zhi neng: ", a, "ma lao shi : ", b)
print("ren gong zhi neng  %d ,  ma lao shi: %0.3f " % (a, b))  # 传统的 格式化 字符串的方式"""

"""
a = chr(97)
b = ord(a)
print("a value", a)
print("b value", b)
# TypeError: ord() expected a character, but string of length 2 found
b = ord("ad")"""

"""PI = 3.1412
print("%010f" % PI)  # 总宽10，小数位3，右对齐，空格
print("%0.*f" % (6, PI))  # 没有指定总宽度，不指定小数位，默认小数后6位
print("%-*.*f" % (6, 4, PI))  # 超参范围按照原样显示，可以有多个*，.之后没有参数默认就是0了
print("%#x" % 24)  # 输出具体格式
print("0x%x" % 24)"""

"""一个整体(.format 是“”是一个字符串， format 是字符串内置的函数)，print("=====", 100)
a = 100
b = 1.34
print("a value: {}, b value: {:-.6f}, str value {}".format(a, b, "AAAA"))  # 按照默认顺序
print("a value: {2}, b value: {0}, str value {1}".format(a, b, "AAAA"))  # 可以指定顺序
print("a value: {2}, b value: {0}, str value {1}, a value: {0}".format(a, b, "AAAA"))  # 可以重复
print("a value {m}, b value: {n}, c value: {m}".format(m=10, n=100.3)) # 传参的方式，--> 键值对传参方式
print("a value {a}, b value: {b}, c value: {a}".format(a=a, b=b))  # 传参的方式，--> 键值对传参方式
==================== {}: 不简单 --> {2} --> 变量；
print("{:b>8.2f}".format(3.141592653))  # 打出来a了 --> 功能强化， 可以填充a
print("%8.2f" % (3.141592653))  # a 没有打出来 不支持填充其它的
print("{:,}".format(123456780))
print("{:x}".format(123456780))
print("{:o}".format(123456780))
print("{:b}".format(123456780))
print("{:d}".format(123456780))"""

"""a = 100.02
b = "ai"
c = b.upper()
d = 1e+2
f = 1e-2
print(f"d value: {d}, f value: {f}")
print(f"value {a:8.3}, str b : {c}")"""

"""
# 字符串对象方法 == 字符串对象 + 方法
# 字符串对象 --> 类的实例
# 所有的这些对象，基本上都是有一些内置函数的，这些内置函数 就叫做 方法；
# format 也是 字符串的一种内置方法，“dddd”.format()
# 常见报错信息：valueError TypeError IndexError NameError
# str1 = "aaaLine1 Line2 Line3aaa"
# str1 = "  \tLine1 Line2 Line3 \n"
# str2 = str1.replace("Li", "C", 2)
# print(f"str value: {str2}")
# print(f"str value: {str1}")
# print(f"str value: {str1.rstrip('a')}")
# str2 = "www.example.com"
# print(str2.strip("eco.")) # 匹配规则：只要是 m e c o w . 中的一个即满足删除规则 --> 循环式删除

# str3 = "mmmmmmmmm"
# print(str3.center(11, "a"))  # 原始字符串
# print(str3.ljust(11, "a"))  # 原始字符串
# print(str3.rjust(11, "a"))  # 原始字符串

# str3 = "path/helloworld.txt"
# str4 = '1123'
# print(str3.rpartition('l'))
# print(str3.rpartition('ll'))
# print(str3.startswith('h', 1, 4))
# print(str3.startswith(('h', 'e')))
# print(str3.isalpha())
# print(str4.isdigit())
# output = str3.split('/', maxsplit=1)  # 可以指定最大分割次数
# output1 = str3.rsplit('/', maxsplit=1)  # 可以指定最大分割次数
# print(type(output))

# str5 = '\\'
# str6 = "hello world"
# print(str5.join(str6)) # join 和 split 是相反的一对用法

# str7 = "aa"
# str8 = ['1', '2', '3'] # list
# print(str7.join(str8))
# print(str8.join(str7)) # 为什么不行 ？？？ --> join 是 字符串的内置方法，只有由字符串来调用

# str9 = "path1"
# str10 = ['path10']
# print(str9.join(str10))"""

# list --> 底层数据是存储在一个个的分开的空间中的 -->
# a = [[0], 2, 3]  # list --> 可变数据类型
# print("a[0] id pre: ", id(a[0]))
# a[0][0] = 100  # list 内部的数据类型 都可以不一样
# print("a[0] id after: ", id(a[0]))
# print(a)

# string 底层存储存储在一个连续空间中的
# str1 = "hello world" # string 是一种不可变数据类型 number 也是一种不可变的数据类型
# print("str1 id: ", id(str1))
# str1 = str1 + " python"  # 新建了一份数据
# print("str1 id after: ", id(str1))

# 构造、 增、 删、 改、 查
# 索引：[] --> 所有编程语言的索引号，都是从 0 开始的；
"""list1 = ['h', 'e', 'l', 'l', 'o', '!', 'w', 'or', 'l', 'd']  # 很多个元素 -->
list1[1] = 100
list2 = list1[0:4]  # 切片操作 --> 通过索引来切 [] --> [0, 4): 左闭右开
list3 = list1[-2: 0: -2]  # 取到最后 --> 可以指定 方向 和 步长 step
list4 = list1[-3:]  #
list4[0] = 10000  # list1 中的值没有改 --> 这种行为好不好呢?
# list5 = list1[::-1]
# list3 = list1[-1:-2] # 没有报错 --> 取了个寂寞[]
# print(id(list5))
# list5 = list1[::-1]
# list1[0:6:2] = ['H', 'E', 'L']  # 长度需要相等
list1[0:3] = [1, 2, 3, 4, 5]  # 整块替换
print(list1)"""

"""# TypeError: 'int' object is not iterable(可迭代的)
# 6 中基本数据类型，处理 数字类型， 其它 5种都是可迭代的
# 只要是可迭代的对象，都可以通过list(aa) 显示构造一个list 对象
aa = "python"
print(list(aa))"""

"""
# a = [5, 2, 4, 1, 5]  # list
# a[:2] = [0, 0, 0, 1, 1, 1]
# a.append(100)
# a.append("python")
# a.insert(100, 2)
# a.insert(2, 100)  # 插到2号索引之前了
# a.insert(2, [100, 100, 100])
# a.insert(-2, 1000)
# a[1:1] = [5, 5, 5, 5, 5]
# b = [-10, 10, -3, 10.5, 10, -5]  # list --> 直接隐式构造一个 list
# b = list()  # 把其它的数据类型 转化 成 一个 list
# a.append(b)
# print(a)
# a.extend(b)
# b = a[0:5]
# b.sort()  # 调用 list 内置的函数
# b.sort(reverse=True)
# b.sort()
# print(b)
# b.sort(key=abs)  # 经过函数变换之后的值进行排序 --> python 中list 内置的函数 --> 类的内置方法
# print(b)
# # print(f"c is {c}")

# c = sorted(b)  # 这种排序方式也可以 --> 调用 python 内置的函数
# print(f"b value: \n {b}")
# list 的内置方法改变这个list 本身，而 python自带的这些函数不改变本身；
# print(b)
# b.reverse()
# c = reversed(b)  # reversed 同样也是python 自带的函数，--> b 的数据类型可以不是list；
# print(b)
#
# c = b.index(10)
# num = len(b)  # 很常用
# print(f"10 index: {c}")
# print(b)
# c = b.copy()
# print("b id: ", id(b))
# print("c id: ", id(c))
# c[0] = -10000
# print("b value: ", b)
# print("c value: ", c)

# d = b  # 没有copy 直接将一个变量赋值给另外一个变量
# print("b id: ", id(b))
# print("d id: ", id(d))
# b[0] = -10000
# print("b value: ", b)
# print("d value: ", d)

# li1 = [1, 2, 3, 4, 5]
# li1.clear()
# del li1[:]
# print(li1)

# print(3 in li1)"""

"""
## tuple --> 元组
# t = (1, 2)
# tu1 = ("ai", 2)
# print(type(tu1[0]))
# print(type(tu1[1]))
# print(tu1)
# tu1[0] = 100 # TypeError --> tuple --> 不可更改的数据类型
# t = ()
# print(type(t)) # empty tuple

# t1 = ("ai") # 在很多语言中，一个变量加一个（）
# t1 = (3 == 5)
# t2 = (2,)  # tuple
# print(type(t1))  # type --> int

t1 = (1, 2, [2, [2, 3], 5])
# t1[2].append(4) # true : 改变的是tuple 中 一个 可变数据 里的值
# t1[2] = 100 # --> wrong
# t1[0] = 100 # --> wrong
# print(type(t1))
# print(t1)
# output = t1[2][1][0]
# print("output: ", output)
#
# li2 = [1, 2, [1, 2]]
# li1 = list(t1)  # tuple --> list
# tu2 = tuple(li2)  # list --> tuple
#
# cnt = tu2.count(1)
# idx = tu2.index(2)
# print("cnt 1: ", cnt)
# print("iex 2: ", idx)
# print("len li2: ", len(tu2))

# tu2 = (2, 3) * 3
# li1 = [1] * 100
# li2 = [2, 2, 2] + li1 # 重新生成了一个list， 不是在原来list基础上 extend
# # print(tu2)
# tu3 = (2, 3) + (4, 5)  # right or wrong ??? --> 重新生成了一个变量
# print(tu3)
"""

# dict
"""
d1 = {"a": 1, "b": 2, "c": 3}  # 查找速度快，空间消耗大
# print(d1[0])  # wrong --> KeyError
# print(d1[0:])  # wrong --> TypeError
# d2 = {[1, 2, 3]: "a"} # TypeError: unhashable type: list
# d2 = {"a": [1, 2, 3]}  # key 必须是一种不可变的数据类型
# d3 = {(1, 2, 3): "tuple"}  # a:b --> key:value
# d4 = {1: 3, 2: 5, "a": [1, 2, 3]}
# d5 = {([1, 2, 3], 2, 3): "tuple"}  # https://www.python.org/
# d6 = {"a": 1, "b": 2, "c": 3, "a": 100}  # 1. 重复的key值，不会报错；2. key 值只能存在一份；3.后来的key 会覆盖原来的key
d7 = {"a": 100, "b": 100, "c": -100}  # value 可以是重复的

# li1 = []
# li1[0] = 100  # IndexError
# print(li1)

# d8 = {}
# print(type(d8))
# print(d7["c"])  # 用key 来索引 --> 得到的是 value 值
# d7["c"] = 100  # 会重建一个新的key：value 添加到我们的dict 中
# print(d7)

# 在python中 = 左边必须是一个变量
# d9 = dict("A" = 10, "b" = 100, "c" = 10)
# d10 = dict(A=10, b=-10, c=100)  # 通过传参的方式来定义一个dict
# print(d10)
# A = "aa"
# d11 = {A: "b"}
# print(d11["aa"]) #
# d11 = dict(A:10, B: 100, c: -100) #
# d12 = dict("a":100, "b": 100)
# print(d10["A"])
# print(d10[A]) # NameError

# d13 = dict(([1, 2], ("a", "b"), ("v", 2), (5, 3)))  # ValueError --> (): key: value

# output = zip([1, 2, 3], ["a", "b", "c"])
# print(list(output))
# d14 = dict(output) # zip 拉链操作，--> 先一一配对
# print("d14: ", d14)

# d15 = dict.fromkeys(("ai", "a", "cd"), "we are students")
# d16 = dict.fromkeys(("ai", "a", "cd"), "we", "are", "students") # TypeError: zip([1, 2, 3], ["a", "b", "c"])
# d17 = dict.fromkeys(("ai", "a", "cd"), ("we", "are", "students")) # TypeError: zip([1, 2, 3], ["a", "b", "c"])

z15 = zip("abcd", "1234")  # 转 list、tuple、set 都可以，转 dict 失败，--> (a, b) 二元组才可以
z16 = zip("abc", "1234", "3333", "eegeg")  # 以最短的为主
z18 = zip("abcd")
z17 = zip()
# print(set(z15))
# print(set(z16))
# print(list(z16)) # 迭代器到底了 --> 为空
d18 = dict(z15)
# print(d18)
# print(d18.keys()) # dict_keys: 字典的 所有的keys 单独拿出来
# print(d18.values()) # dict_values: 字典的所有 values 单独拿出来
# item = d18.items()
# print(item)  # 返回key：value 键值对的 序列
# d18["a"] = 1000
# print(item) # item 自动更新 --> 视图 ？？？

# output = d18.get("e", "none value")  # "e" : key, 不存在则返回 “none value”
# result = d18["e"] # KeyError
# print("output: ", output)
# print("result: ", result)
# d18.update({"1": 100, "d": 1000})
# d18.update([("aa", 1000), (3, 100), ("c", -10900), ("a", -10000)])  #
# output = d18.pop("a", "bbb") # 删除的同时，返回该key 对应的 value，假如没有这个key，返回默认值，假如没有默认值呢？ --> KeyError
# print(d18)
# output = d18.popitem() # 返回删除的item，以tuple的类型返回
# print(output)

# print(d18)
# output = d18.setdefault("e", -1000)  # 1. 是有返回值的；2. dict中已有的key 不会被覆盖；3.  假如dict中没有这个key，则用default value来填充
# # d18["e"] = None
# d18["a"] = -1000  # 一定会set 一个 item， 可能会覆盖初始值
# print(output)
# print(d18)
#
# d18["a"] = [1, 2, 3]
# d19 = d18.copy()  # 浅拷贝
# d18["a"][0] = -999  # 仅修改d18
# print("d19: ", d19)
# print("d18: ", d18)

# d18.clear()
# print(d18)
"""

# set
# s0 = {}  # dict
# s1 = set()  # empty set
# s2 = {1, 2, 3}  # set
# s3 = {100, -2, -4, 50}  # 注意顺序 --> 无序的
# s3.pop()  # 可变的数据类型
# s4 = {2, 4, 5, 5, 4, 2}  # 重复元素清楚
# # s5 = {[1, 2, 4], [2, 3, 4]} # TypeError: unhashable type: list --> 和 dict 中 key的要求是一致的
# # s6 = {(1, [1, 2, 3], 3)} # TypeError: unhashable type: 'list'
# s6 = {(1, 1, 3), (1, 1, 3)}  # TypeError: unhashable type: 'list'
# s7 = set("abc")
# # s8 = set([1, 2, 3])
# s9 = set({"a": 1, "b": 2, "c": 3}) # dict --> set: 提取了key
# s10 = frozenset([1, 2, 3])
# print(s10)
#
# s1 = set("abcd")
# s2 = set("cdefg")
# s3 = {"e": 3, "f": 5, "a":6}
# s3 = set("dfasf")
# print("s1: ", s1)
# print("s2: ", s2)
# print("s3 是否包含 s1: ", s1 <= s3)  # s1 and s3 类型相同
# print("s2 - s1: ", s2 - s1)
# print("s2 和 s1 并集", s2 | s1)
# print("s2 和 s1 交集", s2 & s1)
# print("s2 和 s1 异或: ", s2 ^ s1)

# d1 = {"e": 3, "f": 5, "a": 6, "d": 7, "g": None}
# d2 = "xyze"
# s4 = set("efa")
# s5 = set("axy")
# print(s4.isdisjoint(d1)) #
# print(s4.issubset(d1)) # d1 不一定是 set 类型
# print(s4.union(d1, d2))  # d1 不一定是 set 类型 --> s4 本身并没有改变 --> 生成了一个新的set
# print(s4.intersection(d1, d2))  # d1 不一定是 set 类型 --> s4 本身并没有改变 --> 生成了一个新的set
# print(s4.intersection_update(d1, d2))  # d1 不一定是 set 类型 --> s4 本身并没有改变 --> 生成了一个新的set
# print(s4)


# print(s4) # s4 本身并为改变
# output = s4.intersection(d1, d2)
# output = s4.symmetric_difference(s5)
# print(output)

# a = 999
# print(a)
# del a
# print(a)

# del
"""
## 启动的方式不一样，启动的优化级别也是不一样的，了解一下 -->
# a = 999
# b = 999 #
# b = a  # 发生了什么 --> 引用 -->  别名 --> 底层都是指向同一个地址：--> 引用计数管理机制 ——>
# c = b
# print("id a: ", id(a))  # id a == id b
# print("id b: ", id(b))
# del a  # 删除一个变量 --> 有没有实实在在的删除一个地址上的数据呢？？？？？ --> 视情况而定？？？ -->
# del b  # 彻底删除 999 这个数据 --> 释放内存空间
# # print(a)
# print(b)

# a = [1, 2, 3, 4, 5, 6]
# del a[0]
# print(a)
# del a[0:3]
# print(a)
# del a[:]
# print(a)  # 删除所有的元素 --> a  可以使用
# del a
# print(a)  # 整体删除 --> 变量无法使用

# d = {"a": 1, "b": 2, "c": 3}
# d1 = d
# del d["a"]
# del d
# print(d) # NameError
# print(d1)

# t1 = (1, 2, 3, 4)
# t2 = (1, 2, 3, 4)
# del t1[0] # TypeError
# del t1
# print(t1)
# print(t2)
# print(id(t1))

li1 = [1, 2, 3]
li2 = [1, 2, 3]
print(id(li1))
print(id(li2))

str1 = "abc"
str2 = "abc"
print(id(str1))
print(id(str2))

set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(id(set1))
print(id(set2))
"""

import copy

# t1 = ("abc", 123)
# t2 = copy.copy(t1)
# print("t1 id: ", id(t1))
# print("t2 id: ", id(t2))
# t1 = ("abc", 123, [1, 2, 3]) # tuple 是一个不可变的数据类型
# t2 = copy.copy(t1)
# print("t1[0] id: ", id(t1[0]))
# print("t2[0] id: ", id(t2[0]))
# print("t1[2] id: ", id(t1[2]))
# print("t2[2] id: ", id(t2[2]))

# 浅copy
# 可变数据类型--> id 会发生改变 --> 仅仅是第一层发生改变，里面的id并未发生改变
# why ？ --> 1. 节约空间（回答为为什么里边的算数id不变）；2. 还是要有独立性（t2 还是要单独控制 --> 但是控制的不彻底）
# t1 = ["abc", 123, [1, 2, 3]]
# # t2 = t1
# t2 = copy.copy(t1)
# t2.append(10)
# print(t1)
# print(t2)
# print("t1 id:", id(t1))
# print("t2 id:", id(t2))
# print("t1[0] id: ", id(t1[0]))
# print("t2[0] id: ", id(t2[0]))
# print("t1[2] id: ", id(t1[2]))
# print("t2[2] id: ", id(t2[2]))

# t1 = [[1, (1, 2), 3], (1, 2), 2]
# t2 = copy.deepcopy(t1)
# # t2 = copy.copy(t1)
# print("======: ", id(t1[0][1]))
# print("======: ", id(t2[1]))
# print("t1[0][0]", id(t1[0][0]))
# print("t1[0][0]", id(t2[0][0]))
# print("t1[1] id: ", id(t1[1])) # same
# print("t2[2] id: ", id(t2[1]))

# t1 = ([1, 2], [3, 4])
# t2 = copy.deepcopy(t1)  # id update
# print("t1 id:", id(t1))
# print("t2 id:", id(t2))

## copy 和 deepcopy 最直观的区别:
## 1. 一个变量里（无论层次多深）只要存在一个可变的数据类型，id就会改变；
## 2. 浅copy 只拷贝可变数据类型的最外层；
## 3. 深copy 将存在的所有可变数据类型copy一份；

## 拷贝：copy 的肯定是可变的数据类型；
## 浅copy：就是第一层；
## 深copy：所有层的可变数据类型都会copy一份；

# tu1 = ([1, 2, 3], [2, 3, 4])
# tu2 = copy.copy(tu1)
# tu3 = tu1
# tu1[0][0] = 100
# print(tu1)
# print(tu2)
# print("tu1 id: ", id(tu1))
# print("tu2 id: ", id(tu2))
#
# li1 = [1, 2, 3, [1, 2, 3]]
# li2 = li1.copy()  # 浅copy
# li2 = copy.deepcopy(li1)  # 浅copy
#
# print(id(li1[3]))
# print(id(li2[3]))

# a = 1 + 1
# b = 4 / 5
# c = 10 // 5  # 取整
# print(b)
# print(c)

# d = 3 ** 2
# d = 3 ^ 3 # 按位操作了

# 10 % 3 --> 10 - (3 * 3) = 1
# -10 % 3 --> -10 - (3 * -4) = 2
# d = -10 % 3
# print(d)
#
# d = 10**3
# d = 1e3
# print(d)

# a = 2
# b = 3
# # b %= a #
# # b = b + a
# # b **= a
# b //= a
# b = b // a
# print(b)
#
# string = "hello world"
# print((length := len(string)) + 5)
# print(f"string len: {length}")
#
# list1 = [1, 2, 3]
# list2 = list1
#
# # += 可以用于可变数据类型，也可以用于不可变数据类型
# # 1. 当用于不可变数据类型时，会新建一个变量；
# # 2. 当用于可变数据类型时，修改的可变数据类型本身；
# list1 = list1 + [3, 4] # 一定是新建一个变量
# # list1 += [3, 4]
# print(list1)
# print(list2)

# a, b, _, _, _ = {3, 4, -2, -4, 6}
# # a, b, c, d, e = "hello"
# print(a, b)

# a = b = c = [1, 2, 3]
# c = 999
# b = c
# a = b
# d = 999
# b.append(4)
# print(a)
# print(b)
# print(c)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

a = 2
b = []

# print(a and b) # True
# step1: and or not : 可以理解为一个函数 ： 返回值 a or b
# step2: output --> 隐式转化为 bool 类型

#
# print(not a)
# if a or b:
#     print("==============")
#     print(b and a)  # True

# def all(input):
#     print("===================")
#     for item in input:
#         if not item:
#             return False
#     return True
#
# def any(input):
#     for item in input:
#         if item:
#             return True
#     return False

# a = all([]) # result = True --> result = False return
# a = any([1, 2, 3])
# b = any([]) # result = false --> for item in b: if item: return true;
# print(a)
# print(b)

# a = [1, 2, 4]
# b = [1, 2, 4]
# print(a is b)

# a = ([1, 2, 3, 4],)
# print(type(a))
# b = copy.copy(a)
# print(a is b)
# print(bin(8))
# print(bin(-100))

# print(bin(3))
# print(bin(4))
# print(-3 & -4)
# print(-3 | -4)
# print(bin(7))
# print(~3)
# print(bin((-1)))
# print(-23 << 2)
# print(23 << 2)
#
# print(~-100)
# print((14 + 3) & ~3)
# print((25 + 7) & ~7) # align --> 数据对齐 :
# print((25 + 15) & ~15) #
# print(bin(14))
# print(bin(3))
# print(bin(14+ 3))
# 14 : 00001110; 3: 00000011; 17: 0001,0001
# ~3: 1111,1100 & 0001, 0001
# 0001,0000

# if elif else : python 的关键字；
# if 和 elif 后面要跟一个表达式
# else 后边不用跟表达式：前面的都不满足，就执行else里的内容
# : 不要忘记
# 多个分支是互斥的，只能进一个分支
# if .. elif .. elif

# golden
# if 4 > 2:
#     print("======:", __file__)
# elif True:
#     print("~~~~~~~~~~~")
# else:
#     print("***********")

# 变形1：if
# 变形2：if ... else:
# 变形3：if .. elif .. elif ..
#
# a = 10
# b = 99
#
# st1 = "完美"
# st2 = "不太完美"
# c = st1 if b == 100 else st2
# print(c)

# a = 5
# while a < 100:
#     print(f"a value: {a}")
#     a -= 1 # 100

# a = 5
# while True:
#     a += 1
#     print(f"a value: {a}")
#     if a == 100:
#         break  # 中断 --> 推出整个循环

# a = 5
# while a < 10:
#     print(f"a value: {a}")
#     a += 1
#     if a == 8:
#         break #
# else:
#     print("============== in while else.")

# a = 0
# b = [1, 2, 3, 4]
# data = "ai technoledge"
# data2 = (1, 2, 3)
# data3 = {2, "ai", "shenlan"}
# data4 = {"b": 100, "a":200, 100:"shenlan"} # 遍历字典，遍历的是字典的key
#
# data5 = [("b", 100), ("a", 200), (100, "shenlan")]
#
# key, value = (100, 200)
# for key, value in data4.items():
#     print(key)
#     for i in data2:
#         print(i)
#     # a += i
#     # print(f"i value: {key} : {value}")
#     print(f"i value: {key}")
# else:
#     print("============in for else.")

# li1 = [1, 2, 3, 4, 5]
# li2 = ["a", "b", "c", "d", "e"]
# k_value = 5

# for i in range(len(li1)):
#     print(f"li1 value: {li1[i]}")
#     print(f"li2 value: {li2[i]}")

# a = range(100, 0, -2)
# set1 = {"a": 100, "b": 200, "c": 300}
# a = enumerate(set1)
# print(list(a))
# for index, item in enumerate(set1, start=100):
# print(f"index: {index}")
# print(item)
# print(type(item))

# a = [[1, 2, 3], [3, 4, 5], [4, 5, 6]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print(f"a[i,j] = {a[i][j]}")
#         break # 直接跳出当前循环
#     print(f"i value: {i}")

# a = 3
# while a < 100:
#     while a < 5:
#         break
#
#     a += 1
#     print("we are in while True")

# print(f"a value: {a}")

# li1 = [1, 2, 3, 4, 5, 6, 7]
# for i in li1:
#     if i != 5:
#         continue
#         # break
#     print(f"====== i value: {i}")

# a = []
# for i in range(100):
#     a.append(i*i)
#
# li1 = [i * i for i in range(100) if i == 50]  # 列表推导式
#
# # li2 = [(i, j * j) for i in range(100) for j in range(100) if i == j]
# li2 = [(i, j * j) for i in range(100) for j in range(100)]
# # print(len(li2))
#
# li3 = [[i + j for i in range(10)] for j in range(4)]
# print(li3)

# print(abs.__doc__)
# help(abs)
# help("keywords")
# import builtins
# print(dir(builtins))
# help()

# dic1 = {x: x * x for x in range(10, 20, 2) if x != 10}
# dict2 = {x: y for x, y in zip((1, 2, 3), ('a', 'b', 'c'))}
# print(dict2)

# if a:
#    # IndentationError:

# if a:
#     pass

# list1 = [i for i in range(10)]
# print(list1)
#
# for item in list1:
#     list1.remove(item) # len 已经减少了 -->
#     print(len(list1))
#
# print(list1)
# del list1[:]
# print(list1)

# list1 = [i for i in range(10, 20, 2)]
# list2 = [i for i in range(10, 20, 2)]
#
# for item in list2:
#     list1.remove(item)
#
# list1 = [[1, 2, 3], [1, 5, 6], [7, 8, 9]]
# list2 = list1 #
# list2 = list(list1)
# list2[0][0] = -100
# print(f"list1 id: {id(list1[0][0])}, list2 id: {id(list1[1][0])}")
# list2 = list1.copy()
# import copy
# list2 = copy.copy(list1)
# for item in list2:
#     list1.remove(item)

# print(list1)
# dict1 = {x: x * x for x in range(20, 10, -2)}
# for item in dict1.keys():  # RuntimeError --> dict 在迭代的时候不能改变大小
#     # dict1.pop(item)
#     dict1.update(a=10)
#     print(dict1['a'])
#     print(item)
#     dict1["a"] = 100

# dict1 = {x: x * x for x in range(20, 10, -2)}
# dict2 = dict1
# tuple1 = tuple(dict2.keys())

# print(tuple1)
# dict2.pop(20)
# print(tuple1)
# dict2_keys = list(dict2.keys())
# for key in dict2_keys:  # RuntimeError --> dict 在迭代的时候不能改变大小
#     # print(tuple1)
#     dict1.pop(key)
#     # print(tuple1)

# set1 = {i*i for i in range(10)}
# set2 = set1.copy()
# for item in set2:
#     set1.remove(item)
#
# print(set1)
# print("run demo.py successfully !!!")
