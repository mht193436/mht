import requests
import os
from lxml import etree

# 爬取网页图片，并下载到本地
def download_images():
    url = "http://pic.netbian.com/"
    try:
        # 向目标网站发送请求并获取网页源码
        response = requests.get(url)
        response.encoding = "gbk"
        body = response.text

        html = etree.HTML(body)
        img_list = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print("找到图片：", img_list)

        for i, img_url in enumerate(img_list):
            # 拼接图片路径
            full_url = url + img_url
            try:
                img_response = requests.get(full_url)
                img_data = img_response.content

                # 保存路径
                save_dir = 'd:\\images'
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                save_path = os.path.join(save_dir, '{}.gif'.format(i))
                try:
                    with open(save_path, 'wb') as f:
                        f.write(img_data)
                    print(f"成功下载图片到: {save_path}")
                except Exception as e:
                    print(f"保存图片失败: {str(e)}")
            except Exception as e:
                print(f"下载图片 {full_url} 失败: {str(e)}")

        print("下载完毕")
    except Exception as e:
        print(f"获取网页失败: {str(e)}")

if __name__ == "__main__":
    download_images()