import requests
from bs4 import BeautifulSoup

def three():
    # 定义爬取网址
    url = "https://movie.douban.com/chart"
    # 定义完整的浏览器表头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    try:
        # 向目标网站发送请求并获取网页源码
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'  # 设置编码
        response.raise_for_status()  # 检查请求是否成功

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有电影链接标签
        movie_links = soup.find_all('a', class_='nbg')

        # 提取电影名称
        print("豆瓣电影排行榜中的电影名称：")
        for link in movie_links:
            movie_title = link.get('title')  # 获取 title 属性
            if movie_title:
                print(movie_title)

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")

if __name__ == "__main__":
    three()