from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import _path, profile_path, proxy

try:
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/scroll/4/index.html')
    counter = 0
    time.sleep(2)
    for element in browser.find_elements(By.CLASS_NAME, 'btn'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        counter += int(browser.find_element(By.ID, "result").text)
    time.sleep(1)
    print(counter)
finally:
    browser.quit()