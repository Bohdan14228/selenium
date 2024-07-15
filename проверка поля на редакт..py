from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import _path, profile_path, proxy

try:
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    # time.sleep(100)
    # browser.find_element(By.CLASS_NAME, 'text-field').clear()
    for field in browser.find_elements(By.CLASS_NAME, 'text-field'):
        # print(field.get_attribute('disabled'))
        if not field.get_attribute('disabled'):     # проверки доступности текстового поля
            field.clear()   # очищаем текстовое поле

    button = browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
    time.sleep(1)


finally:
    browser.quit()