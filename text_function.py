# my_function.py

from selenium.webdriver.common.by import By
import time


def generate_target_url(site):
    # 假设你的拼接规则是：https://{site}/sitemap/articles.xml
    target_url = f"https://{site}/sitemap/articles.xml"
    return target_url
def submit_post_request(driver, xml_text):
    # 找到<textarea>元素
    textarea_element = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[4]/textarea')
    # 找到提交按钮
    submit_button = driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div[4]/div[6]/button/span')
    # 输入文本到<textarea>元素
    textarea_element.clear()
    textarea_element.send_keys(xml_text)
    time.sleep(1)
    # 点击提交按钮
    submit_button.click()
    time.sleep(2)

