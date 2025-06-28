# 判断变量的数据类型
x = 10
y = "10"
z = True

print(f"x 是 {type(x)} 类型")
print(f"y 是 {type(y)} 类型")
print(f"z 是 {type(z)} 类型")

# 计算圆的面积
import math

# 定义 π 的值
pi = 3.14

# 接收用户输入的半径
radius = float(input("请输入圆的半径: "))

# 计算圆的面积
area = pi * (radius ** 2)

# 输出圆的面积
print(f"半径为 {radius} 的圆的面积是 {area}")

# 字符串转换为浮点数和整数
# 原始字符串
string_value = "3.14"

# 将字符串转换为浮点数
float_value = float(string_value)

# 将浮点数转换为整数
int_value = int(float_value)

# 输出结果
print(f"原始字符串: {string_value}")
print(f"转换为浮点数: {float_value}")
print(f"转换为整数: {int_value}")



