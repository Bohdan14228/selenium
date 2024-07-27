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

    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')

    ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
                   'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

    for id_ in ids_to_find:
        WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.ID, id_))).click()
    print(browser.switch_to.alert.text)

finally:
    browser.quit()