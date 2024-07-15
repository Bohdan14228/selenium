from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('http://parsinger.ru/scroll/2/index.html')

    count = 0
    for checkbox in browser.find_elements(By.CLASS_NAME, 'item'):
        checkbox.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        digit = checkbox.find_element(By.TAG_NAME, 'span').text
        if digit.isdigit():
            count += int(digit)
    print(count)
    sleep(100)
finally:
    browser.quit()