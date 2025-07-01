import pandas as pd
import matplotlib.pyplot as plt

# 读取数据集，假设文件名为 train.csv，若路径不同需调整
try:
    data = pd.read_csv('train.csv')
except FileNotFoundError:
    print("错误：找不到 train.csv 文件，请检查文件路径是否正确。")
    exit()
except Exception as e:
    print(f"错误：读取文件时发生异常: {e}")
    exit()

# 检查数据列是否存在
required_columns = ['Age', 'Sex', 'Survived']
for col in required_columns:
    if col not in data.columns:
        print(f"错误：数据集中缺少必要的列 '{col}'")
        exit()

# 对年龄进行分组
data['AgeGroup'] = pd.cut(data['Age'], bins=[0, 18, 40, 60, float('inf')], labels=['0-18', '19-40', '41-60', '61+'])

# 按性别和年龄组分组，计算生还率
grouped = data.groupby(['Sex', 'AgeGroup'])['Survived'].mean().reset_index()

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 绘制直方图
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(grouped['AgeGroup'].unique()))

for i, sex in enumerate(grouped['Sex'].unique()):
    subgroup = grouped[grouped['Sex'] == sex]
    plt.bar([pos + i * bar_width for pos in index], subgroup['Survived'], width=bar_width, label=sex)

# 设置图表标签和标题
plt.xlabel('年龄组')
plt.ylabel('生还率')
plt.title('性别和年龄对生还率的影响')
plt.xticks([pos + bar_width / 2 for pos in index], grouped['AgeGroup'].unique())
plt.legend()

plt.tight_layout()  # 确保标签和标题不会被裁剪
plt.show()