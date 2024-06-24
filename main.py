from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from _path import _path, profile_path, proxy


try:
    options_chrome = webdriver.ChromeOptions()
    # options_chrome.add_extension(f'{_path}')
    # options_chrome.add_argument(f"{profile_path}")
    # options_chrome.add_argument('--proxy-server=%s' % proxy)
    # options_chrome.add_argument('--headless')
    
    options_chrome.add_argument('--start-maximized')

    browser = webdriver.Chrome(options=options_chrome)
    browser.get('https://2ip.ru/')
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)



finally:
    browser.quit()
