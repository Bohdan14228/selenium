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

    browser.get("https://parsinger.ru/selenium/5.8/5/index.html")
    sleep(1)
    for i in browser.find_elements(By.TAG_NAME, 'iframe')[-1:]:
        browser.switch_to.frame(i)
        browser.find_element(By.TAG_NAME, 'button').click()
        sleep(1)
        pin = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        browser.find_element(By.ID, 'guessInput').send_keys(pin)
        sleep(1)
        browser.find_element(By.ID, 'checkBtn').click()

        try:
            alert = browser.switch_to.alert
            print(alert.text)
            break
        except:
            pass

        browser.find_element(By.ID, 'guessInput').clear()


finally:
    browser.quit()