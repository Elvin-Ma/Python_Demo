import pandas as pd
import numpy as np

def demo_1():
    d = {'a': 1, 'b': 2, 'c': 3}
    ser = pd.Series(data=d, index=['a', 'y', 'z'])
    print(ser)
    
def demo_2():
    d = np.array([1, 2, 3, 4, 5])
    ser = pd.Series(data=d, index=('a', 'e', 'c', 'd', 'e'))
    print(ser)
    print(ser[1])
    print(ser[1:3])
    print(ser[:-2:2])
    print(ser[[2, 1, 3]])
    
def demo_3():
    d = np.array([1, 2, 3, 4, 5])
    ser = pd.Series(data=d, index=('a', 'e', 'c', 'd', 'e'))
    # print(ser)
    # print(ser['c'])
    # print(ser['e'])

    """ 索引标签切片时, 右边不是开区间哦 """
    print(ser['a':'d'])  # ser['e':'d']报错，因为'e'不唯一
    print(ser[:'c':2])
    print(ser[['c', 'e', 'd']])
    
def demo_4():
    ser = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
    print(ser)
    ser.index = ['aa', 'bb', 'cc', 'dd']  # 修改原数据
    print(ser)
    
def demo_5():
    ser = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])
    ser['a'] = 8
    print(ser)
    ser['b':'d'] = 9
    print(ser)
    ser['b':'d'] = [1, 1, 1]
    print(ser)
    
def demo_6():
    ser = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])
    print(ser)

    new_ser1 = ser.reindex(index=['a', 'c', 'e'], fill_value=-1)
    print(new_ser1)

    new_ser2 = ser.reindex(index=['g', 'c', 'b', 'a', 'f'], fill_value=np.e)
    print(new_ser2)
    
def demo_7():
    d = [1, 2, 3, 4]
    ser = pd.Series(data=d, index=['a', 'b', 'c', 'd'], name="Test-Series")
    print(ser.dtype)
    print(ser.empty)
    print(ser.name)
    print(ser.size)
    print(ser.values)
    print(ser.index)
    
def demo_8():
    ser = pd.Series([1, 2, 5, np.nan])
    print(ser)
    print(ser.isnull())
    print(ser.notnull())
    
def demo_9():
    ser1 = pd.Series([15, 20], index=[1, 2])
    print(ser1 + 1)
    print(ser1 - 1)
    print(ser1 * 2)
    print(ser1 / 2)

    ser2 = pd.Series([1, 2, 3], index=[1, 2, 3])
    print(ser1 + ser2)
    print(ser1 - ser2)
    print(ser1 * ser2)
    print(ser1 / ser2)
    
def demo_10():
    # d = [[1, 2, 3], [4, 5 ,6]]
    # d = np.array([[1, 2, 3], [4, 5 ,6]])
    # d = {'name': ['Tom', 'Bob', 'Linda'], 'age': [17, 18, 26]}
    # df = pd.DataFrame(data=d)
    # print(df)
    # d = [{'name': 'Tom', 'age': 17}, {'name': 'Bob', 'age': 18}, {'name': 'Linda', 'ages': 26}]
    # df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3'])
    # print(df)
    d = [pd.Series(['Tom', 'Bob', 'Linda'], index=['p1', 'p2', 'p3']), pd.Series([17, 18, 26], index=['p1', 'p2', 'p8'])]
    df = pd.DataFrame(data=d)
    print(df["p1"])
    print(df)
    
def demo_11():
    d = {'name': ['Tom', 'Bob', 'Linda'], 'age': [17, 18, 26], 'height': [172, 176, 188]}
    df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3']) # dict d 
    print(df)

    # 索引获取列数据
    # print(type(df['age']))
    # print(df[['age', 'name']]) # 和我们numpy的用法差不多
    
    # print(df['name': 'height'])
    
    # print(df[0: 1])  # 下标切片左闭右开
    # print(df['p1': 'p2'])  # 标签切片两边都是闭区间

    # print(df.loc['p1']) # 索引不出来
    # print(type(df.loc['p2', 'age'])) # 同时提取行和列 --> 什么类型???
    # print(df.loc['p2', ['age', 'name']]) # 一行，两列
    # print(df.loc[['p3', 'p2'], ['age', 'name']]) # 在行和列上同时索引 --> dataFrame
    
    print(df.iloc[0]) # 提取的是第一行
    print("=====================")
    print(df.iloc[1, 1]) # 提起了第一行、第一列的那个值
    print("=====================")
    print(df.iloc[1, [1, 0]]) # 第一行、1/0列的series
    print("=====================")
    print(df.iloc[[2, 1], [1, 0]])   # dataframe
    
def demo_12():
    d = {'name': ['Tom', 'Bob', 'Linda'], 'age': [17, 18, 26], 'height': [172, 176, 188]}
    df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3'])
    print(df)

    """ 修改行索引 """
    df.index = ['n1', 'n2', 'n3']

    """ 修改列索引 """
    df.columns = ['names', 'ages', 'heights']

    print(df)
    
def demo_13():
    d = {'name': ['Tom', 'Bob', 'Linda'], 'age': [17, 18, 26], 'height': [172, 176, 188]}
    df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3'])
    print(df)
    
    # 已有就更改：没有就新增
    df['height'] = pd.Series([1.72, 1.88, 1.76], index=df.index) #更改一列数据
    print("=====================")
    print(df)
    
    df[['name', 'age']] = pd.DataFrame({'name': ['Bob', 'Tom', 'Jack'], 'age': [19, 22, 27]}, ['p1', 'p2', 'p3'])
    print("=====================")
    print(df)
    
    # 已有就更改：没有就新增
    df['weight'] = pd.Series([65, 75, 60], index=df.index)
    print("=====================")
    print(df)
    
    # 新增多列
    df[['BMI', 'adres']] = pd.DataFrame({'BMI': df['weight'] / df['height']**2, 'adres': ['威宁路', '长宁路', '大马路']})
    print("=====================0 ")
    print(df)
    
    #更改
    df.iloc[1] = pd.Series(['Linda', 23, 1.78, 65, 22, '徐汇路'])
    print("********************* 1")
    print(df)
    
    df[::2] = pd.DataFrame([['Jack', 27, 1.76, 60, 19, '大马路'], ['Bob', 19, 1.72, 65, 21, '威宁路']])
    print("******************2 ")
    print(df)
    
    data = [['Jack', 27, 1.76, 60, 19, '大马路'], ['Bob', 19, 1.72, 65, 21, '威宁路']]
    df.loc['p1':'p3':2] = pd.DataFrame(data, index=['p1', 'p3'], columns=df.columns)
    print("******************3 ")
    print(df)
    
    df.loc['p4'] = pd.Series(['Tony', 23, 1.78, 65, 22, '徐汇路'], index=df.columns)
    print("******************4: ")
    print(df) 
    
def demo_14():
    data = np.arange(12).reshape(3, 4)
    df = pd.DataFrame(data, index=['n1', 'n2', 'n3'], columns=['a', 'b', 'c', 'd'])
    print(df)
    
    # df2 = df.reindex(labels=['a'], axis=1, fill_value= 1000)
    # print("====================")
    
    df2 = df.reindex(columns=['c', 'a'])
    print("===============")
    print(df2)
    df2 = df.reindex(index=['n2', 'n1'])
    print("===============")
    print(df2)
    
def demo_15():
    data = np.arange(12).reshape(3, 4)
    df = pd.DataFrame(data, index=['n1', 'n2', 'n3'], columns=['a', 'b', 'c', 'd'])
    # print(df.to_dict())
    # label_attr = ["T", "dtypes", "shape", "size", "index"]
    for i, item in enumerate(dir(df)):
        # if item in label_attr:
            print("================== : {}".format(i))
            print(item)
    
def dmeo_16():
    d = [['Tom', 17], ['Bob', 18], ['Linda', 26]]
    df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3'], columns=['name', 'age'])
    print(df)
    print(df.T)
    print(df.dtypes)
    print(df.empty)
    print(df.shape)
    print(df.size)
    print(df.index)
    print(df.columns)
    print(df.axes)
    print(type(df.values))
    
def demo_17():
    d = {'name': ['Tom', 'Bob', 'Linda'], 'age': [17, 18, 26]}
    df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3'])
    print(df)
    df.insert(1, 'age', [65, 75, 60], allow_duplicates=True)
    print("====================")
    print(df)   

def demo_18():
    d = {'name': ['Tom', 'Bob', 'Linda'], 'age': [17, 18, 26], 'height': [172, 176, 188]}
    df = pd.DataFrame(data=d, index=['p1', 'p2', 'p3'])
    print(df)
    
    # del df['name']
    print("=======================")
    res = df.pop('height') # df 本身也发生了变化
    print(df)
    print("=======================")
    print(res)
    
def demo_19():
    df = pd.DataFrame([[1, 2], [3, 4]], index=['p1', 'p2'], columns=list('AB'))
    print(df)

    print("=======================")
    df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
    # print(df2)    
    df2['c'] = pd.Series([9, 0])
    print(df2)
    
    print(pd.concat([df, df2]))
    print(pd.concat([df, df2], join='inner'))
    print(pd.concat([df, df2], axis=1))
    df2.index = [0, 'p1']  # 修改索引
    print(df2)
    print(pd.concat([df, df2], axis=1, join='inner'))
    
    
    # print("=======================")
    # print(df.append(df2))
    # print("=======================")
    # print(df.append(df2, ignore_index=True))
    
def demo_20():
    d1 = {'name': ['Tom', 'Bob', 'Jack'], 'age': [18, 17, 19], 'weight': [65, 66, 67]}
    df1 = pd.DataFrame(data=d1)

    d2 = {'name': ['Tom', 'Jack'], 'height': [168, 187], 'weight': [65, 68]}
    df2 = pd.DataFrame(data=d2)

    print("======================= 0 ")
    print(df1)
    print("======================= 1 ")    
    print(df2)
    print("======================= 2 ")    
    
    print(pd.merge(df1, df2, how='outer'))
    # print(pd.merge(df1, df2, how='inner', on='name'))
    # print("======================= 3 ")    
    # print(pd.merge(df1, df2, how='left', on='name'))
    # print("======================= 4 ")    
    # print(pd.merge(df1, df2, how='right', on='name'))
    # print("======================= 5 ")    
    # print(pd.merge(df1, df2, how='outer', on='name'))
    
def demo_21():
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], index=['n1', 'n2', 'n3'], columns=['a','b'])
    print(df)

    # print(df.drop(labels='n2', axis=0)) # 有 label + axis 确定
    # print(df.drop(index='n2'))
    
    # print(df.drop(labels='b', axis=1)) #删除列
    # print(df.drop(columns='b'))
    
    # print(df.drop(labels=['n2', 'n1'], axis=0)) #多行
    # print(df.drop(index=['n2', 'n1']))

    # print(df.drop(labels=['a', 'b'], axis=1)) #多列
    # print(df.drop(columns=['a', 'b']))
    
    df.drop(index='n1', inplace=True) # inplace : 原地
    print(df) # do operation  inplace
    
def demo_22():
    d = {'name': ['Tom', np.nan, 'Bob'], 'age': [np.nan, np.nan, 19], 'height': [177, 182, 179]}
    df = pd.DataFrame(data=d)
    print("===========================0")
    print(df)
    
    # print("===========================1")
    # print(df.dropna())
    
    # print("===========================2")
    # print(df.dropna(axis=1))
    
    # df.loc[2, 'age'] = np.nan
    # print("===========================3")
    # print(df)
    # print("===========================4")
    # print(df.dropna(axis=1, how='all'))
    
    # print("===========================5")
    # print(df.dropna(axis=1, thresh=2))
    
    # print("===========================6")
    # print(df.dropna(subset=['name', 'height']))
    
    print("===========================7")
    print(df.dropna(axis=1, subset=[1, 2], inplace=True))
    
    # df.dropna(axis=1, inplace=True)
    # print(df) 
    
def demo_23():
    df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, np.nan],
                    [np.nan, 3, np.nan, 4]],
                    columns=list("ABCD"))
    print("===========================0")
    print(df)
    
    # print("===========================0")
    # print(df.fillna(0))
    
    # dic = {'A': 6, 'B': 7}
    # print(df.fillna(dic)) 
    
    # df2 = pd.DataFrame(np.zeros((4, 4)), columns=list("ABCE"))
    # print("===========================1")   
    # print(df2)
    # print("===========================2")
    # print(df.fillna(df2))  
    
    # print("===========================1")
    # print(df.fillna(method='ffill', axis=1))
    # print("===========================2")
    # print(df.fillna(method='bfill', axis = 1))
    
    print("===========================1")
    print(df.fillna({'A': 6, 'C': 7}, limit=2))
    
def demo_24():
    df = pd.DataFrame(data={'name': ['Tom', 'Bob', np.nan], 'age': [18, 19, 17], 'height': [167, 177, 178]}, index=['n1', 'n2', 'n3'])
    print("===========================0")
    print(df)
    
    print("===========================1")
    df.info()
    
    print("===========================2")
    df.info(verbose=False)
    print("===========================3")    
    df.info(show_counts=False)
    
def demo_25():
    df = pd.DataFrame(data={'name': ['Tom', 'Bob', 'Bob'], 'age': [18, 19, 17], 'height': [167, 177, 178]}, index=['n1', 'n2', 'n3'])
    print("===========================0")
    print(df)
    print("===========================1")    
    print(df.describe())
    print("===========================2")    
    print(df.describe(include='all'))
    print("===========================3")    
    print(df.describe(exclude='object'))
    
def demo_26():
    df = pd.DataFrame(data={'name': ['Tom', 'Bob', 'Jack', 'Linda'], 'age': [18, 19, 17, 21], 'height': [167, 177, 178, 188]}, index=['n1', 'n2', 'n3', 'n4'])
    print(df)
    print(df.sample(frac=0.5, axis=1))
    print(df.sample(n=2, random_state=3))
    
def demo_27():
    d = {'A': [1, 0, 0, 1], 'B':[0, 2, 5, 0],
        'C': [4, 0, 4, 4], 'D':[1, 0, 0, 1]}
    
    df = pd.DataFrame(data=d)
    print("===========================0")    
    print(df)
    print("===========================1")     
    # print(df.drop_duplicates())
    print(df.drop_duplicates(subset=['A', 'D'], keep='first'))
    
def demo_28():
    d = {
    'company': ['A', 'B', 'A', 'C', 'C', 'B', 'C', 'A'],
    'salary': [8, 15, 10, 15, 15, 28, 30, 15],
    'age': [26, 29, 26, 30, 50, 30, 30, 35]
    }
    
    df = pd.DataFrame(data=d)
    print("===========================0")     
    print(df)
    
    res = df.groupby(['company'])
    # print("===========================1")    
    # a = list(res) 
    # print(len(a))
    print(res.groups)
    
    # print(res.get_group('A'))
    # print(res.get_group('B'))
    # print(res.get_group('C'))
    
    # print(res.agg('max'))
    # print(res.agg(np.max))  # 同上
    # print(res.agg('min'))
    # print(res.agg('sum'))
    # print(res.agg('mean'))
    # print(res.agg('median'))  # 中位数
    # print(res.agg('std'))
    # print(res.agg('var'))
    # print(res.agg('count'))
    
    avg_salary = res['salary'].transform('mean')
    print(avg_salary)
    
def demo_29():    
    d = np.arange(9).reshape((3, 3))
    df1 = pd.DataFrame(data=d, columns=list('abc'), index=['n1', 'n2', 'n3'])
    print("===========================0")    

    print(df1)
    
    d = np.arange(16).reshape((4, 4))
    df2 = pd.DataFrame(data=d, columns=list('dacf'),index=['n1', 'n2', 'n3', 'n4'])
    print("===========================1")    

    print(df2)
    print("===========================2")    
    
    print(df1 + df2)
    print("===========================3")    
    print(df1 - df2)
    print("===========================4")    
    print(df1 * df2)
    print("===========================5")    
    print(df1 / df2)
    
def demo_30():
    d = {
    '名字': ['张三', '李四', '王五', '赵六', '孙七'],
    '年龄': [18, 19, 20, 22, 17],
    '身高': [188, 178, 189, 175, 177]
    }
    df = pd.DataFrame(data=d)
    print(df)
    
    df.to_csv('./test04.csv')
    df.to_excel('./test04_ex.xlsx')
    
    
def demo_31():
    a = pd.read_csv("test04.csv")
    # print(a)
    df = pd.read_excel('test04_ex.xlsx', header=2)
    print(df)   
    
if __name__ == "__main__":
    demo_31()
    print("run pandas_demo.py successfully !!!")

    