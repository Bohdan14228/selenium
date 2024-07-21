from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from math import ceil
from _path import proxy
from selenium.webdriver import Keys

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')  # устанавливает окно браузера в максимальном режиме
    browser = webdriver.Chrome(options=options_chrome)

    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')

    pincode = [i.text for i in browser.find_elements(By.CSS_SELECTOR, 'span[class="pin"]')]
    # print(pincode)
    # sleep(100)
    for pin in pincode:
        browser.find_element(By.CSS_SELECTOR, 'input[value="Проверить"]').click()
        sleep(0.5)
        alert = browser.switch_to.alert
        alert.send_keys(pin)
        alert.accept()

        result = browser.find_element(By.ID, 'result')
        if "Неверный пин-код" not in result.text:
            print(result.text)
            break

finally:
    browser.quit()