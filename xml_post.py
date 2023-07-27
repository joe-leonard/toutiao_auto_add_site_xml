from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from text_function import generate_target_url, submit_post_request
import logging

def xml_post_function(cookie_string, options_file):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

    # 初始化Chrome浏览器
    driver = webdriver.Chrome()

    # 打开网页
    url = "https://zhanzhang.toutiao.com/page/inner/link/info"  # 请替换为实际的网页URL
    driver.get(url)

    # 假设你已经获取到登录状态的Cookie信息
    cookies = [cookie.strip() for cookie in cookie_string.split(';')]

    # 将Cookie信息添加到浏览器会话中
    for cookie in cookies:
        name, value = cookie.split('=', 1)
        driver.add_cookie({"name": name, "value": value})

    # 刷新页面以使Cookie生效
    driver.refresh()

    time.sleep(10)

    # 从文件中读取选项列表
    with open(options_file, "r") as file:
        site_options = [line.strip() for line in file]
    try:
        output = ""
        # 遍历每个选项元素并打印文本
        for item in site_options:
            # 找到选择站点的选择框
            select_box = driver.find_element(By.XPATH, "//*[@id=\"app\"]/section/section/main/div/div[1]/div/div/div[2]")

            # 点击选择框，展开选项列表
            select_box.click()
            # 找到<input>元素
            input_element = driver.find_element(By.XPATH,
                                                "//*[@id=\"app\"]/section/section/main/div/div[1]/div/div/div[1]/span/input")
            input_element.clear()  # 清空<input>元素的内容（可选）
            input_element.send_keys(item)  # 输入内容到<input>元素
            time.sleep(1)  # 等待一秒（可选，根据实际情况调整等待时间）
            # 执行确认操作，例如按Enter键确认
            input_element.send_keys(Keys.ENTER)
            time.sleep(2)  # 等待一段时间，等待选项列表更新（根据实际情况调整等待时间）
            # Iterate through the list and input each item into the input element
            xml_text = generate_target_url(item)
            submit_post_request(driver, xml_text)
            output += f"Successfully processed item: {item}\n"
        return output
    except Exception as e:
        output = f"An error occurred: {e}\n"
        output += f"Error occurred at item: {item}\n"
        return output