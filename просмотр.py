from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    # browser.get('http://parsinger.ru/blank/1/1.html')
    browser.get('https://stepik.org/lesson/732079/step/8?unit=733612')
    time.sleep(100000)
finally:
    browser.quit()