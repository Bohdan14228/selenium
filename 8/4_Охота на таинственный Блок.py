from time import sleep
from _path import proxy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')  # устанавливает окно браузера в максимальном режиме
    browser = webdriver.Chrome(options=options_chrome)

    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    element = (WebDriverWait(browser, 30)
               .until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click())
    sleep(0.1)
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()