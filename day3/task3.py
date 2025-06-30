import time
import random
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# 文献列表 - 可在此处添加或删除需要获取BibTeX的文献标题
papers = [
    "Automatic crater detection and age estimation for mare regions on the lunar surface",
    "The origin of planetary impactors in the inner solar system",
    "Deep learning based systems for crater detection: A review",
    "A preliminary study of classification method on lunar topography and landforms",
    "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution",
    "Fast r-cnn",
    "You only look once: Unified, real-time object detection",
    "Attention is all you need",
    "End-to-end object detection with transformers"
]


def setup_driver():
    """配置并初始化Chrome浏览器驱动，添加反爬措施和用户代理"""
    chrome_options = Options()
    # 禁用GPU加速，避免某些系统兼容性问题
    chrome_options.add_argument('--disable-gpu')
    # 禁用沙箱模式，提高稳定性
    chrome_options.add_argument('--no-sandbox')
    # 禁用共享内存使用，防止内存溢出
    chrome_options.add_argument('--disable-dev-shm-usage')

    # 反自动化特征设置，伪装成普通用户浏览器
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # 设置随机用户代理，模拟不同浏览器访问
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ]
    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')

    # 创建并配置Chrome浏览器驱动
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 进一步隐藏自动化特征，避免被网站识别为爬虫
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver


def human_like_delay(min_delay=0.5, max_delay=3.0):
    """模拟人类操作的随机延迟，避免被服务器识别为自动化程序"""
    time.sleep(random.uniform(min_delay, max_delay))


def get_bibtex(driver, paper_title):
    """
    在Google Scholar上搜索指定标题的文献并获取其BibTeX引用格式

    参数:
    driver: Selenium WebDriver实例
    paper_title: 要搜索的文献标题

    返回:
    文献的BibTeX引用文本，如果获取失败则返回错误信息
    """
    try:
        # 编码文献标题并构建Google Scholar搜索URL
        encoded_title = urllib.parse.quote_plus(paper_title)
        search_url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={encoded_title}"

        # 访问搜索页面并等待随机时间
        driver.get(search_url)
        human_like_delay(1.0, 2.5)

        # 等待搜索结果加载完成
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.gs_r.gs_or.gs_scl"))
        )

        # 模拟人类浏览行为：随机滚动页面
        for _ in range(random.randint(1, 3)):
            driver.execute_script("window.scrollBy(0, window.innerHeight * 0.5);")
            human_like_delay(0.7, 1.5)

        # 定位第一个搜索结果
        first_result = driver.find_element(By.CSS_SELECTOR, "div.gs_r.gs_or.gs_scl")

        # 点击"Cite"按钮，显示引用选项
        cite_button = first_result.find_element(By.CSS_SELECTOR, "a.gs_or_cit")
        driver.execute_script("arguments[0].click();", cite_button)
        human_like_delay(1.0, 2.0)

        # 等待引用弹出窗口加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.gs_citr"))
        )

        # 定位并点击BibTeX格式链接
        bibtex_link = driver.find_element(By.XPATH, "//a[contains(., 'BibTeX')]")
        bibtex_url = bibtex_link.get_attribute('href')

        # 访问BibTeX内容页面
        driver.get(bibtex_url)
        human_like_delay(2.0, 3.0)

        # 获取并返回BibTeX文本内容
        pre_element = driver.find_element(By.TAG_NAME, 'pre')
        return pre_element.text

    except TimeoutException:
        print(f"超时错误：未能找到文献 '{paper_title[:50]}...' 的搜索结果")
        return f"@article{{ERROR: Timeout - {paper_title[:50]}...}}\n"

    except NoSuchElementException:
        print(f"元素未找到：无法获取文献 '{paper_title[:50]}...' 的引用信息")
        return f"@article{{ERROR: Element not found - {paper_title[:50]}...}}\n"

    except WebDriverException as e:
        print(f"浏览器操作异常：处理文献 '{paper_title[:50]}...' 时出错 - {str(e)[:100]}")
        return f"@article{{ERROR: WebDriver error - {str(e)[:100].replace('@', '')}}}\n"

    except Exception as e:
        print(f"未知错误：处理文献 '{paper_title[:50]}...' 时发生意外 - {str(e)[:100]}")
        return f"@article{{ERROR: {str(e)[:100].replace('@', '')}}}\n"


def main():
    """主函数：设置浏览器，处理文献列表，并输出BibTeX引用"""
    # 初始化浏览器驱动
    driver = setup_driver()
    output = "以下是您文献的BibTeX引用格式：\n\n"

    try:
        # 先访问Google Scholar主页建立正常会话
        driver.get("https://scholar.google.com")
        human_like_delay(2.0, 4.0)

        # 遍历文献列表，逐个获取BibTeX引用
        for i, paper in enumerate(papers, 1):
            print(f"正在处理第 {i}/{len(papers)} 篇文献: {paper[:50]}...")

            # 添加随机延迟，避免频繁请求导致IP被封
            human_like_delay(random.uniform(3.0, 7.0))

            # 获取当前文献的BibTeX引用
            bibtex = get_bibtex(driver, paper)

            # 将BibTeX添加到输出内容中，并添加分隔标记
            output += f"%%% 文献 {i} - {paper[:60]}... %%%\n"
            output += bibtex + "\n\n"

            # 返回主页，准备处理下一篇文献
            driver.get("https://scholar.google.com")
            human_like_delay(1.5, 2.5)

        # 处理完成后，打印完整的BibTeX引用结果
        print("\n" + "=" * 70)
        print(output)
        print("=" * 70)
        print("所有文献的BibTeX格式已成功生成！")

    except Exception as e:
        print(f"程序运行过程中发生严重错误: {str(e)}")
    finally:
        # 无论是否成功，都关闭浏览器，释放资源
        driver.quit()
        print("浏览器已关闭")


if __name__ == "__main__":
    main()