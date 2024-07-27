from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    # browser.get('http://parsinger.ru/blank/1/1.html')
    url = 'https://stepik.org/course/119495/promo?auth=login'
    browser.get(url)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys("onlyolx1488@gmail.com")
    browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("Qwerty12345")
    time.sleep(1)
    browser.find_element(By.ID, "login_form").find_element(By.TAG_NAME, 'button').click()
    WebDriverWait(browser, 10).until(EC.url_changes(url))
    print(WebDriverWait(browser, 60).until(EC.visibility_of((By.ID, 'ember688'))))
    time.sleep(1000)
    div = browser.find_element(By.XPATH, '//*[@id="ember522"]/div')
    while True:
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

    time.sleep(100000)
finally:
    browser.quit()