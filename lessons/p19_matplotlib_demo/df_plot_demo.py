import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# help(pd.DataFrame.plot) #查看帮助文档

#条状图
def demo_1():
    df = pd.read_csv('weather.csv')
    print(df)
    df.plot(x='month', y=['Tmax', 'Tmin']) #折线图
    df.plot(x='month', y='Rain', kind='bar') #条形图
    # df.plot(x='month', y='Rain', kind='barh') #条形图
    # df.plot.bar(x='month', y='Rain') #条形图
    # ax = df.plot.barh(x='lab', y='val')
    # df.plot(kind='bar', x = 'month', y=['Tmax', 'Tmin']) #多变量条形图
    df.plot(kind='scatter', x = 'month', y = 'Sun') #散点图
    df.plot(kind='pie', y='Sun') #饼状图
    
    # #饼状图
    # df.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # df.plot(kind='pie', y = 'Sun', legend=False)
    
    df.plot(y='Rain', kind='hist', bins=[0,25,50,75,100,125,150,175, 200])   #直方图
    plt.show()

    
if __name__ == "__main__":
    demo_1()
    print("run df_plot_demo.py successfully !!!")