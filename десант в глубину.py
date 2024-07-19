from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from _path import proxy

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)

    browser.get('http://parsinger.ru/infiniti_scroll_2/')
    sleep(1)
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    while True:
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
        sleep(1)
        span = browser.find_element(By.CLASS_NAME, 'scroll-container').find_elements(By.TAG_NAME, 'p')
        if 'last-of-list' in span[-1].get_attribute('class'):
            print(sum(int(i.text) for i in span))
            break



finally:
    browser.quit()