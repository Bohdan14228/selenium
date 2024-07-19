from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from math import ceil
from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)

    browser.get("https://parsinger.ru/selenium/5.7/5/index.html")
    actions = ActionChains(browser)
    for button in browser.find_elements(By.CLASS_NAME, 'timer_button'):
        # print(round(ceil(button.text)))
        actions.click_and_hold(button).pause(ceil(float(button.text))).release().perform()
        sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
finally:
    browser.quit()