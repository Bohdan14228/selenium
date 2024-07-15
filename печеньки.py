from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import _path, profile_path, proxy

try:
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/methods/3/index.html')
    # time.sleep(1000000)
    # for i in browser.get_cookies():
    #     print(i)
    time.sleep(2)
    print(sum(int(i.get("value")) for i in browser.get_cookies() if int(i.get("name").split('_')[-1]) % 2 == 0))


finally:
    browser.quit()