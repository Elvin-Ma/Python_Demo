from typing import Iterator

def demo_1():
    file = open(r'./t01.txt', mode='a')
    file.write('hello world')
    file.write('\nhello China')
    file.write('\nhello Baby')
    file.close()


    file = open(r'./t01.txt')
    # print(isinstance(file, Iterator))
    print(list(file))
    for i in file:
        print(i)
        
def demo_2():
    with open(r"./t01.txt") as file:
        print(file.read(5))
        print(file.read(2))
        print(file.read())
        
def demo_3():
    import time

    file = open(r"./t01.txt", mode='a')
    file.write('\n123456789')
    time.sleep(5)  # 文件需要等到关闭文件时才会把数据从缓冲区写入文件
    file.close()  # 关闭文件，自动刷新缓冲区，数据才写入文件

    file = open(r"./t01.txt", mode='a')
    file.write('\n123456789')
    file.flush()  # 刷新缓冲区，数据立刻写入文件
    time.sleep(5)
    file.close()

def demo_4():
    with open(r"./t02.txt", mode='r') as file:
        if file.writable():
            file.write("hello world")
        if file.readable():
            print(file.read())
    
def demo_5():
    with open(r"./t04.txt") as file:
        if file.writable():
            file.write("hello world")
            file.write("hello shenlan")
            file.write("hello jiaoda")
        if file.readable():
            print(file.seek(2))
            print(file.tell())
            print(file.read())
            file.tell()
            
def demo_6():
    tup = ("a\n", 'bc\n', "def")
    with open(r"./t01.txt", mode="w") as file:
        file.writelines(tup)
           
def demo_7():
    import os
    print(os.path.split('./dir3/dir2/dir1/a.txt'))
    new_name = os.path.join("./dir3/dir2", "dir1/a.txt")
    print(new_name)
#    print(os.getcwd())
#    print(os.listdir(os.getcwd()))
#    os.mkdir(os.getcwd() + "/MyDir")
#    os.makedirs('./dir1/dir2/dir3')
#    os.remove('./dir1/dir2/a.txt')
#    os.removedirs('./dir1/dir2/dir3')
#    os.rename(os.getcwd() + "/dir1", os.getcwd() + "/dir4")
#    os.renames('./dir1/dir2/dir3/a.txt', './dir3/dir2/dir1/b.txt')
#    print(os.path.abspath("./dir3"))
#    print(os.path.abspath("./dir3/a.txt"))
#    print(os.path.basename('./dir3/dir2/dir1/a.txt'))
#    print(os.path.dirname('./dir3/dir2/dir1/a.txt'))
    #  print(os.path.splitext('./dir3/dir2/dir1/a.txt'))
    
def demo_8():
    import json

    info = {'name': 'Tom', 'age': 18, 1: 'one'}
    # print(type(info), info)

    # with open("info.json", mode="w") as f:
    #     info_str = json.dumps(info)  # 序列化
    #     print(type(info_str), info_str)
    #     f.write(info_str)

    with open("info.json") as f:
        content = f.read()
        print(type(content), content)
        res = json.loads(content)  # 反序列化
        print(type(res), res)
    
def demo_9():
    import json

    info = {'name': 'Tom', 'age': 18, 1: 'one'}

    with open("info.json", mode="w") as f:
        json.dump(info, f)

    with open("info.json") as f:
        res = json.load(f)
        print(type(res), res)

def demo_10():
    import json
    
    with open('./TestFile.json') as file:
        content = json.load(file)

    obj_list = content["outputs"]["object"]
    for item in obj_list:
        print(item["name"])
        print(item["bndbox"])  

def demo_11():
    import pickle

    info = {'name': 'Tom', 'age': 18, 1: 'one'}
    print(type(info), info)

    with open("info.pickle", mode="wb") as f:
        info_byte = pickle.dumps(info)
        print(type(info_byte), info_byte)
        f.write(info_byte)

    with open("info.pickle", mode="rb") as f:
        content = f.read()
        print(type(content), content)
        res = pickle.loads(content)
        print(type(res), res)   
 
def demo_12():
    import pickle
    info = {'name': 'Tom', 'age': 18, 1: 'one'}

    with open("info.pickle", mode="wb") as f:
        pickle.dump(info, f)

    with open("info.pickle", mode="rb") as f:
        res = pickle.load(f)
        print(type(res), res)     
        
def demo_13():
    import xml.etree.ElementTree as ET

    tree = ET.parse(r"./TestFile.xml")  # 将XML文档解析为元素树
    root = tree.getroot()  # 返回该树的根元素, 即 <doc>
    obj = root.find("outputs").find("object")  # 找到对应的子元素

    for item in obj:
        name = item.find("name")
        print(name.text)
        bndbox = item.find("bndbox")
        for item in bndbox:
            print(item.tag)  # tag：标签（尖括号之间的内容）
            print(item.text)  # text：文本（标签之间的内容）
            
def demo_14():
    import csv

    # person = [('xxx', 18, 193), ('yyy', 18, 182), ('zzz', 19, 185)]
    # # 表头
    # header = ['name', 'age', 'height']

    # with open('person.csv', 'w',  newline='', encoding='utf-8') as file_obj:
    #     # 1:创建writer对象
    #     writer = csv.writer(file_obj)
    #     # 2:写表头
    #     writer.writerow(header)
    #     # 3:遍历列表，将每一行的数据写入csv
    #     #writer.writerows(person)
    #     for p in person:
    #         writer.writerow(p) 
				
    # with open('person.csv','r') as f:
    #     reader=csv.reader(f)
    #     for data in reader:   
    #         print(data)
                
if __name__ == "__main__":
    # demo_1()
    # demo_2()
    # demo_3()
    # demo_4()
    # demo_5()
    # demo_6()
    # demo_7()
    # demo_8()
    # demo_9()
    # demo_10()
    # demo_11()
    # demo_12()
    # demo_13()
    demo_14()
    print("run file_demo.py successfully !!!")