from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    # browser.get('https://parsinger.ru/selenium/5.5/5/test/test.html')
    time.sleep(1)
    for i in browser.find_elements(By.XPATH,
                                   '//*[@style[contains(., "width: 100%") '
                                   'and contains(., "background-color: rgb")]]'
                                   ):
        span = i.find_element(By.TAG_NAME, 'span').text

        for _hex in i.find_element(By.TAG_NAME, 'select').find_elements(By.TAG_NAME, 'option'):
            if _hex.text == span:
                _hex.click()

        for btn in i.find_elements(By.XPATH, './/button[@data-hex]'):

            if btn.get_attribute('data-hex') == span:
                btn.click()

        i.find_element(By.XPATH, './/input[@type="checkbox"]').click()
        i.find_element(By.XPATH, './/input[@type="text"]').send_keys(span)
        i.find_element(By.XPATH, ".//button[contains(text(), 'Проверить')]").click()
    browser.find_element(By.XPATH, '/html/body/button').click()
    print(browser.switch_to.alert.text)
    time.sleep(1)
finally:
    browser.quit()