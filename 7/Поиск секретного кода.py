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

    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    # print(browser.find_element(By.ID, 'result'))
    # sleep(1000)
    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        sleep(1)

        alert = browser.switch_to.alert
        alert.accept()
        sleep(1)

        if browser.find_element(By.ID, 'result').text:
            print(browser.find_element(By.ID, 'result').text)

    # result = browser.find_element(By.ID, 'result')
    # if result:
    #     print(result.text)



finally:
    browser.quit()
