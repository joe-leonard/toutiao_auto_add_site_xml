# site_post.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging

def site_post_function(cookie_string,site_options_file):
    # Set up logging configuration
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

    driver = webdriver.Chrome()

    url = "https://zhanzhang.toutiao.com/page/inner/site/add"
    driver.get(url)

    cookies = [cookie.strip() for cookie in cookie_string.split(';')]

    for cookie in cookies:
        name, value = cookie.split('=', 1)
        driver.add_cookie({"name": name, "value": value})

    driver.refresh()

    wait = WebDriverWait(driver, 300)

    time.sleep(10)

    with open(site_options_file, "r") as file:
        site_options = [line.strip() for line in file]

    total_items = len(site_options)
    idx = 0
    item = None

    try:
        output = ""
        for idx, item in enumerate(site_options, 1):
            print(f"Working on loop index: {idx}, item: {item}, Total items: {total_items}")
            select_http = driver.find_element(By.XPATH, "//*[@id=\"app\"]/section/section/main/div/div[2]/div[2]/div[3]/div/span/span[1]/div/div/div[1]")
            action = ActionChains(driver)
            action.click(select_http).perform()
            time.sleep(2)

            select_https = driver.find_element(By.XPATH, "/html/body/span/div/ul/li[2]")
            action.click(select_https).perform()

            input_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/section/section/main/div/div[2]/div[2]/div[3]/div/span/span[2]/span/input")
            input_element.clear()
            input_element.send_keys(item)
            time.sleep(2)

            select_next = driver.find_element(By.XPATH, "//*[@id=\"app\"]/section/section/main/div/div[2]/div[2]/div[4]/button[2]/span")
            select_next.click()
            time.sleep(1)

            select_site = driver.find_element(By.XPATH, "//*[@id=\"app\"]/section/section/main/div/div[1]/div/div[1]/a")
            select_site.click()
            time.sleep(5)

            select_site_add = driver.find_element(By.XPATH, "//*[@id=\"app\"]/section/section/main/div/div[1]/div[2]/a/button/span")
            select_site_add.click()

            if idx % 5 == 0:
                time.sleep(30)

        driver.quit()
        return output

    except Exception as e:
        output = f"An error occurred: {e}\n"
        output += f"Error occurred at loop index: {idx}, item: {item}, Total items: {total_items}\n"
        driver.quit()
        return output
