"""Изменение даты применяя библиотеку datetime """
# https://selenium-python.com/

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


base_url = 'https://demoqa.com/date-picker'
driver_g.get(base_url)
driver_g.maximize_window()

"""Проверка откртытия нужного URL"""

get_base_url = driver_g.current_url
assert base_url == get_base_url
print(f"Открыта страница: {get_base_url} соответствуетт {base_url}")

# TODO Удалить из поля ввода сегодняшнию дату.
# TODO Сненрировать новую дату присвоить переменной вставть в поле ввода даты

current_date = datetime.datetime.today()
delta_data = datetime.timedelta(days=10)

past_date = current_date + delta_data
print(past_date.strftime('%m/%d/%y'))   # Печатаем новую дату

new_date = driver_g.find_element(
    By.XPATH, "//input[@id='datePickerMonthYearInput']") # Ищём поле вода даты.


new_date.send_keys(Keys.BACKSPACE*10) # Удаляем сегоднешнею дату.
print("Дада стёрта")
time.sleep(2)

new_date.send_keys(past_date.strftime('%m/%d/%y')) # В поле ввода вставляем новуб дату.
print("Введена новая дата")
time.sleep(2)
new_date.send_keys(Keys.RETURN)

"""Подумать"""
# TODO Проверить, после удаления даты поле ввода пустое.
# TODO Проверить что новая дата +10 дней введена в проле верно, сравнить с past_date