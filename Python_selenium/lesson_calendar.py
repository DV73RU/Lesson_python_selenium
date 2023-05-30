"""Взаимодействие со скрытыми элементами."""
# https://selenium-python.com/

# Установка:
# python -m pip install --upgrade pip.
# python -m venv .selenium - Установка вертуального окружениея.
# pip3 install selenium


"""https://demoqa.com/
Дабл клик"""

import datatime 
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


base_url = 'https://demoqa.com/date-picker'
driver_g.get(base_url)
driver_g.maximize_window()

"""Проверка откртытия нужного URL"""

get_base_url = driver_g.current_url
assert base_url == get_base_url
print(f"Открыта страница: {get_base_url} соответствуетт {base_url}")


new_date = driver_g.find_element(
    By.XPATH, "//input[@id='datePickerMonthYearInput']")

# print(new_date)
new_date.send_keys(Keys.BACKSPACE*10)
print("Дада стёрта")
time.sleep(2)

new_date.send_keys("11/04/2023")
print("Введена новая дата")
time.sleep(2)
new_date.send_keys(Keys.RETURN)




# print("Нажата кнопка 'Double Click Me'")

# label = driver_g.find_element(
#     By.XPATH, "//p[@id='doubleClickMessage']").text
# # Cообщение о двойном нажатии на кнопку Double Click Me //p[@id='doubleClickMessage']
# print(label)
