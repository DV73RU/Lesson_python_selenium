"""https://demoqa.com/
Чек бокс"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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


base_url = 'https://demoqa.com/'
driver_g.get(base_url)
driver_g.maximize_window()

"""Проверка откртытия нужного URL"""

get_base_url = driver_g.current_url
assert base_url == get_base_url
print(f"Открыта страница: {get_base_url} соответствуетт {base_url}")

bootton_element = driver_g.find_element(
    By.XPATH, "//h5[normalize-space(text())='Elements']")
bootton_element.click()
print("Нажата кнопка 'Elements'")
# time.sleep(2)

"""Проверка открытия нужного URL"""
url_elements = "https://demoqa.com/elements"
get_url_elements = driver_g.current_url
# print(get_url_elements)
assert url_elements == get_url_elements
print(f"Открыта страница: {get_url_elements} соответствуетт {url_elements}")
# time.sleep(2)

bootton_check_box = driver_g.find_element(
    By.XPATH, "//span[normalize-space(text())='Check Box'] ")
bootton_check_box.click()
print("Нажата кнопка 'Check Box'")
# time.sleep(2)

check_box = driver_g.find_element(By.XPATH, "//span[@class='rct-title']")
check_box.click()
print("Нажат чекбокс 'Home'")

"""Проверка соответстия текста сообщения выюранного чек бокса"""

# Ищём текстовое поле "You have selected :"
text = "You have selected :"
text_selected = driver_g.find_element(
    By.XPATH, "//span[normalize-space(text())='You have selected :'] ").text
print(text_selected)
assert text == text_selected
print("Текст 'You have selected :' найден")

# Список опций выбираемых чекбоксами
ottions_list = ['home', 'desktop', 'notes', 'commands', 'documents', 'workspace', 'react', 'angular',
                'veu', 'office', 'public', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']

#TODO # Сравнить этот список с какими опции отображаются при нажатии на чек бокс 'Home' 

# Найти все элементы обций на странице 

options_text = driver_g.find_element(By.XPATH, "//div[@class='display-result mt-4']").text
print(options_text)
# list_1 = [options_text]
# list_2 = [ottions_text for i in range(str(ottions_text()))]
# print(list_2)

"""Фразу You have selected : эта функуия разбивает на слова и заносит в список.
Нужно что бы в списке фраза You have selected : была оддельным элементом списка"""
rices_1 = [str(i) for i in options_text.split()] # Получаем списк Всех  функций на сайте 
print(rices_1)


"""Рескрытие дерева чекбоксов"""
tree_check_box = driver_g.find_element(By.XPATH, "//button[@class = 'rct-option rct-option-expand-all']")
tree_check_box.click()
print("Нажат кнопка '+'")

time.sleep(2)

"""Проверка разворачивания дерева"""
open_tree = driver_g.find_element(By.XPATH, "//span[@class='rct-title']").text
print(open_tree)
# assert open_tree == True
# print("Дерево раскрыто")

"""Закрытие дерева чекбоксов"""
tree_check_box = driver_g.find_element(By.XPATH, "//button[@class = 'rct-option rct-option-collapse-all']")
tree_check_box.click()
print("Нажат кнопка '-'")

"""Проверка сворачивания дерева"""
