from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')  # устанавливает окно браузера в максимальном режиме
    browser = webdriver.Chrome(options=options_chrome)

    browser.get('http://parsinger.ru/blank/3/index.html')
    sleep(1)
    c = 0
    for i in browser.find_elements(By.CSS_SELECTOR, 'input[type="button"]'):
        i.click()

    for y in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[y])
        time.sleep(1)
        if browser.execute_script("return document.title;").isdigit():
            c += int(browser.execute_script("return document.title;"))
    print(c)


finally:
    browser.quit()