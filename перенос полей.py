from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')

    for url in browser.find_elements(By.CLASS_NAME, 'parent'):
        element = url.find_element(By.XPATH, './/textarea[@color="gray"]')
        element.clear()
        url.find_element(By.XPATH, './/textarea[@color="blue"]').send_keys(element.text)
        url.find_element(By.TAG_NAME, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'congrats').text)
finally:
    browser.quit()