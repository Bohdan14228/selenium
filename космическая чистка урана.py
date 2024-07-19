from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)

    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    sleep(1)
    c = 0
    button = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for i in button:
        browser.execute_script("return arguments[0].scrollIntoView(true);", i)
        i.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    browser.quit()