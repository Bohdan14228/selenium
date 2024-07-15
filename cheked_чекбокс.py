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
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    time.sleep(2)
    count = 0
    for url in browser.find_elements(By.CLASS_NAME, 'parent'):
        if url.find_element(By.CLASS_NAME, 'checkbox').is_selected():   # проверяем отмечен ли чекбокс
            count += int(url.text)
    print(count)
    time.sleep(2)
finally:
    browser.quit()