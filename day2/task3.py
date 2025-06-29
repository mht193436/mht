import os, re

# 原始图片路径
folder_path = "新建文件夹"
# 新名称列表 (调整顺序)
new_names = [
    "冯秋华", "陈思彤", "万怡蓉", "洪亮", "柳苗苗",
    "蒋良美", "和彦汝", "彭欣怡", "熊朵", "于跃",
    "许嘉屹", "刘俊锋", "叶曜玮", "熊壮", "汪宇鑫",
    "付星宇", "秦焱彬", "甘鑫", "武怡聪", "程卫",
    "郑芳健", "王芳龙", "麻弘涛", "徐策", "陈义谋"
]

# 获取文件夹中所有png文件并按Windows自然排序，确保5a0c830d7347d2bb0c51df4815176a79.png是最后一个文件
files = sorted(
    [f for f in os.listdir(folder_path) if f.endswith('.png')],
    key=lambda x: [
        "inf" if x == "5a0c830d7347d2bb0c51df4815176a79.png" else
        int(c) if c.isdigit() else c.lower()
        for c in re.split('([0-9]+)', x)
    ]
)

# 验证文件数量和名称列表匹配
if len(files) != len(new_names):
    print(f"错误: 文件数量({len(files)})与名称数量({len(new_names)})不匹配")
    exit(1)

# 执行重命名
for old_name, new_name in zip(files, new_names):
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, f"{new_name}.png")
    if os.path.exists(new_path):
        os.remove(new_path)
    os.rename(old_path, new_path)
    print(f"已将 {old_name} 重命名为 {new_name}.png")

print("所有文件重命名完成！")