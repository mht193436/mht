import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
df = pd.read_csv('train.csv')

# 按 Pclass 分组，计算每组 Survived 的均值
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean()

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 绘制直方图
plt.bar(survival_rate_by_class.index.astype(str), survival_rate_by_class)
plt.xlabel('乘客等级')
plt.xticks(rotation=45)
plt.ylabel('生还率')
plt.title('不同乘客等级的生还率')

plt.show()