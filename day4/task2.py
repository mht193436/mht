import pandas as pd
import matplotlib.pyplot as plt

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载 2015 年数据
df_2015 = pd.read_csv('2015年国内主要城市年度数据.csv')

# 加载 2016 年数据
df_2016 = pd.read_csv('2016年国内主要城市年度数据.csv')

# 加载 2017 年数据
df_2017 = pd.read_csv('2017年国内主要城市年度数据.csv')

# 绘制 2015 - 2017 年各个城市的国内生产总值的直方图
width = 0.25
x = range(len(df_2015['地区']))
plt.bar(x, df_2015['国内生产总值'], width, label='2015年')
plt.bar([i + width for i in x], df_2016['国内生产总值'], width, label='2016年')
plt.bar([i + 2 * width for i in x], df_2017['国内生产总值'], width, label='2017年')
plt.xticks([i + width for i in x], df_2015['地区'], rotation=45)
plt.xlabel('地区')
plt.ylabel('国内生产总值（亿元）')
plt.title('2015 - 2017 年各个地区的国内生产总值')
plt.legend()
plt.show()

# 绘制 2015 年各个城市的国内生产总值的饼状图
plt.pie(df_2015['国内生产总值'], labels=df_2015['地区'], autopct='%1.1f%%')
plt.title('2015 年各个地区的国内生产总值')
plt.show()