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

    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    r = []
    for button in browser.find_elements(By.CLASS_NAME, 'box_button'):
        button.click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'close_ad'))).click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, 'ad_window')))
        WebDriverWait(browser, 10).until(lambda _: button.text != '')   # ожидание текста в атрибуте
        r.append(button.text)
    print('-'.join(r))


finally:
    browser.quit()