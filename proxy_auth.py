import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver


options = {'proxy': {
    'http': "socks5://AZNzuBZX:uNdek1PJ@91.220.81.99",
    }}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)