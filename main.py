from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import _path, profile_path, proxy

try:
    options_chrome = webdriver.ChromeOptions()
    # browser.refresh()     # перезагрузка странички браузера
    # options_chrome.add_extension(f'{_path}')

    # options_chrome.add_argument(f"{profile_path}")

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    # options.add_argument(f'--proxy-server=https://{login}:{password}@45.145.57.201:13231')

    # options_chrome.add_argument('--headless')     # работает без графического интерфейса
    options_chrome.add_argument('--start-maximized')    # устанавливает окно браузера в максимальном режиме

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://parsinger.ru/methods/5/index.html')
    d = {}
    for url in browser.find_elements(By.CLASS_NAME, "urls"):
        url = url.find_element(By.TAG_NAME, 'a').get_attribute('href')
        browser.get(url)
        cook = browser.get_cookies()[0].get('expiry')
        d[url] = cook
        browser.back()
    max_key = max(d, key=d.get)
    browser.get(max_key)    
    print(browser.find_element(By.ID, 'result').text)
finally:
    browser.quit()
