from pprint import pprint
from selenium import webdriver
import time

# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://google.com/')
#     time.sleep(5000)
#     cookies = webdriver.get_cookies()
#     # pprint(cookies["NID"]['expiry'])
#     for cookie in cookies:
#         print(cookie)


import time
from pprint import pprint
from selenium import webdriver

cookie_dict = {
    'name': 'any_name_cookie',    # Любое имя для cookie
    'value': 'any_value_cookie',  # Любое значение для cookie
    'expiry': 2_000_000_000,      # Время жизни cookie в секундах
    'path': '/',                  # Директория на сервере дял которой будут доступны cookie
    'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
    'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
    'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
    'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
}

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/4/index.html')
    webdriver.add_cookie(cookie_dict)
    pprint(webdriver.get_cookies())
    time.sleep(100)