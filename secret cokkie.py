from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/methods/3/index.html')

    print(sum(int(i.get("value")) for i in browser.get_cookies()))
finally:
    browser.quit()