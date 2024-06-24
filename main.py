from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import _path, profile_path, proxy


try:
    options_chrome = webdriver.ChromeOptions()
    # options_chrome.add_extension(f'{_path}')
    # options_chrome.add_argument(f"{profile_path}")
    # options_chrome.add_argument('--proxy-server=%s' % proxy)
    # options_chrome.add_argument('--headless')     # работает без графического интерфейса
    
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    # browser.get('https://parsinger.ru/methods/1/index.html')
    browser.get('https://2ip.ru/')
    time.sleep(100000)
    per = browser.find_element(By.ID, 'result').text
    while per is None:
        browser.refresh()
        time.sleep(2)
        per = browser.find_element(By.ID, 'result').text

    print(per)


finally:
    browser.quit()
