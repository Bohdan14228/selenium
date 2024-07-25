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

    sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
             'http://parsinger.ru/blank/1/3.html',
             'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
             'http://parsinger.ru/blank/1/6.html', ]
    c = 0
    for site in range(len(sites)):
        browser.execute_script(f'window.open("{sites[site]}", "_blank{site+1}");')
        sleep(1)
        browser.switch_to.window(browser.window_handles[-1])
        browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        sleep(1)
        c += int(browser.find_element(By.CSS_SELECTOR, 'span[id="result"]').text) ** 0.5
    print(round(c, 9))

finally:
    browser.quit()