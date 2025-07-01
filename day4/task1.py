import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者 ['Microsoft YaHei', 'FangSong'] 等
plt.rcParams['axes.unicode_minus'] = False

# 国家
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数
gold_medal = np.array([16, 12, 9, 8, 8])
# 银牌个数
silver_medal = np.array([8, 10, 4, 10, 5])
# 铜牌个数
bronze_medal = [13, 5, 2, 7, 5]

x = np.arange(len(countries))

# 恢复x轴的坐标值
plt.xticks(x, countries)

# 绘图
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold", label='金牌')
plt.bar(x, silver_medal, width=0.2, color="silver", label='银牌')
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown", label='铜牌')

# 显示文本标签
# 金牌
for i in x:
    plt.text(x[i] - 0.2, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
# 银牌
for i in x:
    plt.text(x[i], silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
# 铜牌
for i in x:
    plt.text(x[i] + 0.2, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

plt.legend()
plt.title('各国奖牌数量对比')
plt.xlabel('国家')
plt.ylabel('奖牌数')

plt.tight_layout()
plt.show()