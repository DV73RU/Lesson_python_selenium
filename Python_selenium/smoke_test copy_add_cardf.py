"""Smoke testing."""


import time

from selenium import webdriver

from selenium.webdriver import ActionChains

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
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

""" Финкция поиска и нажатия на кнопку Add to card"""

def add_card(driver_g, xpath):
    try:
        button_add_card = driver_g.find_element(By.XPATH, xpath)
        button_add_card.click()
    except:
        button_add_card = None
    return button_add_card


login = "standard_user"     # Присваиваем переменной значение логина.
password_all = "secret_sauce"   # Присваиваемм переменной значение пароля.

# Присваиваем переменной значение локатора поля ввода логин.
user_name = driver_g.find_element(By.ID, 'user-name')
user_name.send_keys(login)  # Вставляем в поле логин значение логина.
print('Ввод логин')
time.sleep(2)

password = driver_g.find_element(By.ID, 'password')
password.send_keys(password_all)
print('Ввод пароля')
time.sleep(2)

# Локатор кнопки авторизации.
button_login = driver_g.find_element(By.ID, 'login-button')
button_login.click()
print('Клик кнопки авторизации')
time.sleep(2)

# """Проверяем что открыта страница PRODUCTS"""
# url_products = "https://www.saucedemo.com/inventory.html"
# get_url_products = driver_g.current_url
# print(get_url_products)
# # Проверяем открытой url и ожидаемый url.
# assert url_products == get_url_products
# # Выводим сообщение о коректности url PRODUCTS.
# print(f"Current URL: {get_url_products} matches {url_products}")

# """Информация о продукте №1 на странице."""
# produkt_1 = driver_g.find_element(
#     By.XPATH, "//a[@id = 'item_4_title_link']")       # Присваиваем переменной локатор название продукта №1 на странице.
# value_produkt_1 = produkt_1.text
# print(f"Название продукта №1: {value_produkt_1}")

# price_produkt_1 = driver_g.find_element(
#     By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №1 на странице.
# price_value_produkt_1 = price_produkt_1.text
# print(f"Цена продукта №1: {price_value_produkt_1}")



# add_to_cart = driver_g.find_element(
#     By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
# add_to_cart.click()
# print("Нажата кнопка 'ADD TO CARD' продукта №1")
# Присваиваем переменной локатор кнопки "add to card продукта №2".
# add_to_cart_2 = driver_g.find_element(
#     By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-bolt-t-shirt']")
# add_to_cart_2.click()
# print("Нажата кнопка 'ADD TO CARD' продукта №2")
# Присваиваем переменной локатор кнопки "значка количесво товаров в корзине".
# container = driver_g.find_element(
#     By.XPATH, "//span[@class ='shopping_cart_badge']")
# value_container = container.text
# print(f"Количество добавленного товара в корзину: {value_container}")
# # Присваиваем переменной локатор кнопки "значка корзины".
# shopping_cart = driver_g.find_element(
#     By.XPATH, "//a[@class='shopping_cart_link']")
# shopping_cart.click()
# print("Нажата кнопка 'Корзина'")

# """Проверяем что открыта страница корзины"""
# url_card = "https://www.saucedemo.com/cart.html"
# get_url_card = driver_g.current_url
# print(get_url_card)
# assert url_card == get_url_card
# # Выводим сообщение о коректности url корзины.
# print(f"Current URL: {get_url_card} matches {url_card}")
# time.sleep(2)
# """Информация о продукте №1 в корзине."""
# card_produkt_1 = driver_g.find_element(
#     By.XPATH, "//a[@id = 'item_4_title_link']")    # Присваиваем переменной локатор название продукта №1 в корзине.
# card_value_produkt_1 = card_produkt_1.text
# print(f"Название продукта №1 в корзине: {card_value_produkt_1}")
# assert value_produkt_1 == card_value_produkt_1
# print("Название продукта №1 на странице одинковое с названием продукта в корзине.")
