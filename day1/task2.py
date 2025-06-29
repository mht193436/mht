# 1. 输出1到100之间的所有素数
def print_primes():
    """打印1到100之间的所有素数"""
    print("1-100之间的素数:")
    for num in range(2, 101):  # 1不是素数
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
    print()  # 换行

# 2. 计算斐波那契数列的前20项
def fibonacci_sequence(n=20):
    """生成斐波那契数列前n项"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(f"\n斐波那契数列前{n}项:")
    print(fib)

# 3. 使用while循环计算特定条件的数字和
def special_sum():
    """计算1-10000之间能被3或5整除但不能被15整除的数字和"""
    total = 0
    num = 1
    while num <= 10000:
        if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
            total += num
        num += 1
    print(f"\n1-10000之间能被3或5整除但不能被15整除的数字和: {total}")

# 调用所有函数
if __name__ == "__main__":
    print_primes()
    fibonacci_sequence()
    special_sum()