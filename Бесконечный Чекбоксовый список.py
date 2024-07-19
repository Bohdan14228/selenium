from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from math import ceil
from _path import proxy
from selenium.webdriver import Keys

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)

    browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
    list_input = []

    while True:
        input_tags = [x for x in browser.find_elements(By.CLASS_NAME, 'child_container')]
        for tag_input in input_tags:
            input_t = tag_input.find_elements(By.TAG_NAME, 'input')[-1]
            if input_t not in list_input:
                input_t.send_keys(Keys.DOWN)
                browser.execute_script("return arguments[0].scrollIntoView(true);", input_t)
                list_input.append(input_t)
        if len(list_input) == 100:
            break
    sleep(1)
    for checkbox in browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]'):
        if int(checkbox.get_attribute('value')) % 2 == 0:
            checkbox.click()
    sleep(1)
    browser.find_element(By.CLASS_NAME, 'alert_button').click()
    alert = browser.switch_to.alert
    print(alert.text)


finally:
    browser.quit()

