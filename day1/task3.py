# 1. 使用列表推导式存储 1-100 的整数，然后输出其中所有偶数。
numbers = [i for i in range(1, 101)]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# 2. 给定一个列表，删除其中的重复元素并保持顺序不变。
def remove_duplicates(lst):
    seen = set()
    unique_list = [x for x in lst if not (x in seen or seen.add(x))]
    return unique_list

sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_sample_list = remove_duplicates(sample_list)
print("List after removing duplicates:", unique_sample_list)

# 3. 假设两个列表为 keys = ["a", "b", "c"], values = [1, 2, 3]，
# 将它们合并为一个字典并输出（第一个列表为键，第二个列表为值）。
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print("Combined dictionary:", combined_dict)

# 4. 定义一个元组存储学生信息（姓名，年龄，成绩），然后解包并输出各字段。
student_info = ("Alice", 20, 90)
name, age, score = student_info
print(f"Name: {name}, Age: {age}, Score: {score}")