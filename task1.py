# 练习题1：判断一个数是否为回文数
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# 测试示例
print("Is 121 a palindrome?", is_palindrome(121))  # 输出: True
print("Is 123 a palindrome?", is_palindrome(123))  # 输出: False

# 练习题2：计算任意数量参数的平均值
def calculate_average(*args):
    if not args:
        return 0
    total = sum(args)
    count = len(args)
    average = total / count
    return average

# 测试示例
print("Average of 1, 2, 3, 4, 5:", calculate_average(1, 2, 3, 4, 5))  # 输出: 3.0
print("Average with no arguments:", calculate_average())              # 输出: 0

# 练习题3：返回最长的字符串
def find_longest_string(*strings):
    if not strings:
        return None
    longest = max(strings, key=len)
    return longest

# 测试示例
print("Longest string in 'apple', 'banana', 'cherry':", find_longest_string("apple", "banana", "cherry"))  # 输出: banana
print("Longest string with no arguments:", find_longest_string())                                     # 输出: None

# 练习题4：创建模块并导入使用
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# 创建矩形对象并计算面积和周长
rectangle = Rectangle(5, 3)
print("Rectangle area:", rectangle.area())         # 输出: Rectangle area: 15
print("Rectangle perimeter:", rectangle.perimeter()) # 输出: Rectangle perimeter: 16



