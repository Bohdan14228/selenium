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

    pincods = []

    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    for button in browser.find_elements(By.CLASS_NAME, 'buttons')[::-1]:
        button.click()
        sleep(1)

        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        sleep(1)

        browser.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(pin)
        # sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[value="Проверить"]').click()
        # sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[type="text"]').clear()

        result = browser.find_element(By.ID, 'result')
        if "Неверный пин-код" not in result.text:
            print(result.text)
            break



finally:
    browser.quit()
