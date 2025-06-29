import os, re

# 原始图片路径
folder_path = "新建文件夹"
# 新名称列表
new_names = [
    "冯秋华", "陈思彤", "万怡蓉", "洪亮", "柳苗苗",
    "蒋良美", "和彦汝", "彭欣怡", "熊朵", "于跃",
    "许嘉屹", "刘俊锋", "叶曜玮", "熊壮", "汪宇鑫",
    "付星宇", "秦焱彬", "甘鑫", "武怡聪", "程卫",
    "郑芳健", "王芳龙", "麻弘涛", "徐策", "陈义谋"
]

# 获取文件夹中所有png文件并按Windows自然排序
files = sorted([
    "0a01b28cf1fcf2cfe2d71f29d731ced4.png",
    "0bc93446a10037c9dc172196e6a091d3.png",
    "0d7181956a1557a4c04a54fac101a7a9.png",
    "0e4fc158a04f115df5790aff81e5f7ed.png",
    "0e480bfcb517a317a31751d7547816a3.png",
    "0f69525b0c7c80c3289ca7428390c961.png",
    "0f312652ecbe7048446f4337a8534aee.png",
    "1d976b7d91985185f2aba402315a8d97.png",
    "2a515616393fe569f8c7d91870834df9.png",
    "2eac0399608eb148c9f323bb5631b71e.png",
    "02f31defa56eb14b6c0c8b29c1fd3b7c.png",
    "3abec6ffc979df972fb0dc7230c03529.png",
    "3cb89360d808cbfb5de4259e46137a32.png",
    "3cc87f3b0e49fa277cdf5fe026148d10.png",
    "3d9ff739bf8e5405f1d71942e892af41.png",
    "3f804589285c952bd6a1f4ae0915c233.png",
    "4b113e899126e33fe4558eb8f3763fcd.png",
    "4c6a57b5a73b7bf65ef9616c60d2722b.png",
    "4c73bff49fbdec20865f3deda396d3de.png",
    "4d5fea0afb49251aa6f92361a84ee5a7.png",
    "4ddb515e898fa18e0903379947b45494.png",
    "4e32a022a8f33372ede7f585069c483b.png",
    "5a0c830d7347d2bb0c51df4815176a79.png",
    "05b48aa7c18c38ba677dbede07dac3bc.png",
    "05ce007803a016736db30d88ef579a82.png"
], key=lambda x: [int(c) if c.isdigit() else c.lower() for c in re.split('([0-9]+)', x)])

# 执行重命名
for old_name, new_name in zip(files, new_names):
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, f"{new_name}.png")
    os.rename(old_path, new_path)
    print(f"已将 {old_name} 重命名为 {new_name}.png")

print("所有文件重命名完成！")