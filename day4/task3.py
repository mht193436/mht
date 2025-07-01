import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置中文字体为 SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']

# 读取数据集，假设文件名为 train.csv，若路径不同需调整
df = pd.read_csv('train.csv')

# 按 Pclass 列分组，计算 Survived 列的平均值
grouped_class = df.groupby('Pclass')['Survived'].mean()

# 设置图形风格
plt.style.use('ggplot')

# 绘制不同 Pclass 的生还率直方图
plt.figure(figsize=(8, 6))
bars = plt.bar(grouped_class.index.astype(str), grouped_class.values, color='skyblue')
plt.xlabel('乘客等级', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.ylabel('生还率', fontsize=14)
plt.title('不同乘客等级的生还率', fontsize=16)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=12)

# 添加网格线
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# 处理缺失值
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 创建 10 岁一个年龄段的年龄区间
age_bins = list(range(0, int(df['Age'].max()) + 11, 10))
age_labels = [f'{i}-{i + 9}' for i in age_bins[:-1]]
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# 按年龄区间分组，计算生还率
grouped_age = df.groupby('AgeGroup', observed=True)['Survived'].mean()

# 绘制不同年龄区间的生还率直方图
plt.figure(figsize=(8, 6))
bars = plt.bar(grouped_age.index.astype(str), grouped_age.values, color='salmon')
plt.xlabel('乘客年龄段', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.ylabel('生还率', fontsize=14)
plt.title('不同乘客年龄段的生还率', fontsize=16)

# 添加数值标签，检查高度是否为有限值
for bar in bars:
    height = bar.get_height()
    if np.isfinite(height):
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=12)

# 添加网格线
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()