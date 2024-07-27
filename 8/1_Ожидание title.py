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

    browser.get('https://parsinger.ru/expectations/3/index.html')
    btn = browser.find_element(By.ID, 'btn')
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(btn))
    button.click()
    if WebDriverWait(browser, 20).until(EC.title_is("345FDG3245SFD")):
        print(browser.find_element(By.ID, 'result').text)
    # print(title)
    sleep(5)

finally:
    browser.quit()