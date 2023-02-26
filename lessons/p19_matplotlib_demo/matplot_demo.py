# from matplotlib.font_manager import _rebuild
# _rebuild() #reload一下
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def demo_1():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    plt.plot(x, y, color='skyblue', linestyle='-.', linewidth=2, 
            marker='h', markerfacecolor='gold', markersize=8)
    # plt.show()

    plt.savefig("xxxxxx.jpg") 

def demo_2():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x = np.linspace(-3, 3, 50)
    y1 = 2*x + 1
    y2 = x**2
    y3 = np.sin(x)

    plt.figure()
    """
    对这四个数字的说明:
    0.1, 0.1表示坐标框左下角的位置, x和y坐标在画布的10%的位置
    0.8, 0.8表示坐标框的宽和高为画布的80%大小 """
    plt.axes([0.1, 0.1, 0.8, 0.8])
    plt.title('直线')  # 标题
    plt.plot(x, y1)

    # plt.axes([0.2, 0.6, 0.25, 0.25])
    plt.title('抛物线')
    plt.plot(x, y2)

    # plt.axes([0.6, 0.2, 0.25, 0.25])
    plt.plot(x, y3)
    plt.title('余弦曲线')
    plt.show()
    
def demo_5():
    import matplotlib.image as mpimg#读取图片
    import matplotlib.pyplot as plt #显示图片

    image = mpimg.imread('cat.png')
    plt.title('Read Image by Matplotlib')
    plt.axis('off')# 不显示坐标轴
    plt.imshow(image)
    plt.show()
    
#画布控制
def demo_6():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    # plt.figure(num=3, figsize=(8, 8), dpi=200, facecolor="blue", edgecolor="cornsilk", frameon=True)
    # plt.plot(x, y)
    # plt.show()

    plt.figure(num="画布二", figsize=(7, 3), dpi=100, facecolor="green", edgecolor="red", frameon=True)
    plt.plot(x, y)
    plt.show()

# 坐标轴控制
def demo_7():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    plt.figure()  # 创建画布1
    plt.plot(x, y)
    a, b = plt.xlim(xmin=-4, xmax=4)  # 限制横坐标显示最小值为 -2
    plt.ylim(-2, 2)  # 限制纵坐标显示最大值为 0.8
    c, d = plt.ylim()
    print(c, d)
    plt.show()

    # plt.figure()  # 创建画布2
    # plt.plot(x, y)
    # plt.xlim((-2, 4))  # 限制横坐标显示范围[-2, 4]
    # plt.ylim(ymin=-0.5, ymax=0.8)  # 限制纵坐标显示范围[-0.5, 0.8]
    # plt.show()
    
def demo_8():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y)
    # plt.xlim((-2, 4))
    # plt.ylim((-0.5, 0.8))

    # 指定横轴标签
    plt.xlabel("x", fontsize=14, color='skyblue')
    # 指定纵轴标签,并设置字体大小为14
    plt.ylabel("sin(x)", fontsize=14, color='red')
    plt.show()
    
def demo_9():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    plt.figure()  # 画布1
    plt.yticks(ticks=[-1, -0.8, -0.5, -0.1, 1], labels=["a", "b", "c", "d", "e"])
    plt.xticks(ticks=[-1, -0.8, -0.5, -0.1, 1], labels=["a", "b", "c", "d", "e"])
    plt.plot(x, y)
    # ticks的值作为刻度点的位置, labels的值作为刻度点的位置上的标签

    plt.figure()  # 画布2
    plt.plot(x, y)
    # ticks指定为空列表, 去掉刻度, 但轴还在
    plt.xticks(ticks=[])

    plt.figure()  # 画布3
    plt.plot(x, y)
    plt.axis("off")  # 把轴去掉,刻度一起没了

    plt.figure()  # 画布4
    plt.plot(x, y)
    new_xticks = np.linspace(-4, 4, 9)
    # 因为没有指定labels参数,所以ticks的值既作为刻度点的位置又作为刻度的标签
    plt.xticks(ticks=new_xticks)
    plt.yticks(ticks=[-1, -0.8, -0.5, -0.1, 1])
    plt.show()
   
def demo_10():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y)
    plt.yticks(ticks=[-1, -0.8, -0.5, -0.1, 1], labels=["a", "b", "c", "d", "e"])

    ax = plt.gca() # get coordinate a*
    ax.spines['right'].set_color('skyblue')
    ax.spines['top'].set_color('green')
    ax.spines['left'].set_color('red')
    ax.spines['bottom'].set_color('green')
    
    ax.xaxis.set_ticks_position('top') # 换轴
    # 把坐标体系的右边框作为y轴
    ax.yaxis.set_ticks_position('right')
    plt.show() 
    
def demo_11():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y)
    plt.yticks(ticks=[-1, -0.8, -0.5, -0.1, 1], labels=['a', 'b', 'c', 'd', 'e'])

    ax = plt.gca()
    ax.spines['right'].set_color('None')
    ax.spines['top'].set_color('None')
    ax.spines['left'].set_color('red')
    ax.spines['bottom'].set_color('green')

    # 选择坐标体系的左边框, 设置位置到数据为0的地方(即x轴原点)
    ax.spines['left'].set_position(('data', 0))
    # 选择坐标体系的底边框, 设置位置到数据为-0.1的地方(即y轴的'd'点)
    ax.spines['bottom'].set_position(('data', 0))
    plt.show()
    
def demo_12():
    x = np.linspace(-3, 3, 50)
    y1 = 2*x + 1
    y2 = np.sin(x)

    plt.figure()
    plt.plot(x, y1, color='blue', label='直线')
    plt.plot(x, y2, color='green', label='曲线')
    plt.legend(loc='lower right', fontsize=14, frameon=True, edgecolor='red', facecolor='yellow')

    plt.figure()
    plt.plot(x, y1, color='blue')
    plt.plot(x, y2, color='green')
    # 指定labels
    plt.legend(labels=['直线', '曲线'])

    plt.figure()
    # plot返回Line2D对象, 装在列表里, 所以解包
    line1, = plt.plot(x, y1, color='blue', label='直线')
    line2, = plt.plot(x, y2, color='green', label='曲线')
    print(line1)
    print(line2)
    # 指定第一条线创建图例, 且图例标签改为'线条1'
    plt.legend(handles=[line1, line2], labels=['线条1', "aaa" ])
    plt.show()
    
def demo_13():
    x = np.linspace(-3, 3, 50)
    y = np.sin(x)
    y1 = 2*x + 1

    plt.figure()
    plt.plot(x, y, label="直线")
    plt.plot(x, y1, color='green', label='曲线')
    

    plt.text(x=1.1, y=0.4, s="y=sinx", size=16, color="red")
    plt.text(x=1.5, y=3, s="y=2x + 1", size=16, color="blue")
    plt.legend(loc='lower right', fontsize=14, frameon=True, edgecolor='red', facecolor='yellow')
    
    plt.show()
    
def demo_14():
    data = np.array([[0, 50, 200], [200, 100, 0], [0, 150, 200]])
    plt.imshow(data)
    # plt.imshow(data, cmap="Greys")
    # plt.imshow(data, cmap="Greys", alpha=0.3)
    plt.show()

def demo_15():
    x = np.linspace(-3, 3, 50)
    y1 = 2*x + 1
    y2 = x**2
    y3 = np.sin(x)

    plt.figure()
    """
    对这四个数字的说明:
    0.1, 0.1表示坐标框左下角的位置, x和y坐标在画布的10%的位置
    0.8, 0.8表示坐标框的宽和高为画布的80%大小 """
    plt.axes([0.1, 0.1, 0.8, 0.8])
    plt.title('直线')  # 标题
    plt.plot(x, y1)

    # plt.axes([0.2, 0.6, 0.25, 0.25])
    plt.title('抛物线')
    plt.plot(x, y2)

    # plt.axes([0.6, 0.2, 0.25, 0.25])
    plt.plot(x, y3)
    plt.title('余弦曲线')
    plt.show()
    
if __name__ == "__main__":
    demo_15()
    print("run matplot_demo.py successfully !!!")