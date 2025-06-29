# 练习题 1

# 给定字符串 s1
s1 = "Python is a powerful programming language"

# （1）提取单词 "language"
words = s1.split()
last_word = words[-1]
print("Last word:", last_word)

# （2）将 s1 与 s2 连接，并使用一句 print 重复输出 3 次
s2 = " Let's learn together"
combined_string = s1 + s2
print((combined_string + "\n") * 3)

# （3）输出所有以 p 或 P 开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("Words starting with p or P:", p_words)


# 练习题 2

# 给定字符串 s3
s3 = " Hello, World! This is a test string. "

# （1）去除字符串前后的空格
trimmed_s3 = s3.strip()
print("Trimmed string:", trimmed_s3)

# （2）将所有字符转换为大写
upper_s3 = trimmed_s3.upper()
print("Uppercase string:", upper_s3)

# （3）查找子串 "test" 的起始下标
test_index = trimmed_s3.find("test")
print("Index of 'test':", test_index)

# （4）将 "test" 替换为 "practice"
replaced_s3 = trimmed_s3.replace("test", "practice")
print("String after replacing 'test' with 'practice':", replaced_s3)

# （5）以空格为分隔符分割字符串，并使用 "-" 连接分割后的列表
split_s3 = trimmed_s3.split()
joined_s3 = "-".join(split_s3)
print("String joined by '-':", joined_s3)