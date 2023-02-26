import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#折线图
def demo_1():
    '''
    折线图是一个由点和线组成的统计图表,常用来表示数值随连续时间间隔或有序类别的变化。
    在折线图中,x 轴通常用作连续时间间隔或有序类别(比如阶段1,阶段2,阶段3)。
    y 轴用于量化的数据,如果为负值则绘制于 y 轴下方。连线用于连接两个相邻的数据点。

    折线图用于分析事物随时间或有序类别而变化的趋势。
    如果有多组数据,则用于分析多组数据随时间变化或有序类别的相互作用和影响。
    折线的方向表示正/负变化。折线的斜率表示变化的程度。
    '''
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
    plt.plot(ages_x, dev_y, label="全部开发者", color="#FF0000", marker=".", linestyle="-")

    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
    plt.plot(ages_x, py_dev_y, label="Python开发者", color="#00FF00", marker=".", linestyle="--")

    plt.xlabel("年龄")
    plt.ylabel("年薪")
    plt.title("年龄和薪水的关系")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()
    
#条形图
def demo_2():
    '''
    条形图(bar chart)是用宽度相同的条形的高度或长短来表示数据多少的图形,是一种用于对不同类别进行数值比较的统计图表。
    条形图可以横置或纵置,纵置时也称为柱形图(column chart)。条形图被误用的一个典型代表就是篡改 y 轴,对读者视觉造成误导。在使用条形图时,务必要是原点位于 0。
    此外,注意对条形图进行排序。依据可视化的目的、以及想突出的重点信息,确定合理的排序标准,避免条形图看起来杂乱无章。
    '''
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    x_indexes = np.arange(len(ages_x))
    width = 0.33

    dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
    py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

    plt.bar(x_indexes, dev_y, width=width, label="全部开发者")
    plt.bar(x_indexes + width, py_dev_y, width=width, label="Python开发者")

    plt.xlabel("年龄")
    plt.ylabel("年薪")
    plt.title("年龄和薪水的关系")

    plt.legend()

    plt.xticks(ticks = x_indexes, labels = ages_x)

    plt.show()
    
#堆叠条形图
def demo_3():
    '''
    堆叠条形图是一种用来分解整体、比较各部分的图。与条形图类似,堆叠条形图常被用于比较不同类别的数值。
    而且,它的每一类数值内部,又被划分为多个子类别,这些子类别一般用不同的颜色来表示。

    如果说条形图可以帮助我们观察总量,那么堆叠条形图则可以同时反映总量与结构,即总量是多少？
    它又是由哪些部分构成的？进而,我们还可以探究哪一部分比例最大,以及每一部分的变动情况等等。
    '''
    x = ['A', 'B', 'C', 'D']
    y1 = np.array([10, 20, 10, 30])
    y2 = np.array([20, 25, 15, 25])
    y3 = np.array([12, 15, 19, 6])
    y4 = np.array([10, 29, 13, 19])
    
    plt.bar(x, y1, label='Round1', width=0.67)
    plt.bar(x, y2, bottom=y1, label='Round2', width=0.67)
    plt.bar(x, y3, bottom=y1+y2, label='Round3', width=0.67)
    plt.bar(x, y4, bottom=y1+y2+y3, label='Round4', width=0.67)

    plt.xlabel("Teams")
    plt.ylabel("Score")
    plt.legend()
    plt.title("Scores by Teams in 4 Rounds")

    plt.tight_layout()
    plt.show()

#直方图
def demo_4():
    '''
    直方图,又称质量分布图,用于表示数据的分布情况,是一种常见的统计图表。一般用横轴表示数据区间,纵轴表示分布情况,柱子越高,
    则落在该区间的数量越大。直方图和条形图的外观相似。区别主要有以下几点：

    条形图用条形的长度(横置时)或高度(纵置时)表示各类别频数的多少,其宽度(表示类别)则是固定的；
    直方图是用面积表示各组频数的多少,矩形的高度表示每一组的频数或频率,宽度则表示各组的组距,因此其高度与宽度均有意义。
    由于分组数据具有连续性,直方图的各矩形通常是连续排列,而条形图则是分开排列。
    条形图主要用于展示分类数据的大小,而直方图则主要用于展示数值型数据的分布。
    '''
    ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
    bins = [20, 30, 40, 50, 60]
    plt.hist(ages, bins=bins, edgecolor='black')

    plt.title('人员的年龄分布')
    plt.xlabel('年龄')
    plt.ylabel('人数')

    plt.tight_layout()

    plt.show()

# 散点图
def demo_5():
    '''
    散点图,又名点图、散布图、X-Y图,英文 Scatter plot 或 Scatter gram。散点图将所有的数据以点的形式展现在平面直角坐标系上。
    它至少需要两个不同变量,一个沿 x 轴绘制,另一个沿 y 轴绘制。每个点在 x、y 轴上都有一个确定的位置。
    众多的散点叠加后,有助于展示数据集的"整体景观",从而帮助我们分析两个变量之间的相关性,或找出趋势和规律。

    散点图常被用于分析变量之间的相关性。如果两个变量的散点看上去都在一条直线附近波动,则称变量之间是线性相关的；
    如果所有点看上去都在某条曲线(非直线)附近波动,则称此相关为非线性相关的；
    如果所有点在图中没有显示任何关系,则称变量间是不相关的。
    '''
    plt.style.use('fivethirtyeight')

    price_orange = np.array([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])
    sales_per_day_orange = np.array([34, 62, 49, 22, 13, 19])
    profit_margin_orange = np.array([20, 35, 40, 20, 27.5, 15])

    price_cereal = np.array([1.50, 2.50, 1.15, 1.95])
    sales_per_day_cereal = np.array([67, 34, 36, 12])
    profit_margin_cereal = np.array([20, 42.5, 33.3, 18])

    plt.scatter(price_orange, sales_per_day_orange, s=profit_margin_orange*10, c=profit_margin_orange, 
                cmap='jet', edgecolors='black', linewidth=1, alpha=0.7, label='orange')


    plt.scatter(price_cereal, sales_per_day_cereal, s=profit_margin_cereal*10, c=profit_margin_cereal, 
                cmap='jet', edgecolors='black', linewidth=1, alpha=0.7, marker='d', label='cereal')

    cbar = plt.colorbar()
    cbar.set_label('利润率')

    plt.title('价格和销量的关系')
    plt.xlabel('价格')
    plt.ylabel('销量')

    plt.legend()
    plt.tight_layout()
    plt.show()

#饼状图    
def demo_6():
    '''
    饼图,或称饼状图,是一个将圆形划分为几个扇形的统计图表。在饼图中,每个扇形的弧长大小,表示该种类占总体的比例,
    这些扇形合在一起刚好是一个完整的圆形。饼图最显著的功能在于表现"占比"。
    
    习惯上,人们也用饼图来比较扇形的大小,从而获得对数据的认知。
    但是,由于人类对"角度"的感知力并不如"长度",在需要准确的表达数值(尤其是当数值接近、或数值很多)时,
    饼图常常不能胜任,建议用柱状图代替。

    使用时,须确认各个扇形的数据加起来等于 100%；避免扇区超过 5 个,尽量让图表简洁明了。
    '''
    languages = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
    popularity = [59219, 55466, 47544, 36443, 35917] # data

    plt.pie(popularity, labels=languages, autopct='%1.1f%%', 
            counterclock=False, startangle=90,explode=[0,0,0.1,0,0])

    plt.title('top5 编程语言占比')
    plt.tight_layout()
    plt.show()

#热力图
def demo_7():
    '''
    热力图是一种通过对色块着色来显示数据的统计图表。绘图时，需指定颜色映射的规则。
    例如，较大的值由较深的颜色表示，较小的值由较浅的颜色表示；较大的值由偏暖的颜色表示，较小的值由较冷的颜色表示，等等。

    从数据结构来划分，热力图一般分为两种:
    第一，表格型热力图，也称色块图。它需要 2 个分类字段和 1 个数值字段，分类字段确定 x、y 轴，
          将图表划分为规整的矩形块。 数值字段决定了矩形块的颜色。
    第二，非表格型热力图，或曰平滑的热力图，它需要 3 个数值字段，
         可绘制在平行坐标系中(2个数值字段分别确定x、y轴, 1个数值字段确定着色)。

    热力图适合用于查看总体的情况、发现异常值、显示多个变量之间的差异，以及检测它们之间是否存在任何相关性。
    '''
    vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
    farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
            "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

    harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                        [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                        [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                        [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                        [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                        [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                        [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

    plt.xticks(np.arange(len(farmers)), labels=farmers, 
                        rotation=45, rotation_mode="anchor", ha="right")
    plt.yticks(np.arange(len(vegetables)), labels=vegetables)    
    plt.title("Harvest of local farmers (in tons/year)")

    for i in range(len(vegetables)):
        for j in range(len(farmers)):
            text = plt.text(j, i, harvest[i, j], ha="center", va="center", color="w")

    plt.imshow(harvest)
    plt.colorbar()
    plt.tight_layout()
    plt.show()

#多子图绘制
def demo_8():
    '''
    前面讲述的图表绘制方法一次只会绘制一张图表，但是有些情况下，我们希望把一组图放在一起进行比较，
    有没有什么好的方法呢？
    matplotlib 中提供的 subplots() 可以很好的解决这个问题。
    通过调用 subplots() 可以将整个绘图区域分成 m * n 个子区域，每个子区域都可以绘制一个子图。
    '''
    x1 = np.linspace(0, 2*np.pi, 400)
    y1 = np.sin(x1)
    y2 = np.cos(x1)

    x2 = np.linspace(0, 2*np.pi, 40)
    y3 = np.sin(x2)
    y4 = np.cos(x2)

    fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

    ax[0,0].plot(x1, y1)
    ax[0,0].set_title('plot sin')

    ax[0,1].plot(x1, y2)
    ax[0,1].set_title('plot cos')

    ax[1,0].scatter(x2, y3)
    ax[1,0].set_title('plot scatter sin')

    ax[1,1].scatter(x2, y4)
    ax[1,1].set_title('plot scatter cos')

    plt.show()

if __name__ == "__main__":
    demo_8()
    print("run plot_demo.py successfully !!!")