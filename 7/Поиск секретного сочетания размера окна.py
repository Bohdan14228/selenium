from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from math import ceil

from selenium.webdriver.support.wait import WebDriverWait

from _path import proxy
from selenium.webdriver import Keys

try:
    options_chrome = webdriver.ChromeOptions()

    options_chrome.add_argument('--proxy-server=%s' % proxy)
    # options_chrome.add_argument('--headless')
    options_chrome.add_argument('--start-maximized')  # устанавливает окно браузера в максимальном режиме
    browser = webdriver.Chrome(options=options_chrome)

    browser.get('http://parsinger.ru/window_size/1/')

    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    for i in window_size_x:
        for y in window_size_y:
            browser.set_window_size(i+16, y+147)
            sleep(1)

            # try:
            #     # Ожидание обновления текста в элементе result
            #     result = WebDriverWait(browser, 1).until(
            #         EC.text_to_be_present_in_element((By.ID, 'result'), '')
            #     )
            #     result_text = browser.find_element(By.ID, 'result').text
            #     if result_text:
            #         print(f"{x} x {y}")
            #         print(result_text)
            #         break
            # except:
            #     # Если не обновилось в течение 1 секунды, продолжить
            #     continue

            try:
                t = browser.find_element(By.ID, 'result').text
                if t != '':
                    print(t)
            except:
                pass


finally:
    browser.quit()