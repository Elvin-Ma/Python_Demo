import numpy as np
from typing import Iterable
from aa import add_demo
from ctypes import string_at

def demo_1():
    a = np.array([[2, 3], [4, 5]], dtype=np.float32)
    print(a)
    
def demo_2():
    # arr1 = np.array((1, 2, 3))
    # arr1 = np.array(range(1, 4))
    arr1 = np.array([1, 2, 3]).astype(np.float32)
    print(arr1)
    print(type(arr1))
    print(isinstance(arr1, np.ndarray))
    print(isinstance(arr1, Iterable))

    print(arr1.ndim)
    print(arr1.shape)
    print(arr1.size)
    print(arr1.dtype)
    print(arr1.itemsize)

    arr2 = np.array([[1, 2, 3], [4, 5, 2147483648]]).astype(np.int64)
    print(arr2)
    print(arr2.ndim)
    print(arr2.shape)
    print(arr2.size)
    print(arr2.dtype)
    print(arr2.itemsize)


    arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12.]]])
    print(arr3)
    print(arr3.ndim)
    print(arr3.shape)
    print(arr3.size)
    print(arr3.dtype)
    print(arr3.itemsize)


    arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=np.float32)
    print(arr4)
    print(arr4.ndim)
    print(arr4.shape)
    print(arr4.size)
    print(arr4.dtype)
    print(arr4.itemsize)


    arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12.]]], dtype=np.int32)
    print(arr5)
    print(arr5.ndim)
    print(arr5.shape)
    print(arr5.size)
    print(arr5.dtype)
    print(arr5.itemsize)


    arr6 = np.array(13)
    print(arr6)
    print(type(arr6))
    print(arr6.ndim)
    print(arr6.shape)
    print(arr6.size)
    print(arr6.dtype)
    print(arr6.itemsize)
    
def demo_3():
    aa = [4, 5.0]
    print(type(aa[0]))
    print(type(aa[1]))
    
    arr1 = np.array(((2, 3, 4), (4, 5, 6)), dtype=np.int32)
    arr2 = np.array(arr1)
    print(arr2)
    print(type(arr2))
    print(arr2.ndim)
    print(arr2.shape)
    print(arr2.size)
    print(arr2.dtype)
    print(arr2.itemsize)
    
def demo_4():
    import numpy as np
    # obj = [1, 2, 3]  # a是array_like
    obj = np.array([1, 2, 3])  # a是ndarray
    arr1 = np.array(obj) #实实在在的有另外一份数据 raw_data：改变了； meta_data:没变 --> id 改变
    arr2 = np.asarray(obj) # raw_data:没变； meta_data:也没变 --> id 不变
    arr3 = arr2.reshape(3, 1) # raw_data:没变； meta_data: 变了 --> id 发生改变；
    arr2[0] = 5
    # obj[1] = 4
    # print(obj)
    print(obj.ctypes.data) # 数据内存上的地址
    print(arr1.ctypes.data)
    print(arr2.ctypes.data)
    
    # print(string_at(obj.ctypes.data, obj.nbytes).hex())  # transpos
    # print(string_at(arr1.ctypes.data, arr1.nbytes).hex())
    # print(string_at(arr2.ctypes.data, arr2.nbytes).hex())
    
    print(arr1)
    print(arr2)
    print(arr1 == arr2)

    # asarray中的dtype和obj不匹配
    # obj = np.array([1, 2, 3])
    # arr1 = np.array(obj, dtype=np.float32)
    # arr2 = np.asarray(obj, dtype=np.float32)
    # obj[1] = 4
    # print(obj)
    # print(arr1)
    # print(arr2)
    
def demo_5():    
    # a1 = [1, 2, 3]
    # arr1 = np.copy(a1)
    # print(arr1)

    a2 = np.array([1, 2, 3])
    arr2 = np.copy(a2) # 重新申请了内存，并且把数据copy了进去
    print("==============:")
    print(id(a2))
    print(id(arr2))
    print(arr2)
    
def demo_6():
    import numpy as np
    iterable = (x*x for x in range(5))
    print(np.fromiter(iterable, dtype=np.float64))

def demo_7():
    print(np.empty((2, 3)))
    print(np.empty((2, 3), dtype=np.int32))
    
    a = ([1, 2, 3], [4, 5, 6])
    print(np.empty_like(a))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.empty_like(a))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.empty_like(a, dtype=np.int32))
    
    print(np.zeros((2, 3)))
    print(np.zeros((2, 3), dtype=np.int32))
    
    a = ([1, 2, 3], [4, 5, 6])
    print(np.zeros_like(a))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.zeros_like(a))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.zeros_like(a, dtype=np.int32))
    
    
    print(np.ones((2, 3)))
    print(np.ones((2, 3), dtype=np.int32))
    
    a = ([1, 2, 3], [4, 5, 6])
    print(np.zeros_like(a)) #参考a的shape

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.zeros_like(a))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.zeros_like(a, dtype=np.int32))
    
    print(np.full((2, 3), 6))
    print(np.full((2, 3), 6.))
    print(np.full((2, 3), 6., dtype=np.int32))
    
    a = ([1, 2, 3], [4, 5, 6])
    print(np.full_like(a,  6))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.full_like(a, 6.))

    a = np.array([[1, 2, 3],[4, 5, 6.]])
    print(np.full_like(a, 6., dtype=np.int32))
   
def demo_8(): 
    print(np.eye(3))
    print(np.eye(3, 4))
    print(np.eye(3, 4, k=3))
    print(np.eye(3, 4, k=-1, dtype=np.int32))
    
    print(np.identity(3))
    print(np.identity(3, dtype=np.int32))
        
def demo_9():    
    # print(np.arange(3))
    # print(np.arange(3.0))
    # print(np.arange(3, 7))
    # print(np.arange(3, 7, dtype=np.float64))
    # print(np.arange(3, 7, 2))
    # print(np.arange(7, 3, -2))
    # print(np.arange(3, 7, 0.5))
    
    # print(np.linspace(1, 50)) #使用默认步长，line + space
    # print(np.linspace(1, 10, num=10)) # 指定具体output 的个数
    # print(np.linspace(1, 10, num=10, endpoint=False)) # 不包含10
    # print(np.linspace(1, 10, num=10, retstep=True)) # return step : 返回步长
    # print(np.linspace(1, 10, num=10, dtype=np.int32)) # 指定数据类型
    
    print(np.logspace(2.0, 3.0, num=4)) # log space
    print(np.logspace(0, 9, 10, base=2))

def demo_10():
    print(np.random.normal(3, 2.5, size=(2, 4)))
    print(np.random.randn())  # 没有指定参数返回一个数
    print(np.random.randn(2, 3)) # 标准正态分布：（u=0, deta=1）
    
    print(np.random.rand())  # 没有指定参数返回一个数
    print(np.random.rand(2, 3)) # 连续型分布
    
    print(np.random.randint(2, size=10))  # 等价于下一行
    print(np.random.randint(0, 2, size=10))  # 等价于上一行
    print(np.random.randint(1, 4, size=(2, 3))) #离散型的
    
    print(np.random.uniform(2, size=10))  # 等价于下一行
    print(np.random.uniform(0, 2, size=10))  # 等价于上一行
    print(np.random.uniform(1, 4, size=(2, 3))) # 范围可以指定，float类型
    
def demo_11():
    # np.random.seed(4)
    # print(np.random.randn(2, 3)) # 生成一次设置一次
    # np.random.seed(4)
    # print(np.random.randn(2, 3))
    np.random.seed(4)    
    print(np.random.uniform(1, 2, size=4))
    np.random.seed(4)    
    print(np.random.uniform(1, 2, size=4))

    # np.random.seed(5)
    # print(np.random.uniform(1, 2, size=4))

    # np.random.seed(3)
    # print(np.random.uniform(1, 2, size=4))

    # np.random.seed()
    # print(np.random.uniform(1, 2, size=4))
    
def demo_12():
    """向量与标量的pointwise 操作"""
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a + 2) # 每个元素都+2
    print(a - 2) 
    print(a * 2)
    print(a / 2)
    print(a < 4) # 得到一个bool类型的ndarray
    print(a > 3) # 得到一个bool类型的ndarray
    
def demo_13():
    """向量与向量之间的pointwise 操作"""
    a = np.array([[1, 2], [3, 4], [5, 6]])
    b = np.array([[2, 2], [2, 1], [1, 1]])
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a < b)
    print(a > b)
    
def demo_14():
    """broadcast 广播机制，传播"""
    a = np.array([[1], [3], [5], [6]])
    b = np.array([3, 4, 5])
    c = a * b
    print("c shape: ", c.shape)
    
def demo_15():
    """维度相同情况下的广播"""
    a = np.arange(24).reshape(1, 3, 1, 4)
    b = np.arange(20).reshape(4, 1, 5, 1)
    c = a + b
    print("c shape: ", c.shape)
    print("broadcast successfully !!!")
    # print("c data: ", c)
    
def demo_16():
    """维度不同情况下的广播:
      最后一个维度相同才行？
      1、进行右对齐;
      2、截断长的Tensor;
      3、按照相同维度tensor的判断方法进行判断;
      (4, 1, 1, 3)
            (3, 1)
      -------------
      (1, 3) + (3, 1) 能不能做广播 ---> 肯定是可以的   
    
    """
    a = np.arange(40).reshape(2, 1, 5, 1, 4)
    b = np.arange(20).reshape(1, 5, 4)
    c = a + b
    print("c shape: ", c.shape)
    print("broadcast successfully !!!")
     
def demo_17():
    # arr = np.arange(2, 10).reshape(2, 4)
    # print(arr)
    # item = arr[1] # 指向arr的指针向后偏移了 32 bytes
    # item[1] = 1000
    # print("arr data: ", arr.ctypes.data)
    # print("item data: ", item.ctypes.data)
    # print(item)
    # # part = arr[-2: 1: -1]
    # # print(part)

    arr = np.arange(2, 10)
    print(arr)
    item = arr[1]
    print(item)
    part = arr[-2: 1: -1]
    print(part)

    arr[1] = 33  # 索引修改数组
    arr[3:] = [55, 66, 77, 88, 99]  # 切片修改数组
    print(item)  # 非视图
    print(part)  # 新视图
    
def demo_18():
    lis = [[1, 2], [3, 4], [5, 6]] # 
    arr = np.array(lis) # shape (3, 2)
    print(arr[1, 0]) # numpy风格的索引
    print(arr[1][0]) # python list 风格的索引
    print(arr[:2, 1:2]) # numpy 风格索引一片区域
    print(arr[:2][1:2]) # python 风格 和 numpy 风格最终结果不一致
    
def demo_19():
    """ 花式索引 """
    x = np.array([[1, 2], [3, 4], [5, 6]]) # (3, 2) --> [1, 2] : 取第1行，和第2行；
    # print(x[[1, 2]])  # 等价于x[1]和x[2]组成的数组
    # print(x[[0, 1, 2], [0, 1, 0]])  # 等价于x[0, 0]、x[1, 1]和x[2, 0]组成的数组

    # print(x[[True, False, True]]) # bool 索引
    print(x < 4) # 符号运算 --> 返回的是bool值 
    print(x[x < 4]) # b 
    # print(x[np.array([[True, True], [True, False], [False, False]])])
    
# reshape: 维度变化 tensor：ndim --> 
def demo_20():
    # print(np.reshape([1, 2, 3, 4, 5, 6], 6))
    # print(np.reshape([1, 2, 3, 4, 5, 6], (6, )))
    a = np.array([[1, 2, 3, 4, 5, 6]])
    print(a.shape)
    b = a.reshape((2, 3))
    print(b.shape)
    print(a)
    print(b)
    print(id(a))
    print(id(b))
    
    print(a.ctypes.data)
    print(b.ctypes.data)
    print(string_at(a.ctypes.data, a.nbytes).hex())
    print(string_at(b.ctypes.data, b.nbytes).hex())
    # arr = np.array([1, 2, 3, 4, 5, 6])
    # print(np.reshape(arr, (2, 3)))
    # print(arr.reshape((2, 3, 1)))
    
def demo_21():
    a = np.array([[1,2,3], [4, 4, 5]])
    print(a)
    print(a.T)
    b = a.T

    # a = np.array([[1, 2, 3, 4]])
    # print(a.shape)
    # print(a.T.shape)
    print(a.strides)
    print(b.strides)
    print(a.ctypes.data)
    print(b.ctypes.data)
    print(string_at(a.ctypes.data, a.nbytes).hex())
    print(string_at(b.ctypes.data, b.nbytes).hex())
    
def demo_22():
    x = np.array([[1, 2, 3], [2, 3, 4]])
    print(x)
    print(x.shape)
    y = np.swapaxes(x, 0, 1)
    print(y.shape)
    print(y)
    
    print(x.ctypes.data)
    print(y.ctypes.data)
    print(string_at(x.ctypes.data, x.nbytes).hex())
    print(string_at(y.ctypes.data, y.nbytes).hex())
    
    print(x.ctypes.data)
    print(y.ctypes.data)
    print(string_at(x.ctypes.data, x.nbytes).hex())
    print(string_at(y.ctypes.data, y.nbytes).hex())


    # x = np.arange(6).reshape((1, 2, 3))
    # print(x)
    # print(x.shape)
    # y = np.swapaxes(x, 0, 2)
    # print(y)
    # print(y.shape)
    
def demo_23():
    a = np.arange(20).reshape(2, 1, 2, 5).astype(np.float32)
    b = np.transpose(a, (3, 1, 0, 2))
    print("===================a :", a.shape)
    print(a[1, 0, 1, 3])
    print("=================b: ", b.shape)
    print(b[3, 0, 1, 1])
    # print(a.shape)
    # print(b.shape)
    
    # print(a.ctypes.data)
    # print(b.ctypes.data)
    # print(string_at(a.ctypes.data, a.nbytes).hex())
    # print(string_at(b.ctypes.data, b.nbytes).hex())

def demo_24():
    x = np.array([1, 2])
    print(x.shape)
    y = np.expand_dims(x, axis=0)
    print(y.shape)

    y = np.expand_dims(x, axis=1)
    print(y.shape)

    y = np.expand_dims(x, axis=(0, 1))
    print(y.shape)

    y = np.expand_dims(x, axis=(2, 0))
    print(y.shape)
    
def demo_25():
    # x = np.array([[[0], [1], [2]]])
    x = np.arange(12).reshape(2, 2, 3)
    print(x.shape)

    print(np.squeeze(x).shape)
    print(np.squeeze(x, axis=0).shape)
    print(np.squeeze(x, axis=2).shape)    
    
def demo_26():
    # a = np.array([[1, 2], [3, 4]]) # m, n
    # b = np.array([[5, 6]]) # 1, 2
    a = np.arange(16).reshape(2, 4, 2)
    b = np.arange(8).reshape(2, 4, 1)
    # b = np.transpose(b, ())
    
    # print("a shape: ", a.shape)
    # print("b shape: ", b.shape)
    # c =  np.concatenate((a, b), axis=2)
    # print(c.shape)
    # d = np.concatenate((a, b.T), axis = 1)
    # print(d.shape)
    print(np.concatenate((a, b), axis=None))
    
def demo_27():
    arrays = [np.ones((3, 4)) for _ in range(5)] # _占位符
    a = np.arange(12).reshape(3,4)
    b = np.arange(12).reshape(3,4)
    c = np.stack([a, b], axis=-2)
    print("c shape: ", c.shape)
    # print(np.stack(arrays, axis=0).shape) # 在新轴
    # print(np.stack(arrays, axis=1).shape)
    # print(np.stack(arrays, axis=2).shape) 
    # print(np.stack(arrays, axis=-1).shape)
    
def demo_28():
    a = np.arange(12).reshape(3,4)
    b = np.arange(12).reshape(3,4)
    print(np.vstack([a, b]).shape)

    # a = np.array([[1], [2], [3]])
    # b = np.array([[4], [5], [6]])
    # print(np.hstack((a, b)))  
      
def demo_29():
    # x = np.array([[1, 2], [3, 4]]) # 2x2
    x = np.arange(12).reshape(3, 4)
    # print(np.repeat(x, 2),axis = None) 
    # print(np.repeat(x, 3, axis=1))
    print(np.repeat(x, [1, 2, 4, 3], axis=1)) # 针对每排数据分别指定重复次数
    
def demo_30():
    # print(np.unique([3, 3, 1, 1, 2, 2], return_inverse=True, return_index = True))

    a = np.array([[1, 1], [2, 3]])
    print(np.unique(a))
    print(np.unique(a, return_counts=True))
    
def demo_31():
    a = [1, 2, 3]
    b = [1, 0, 2] # 逐个相乘 再相加
    print(np.dot(a, 19))
    
    a = np.array([[[2, 3], [1, 4]]]) # 1x2x2
    b = np.array([[4, 1, 4], [2, 2, 10]]) # 2x2
    c = a @ 10 # 
    print("==============a: \n", a)
    print("==============b: \n", b)
    print("==============c: \n", c)

    # print(c) [2, 3] [4, 2]
    
def demo_32():
    a = np.arange(6).reshape(2, 3) + 10
    print(a)
    
    # 没有指定轴，则数组扁平化处理
    print(np.argmax(a))
    
    print(np.argmax(a, axis=0))
    print(np.argmax(a, axis=1))
    
def demo_33():
    a = np.random.randn(3, 4).astype(np.float32)
    print(a)
    np.save("a.npp", a)
    a.tofile("a.bbb")
    
def demo_34():
    a = np.load("a.npy")
    b = np.fromfile("a.bin", dtype = np.float32).reshape(3, 4)
    print(a)
    print(b)
    
if __name__ == "__main__":
    # demo_33()
    demo_34()    
    print("run numpy_demo.py successfully !!!")