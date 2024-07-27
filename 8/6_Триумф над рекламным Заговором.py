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

    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')

    browser.find_element(By.CSS_SELECTOR, 'span[class="close"]').click()
    if WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, 'ad'))):
        browser.find_element(By.TAG_NAME, 'button').click()
        print(browser.find_element(By.ID, 'message').text)


finally:
    browser.quit()