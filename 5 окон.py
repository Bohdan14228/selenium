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

    browser.get('http://parsinger.ru/infiniti_scroll_3/')
    sleep(1)
    counter = 0
    for i in range(1, 6):
        div = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div')
        sleep(1)
        while True:
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
            sleep(1)
            span = browser.find_element(By.CLASS_NAME, f"scroll-container_{i}").find_elements(By.TAG_NAME, 'span')
            if 'last-of-list' in span[-1].get_attribute('class'):
                counter += sum(int(i.text) for i in span)
                print(counter)
                break
    print(counter)

finally:
    browser.quit()