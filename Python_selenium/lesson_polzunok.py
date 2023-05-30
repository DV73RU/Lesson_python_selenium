"""Взаимодействие с ползунком"""
# https://html5css.ru/howto/howto_js_rangeslider.php

# Установка:
# python -m pip install --upgrade pip.
# python -m venv .selenium - Установка вертуального окружениея.
# pip3 install selenium


import datetime 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-gpu')
options.add_argument('--mute-audio')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-infobars')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--no-sandbox')
options.add_argument('--no-zygote')
options.add_argument('--log-level=3')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-breakpad')
options.add_experimental_option("detach", True)
g = Service('H:\\Python.Selenium_lesson-1\\Python_selenium\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)


base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver_g.get(base_url)
driver_g.maximize_window()

"""Проверка откртытия нужного URL"""

get_base_url = driver_g.current_url
assert base_url == get_base_url
print(f"Открыта страница: {get_base_url} соответствуетт {base_url}")

action = ActionChains(driver_g)
value1 = driver_g.find_element(By.XPATH, "//*[@id='slidecontainer']/input")
action.click_and_hold(value1).move_by_offset(20, 0).release().perform
