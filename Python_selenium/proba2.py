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
        # button_add_card.click()
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
# def func1():
#     print("Функция 1")

# def func2():
#     print("Функция 2")

# def func3():
#     print("Функция 3")

# func_list = [func1, func2, func3]

# # Вызовем каждую функцию из списка в цикле:
# for func in func_list:
#     func()

# TODO Спарсить название товаров и вставить в список.
# TODO Скрипт сканирует сколько продуктов на одной странице.
"""Информация о продукте №1 на странице."""
produkt_1 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_4_title_link']")       # Присваиваем переменной локатор название продукта №1 на странице.
value_produkt_1 = produkt_1.text
print(f"Название продукта №1: {value_produkt_1}")

price_produkt_1 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №1 на странице.
price_value_produkt_1 = price_produkt_1.text

"""Информация о продукте №2 на странице."""
produkt_2 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_1_title_link']")       # Присваиваем переменной локатор название продукта №2 на странице.
value_produkt_2 = produkt_2.text
print(f"Название продукта №2: {value_produkt_2}")

price_produkt_2 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №2 на странице.
price_value_produkt_2 = price_produkt_2.text

"""Информация о продукте №3 на странице."""
produkt_3 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_2_title_link']")       # Присваиваем переменной локатор название продукта №3 на странице.
value_produkt_3 = produkt_3.text
print(f"Название продукта №3: {value_produkt_3}")

price_produkt_3 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №1 на странице.
price_value_produkt_3 = price_produkt_3.text

"""Информация о продукте №4 на странице."""
produkt_4 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_3_title_link']")       # Присваиваем переменной локатор название продукта №4 на странице.
value_produkt_4 = produkt_4.text
print(f"Название продукта №4: {value_produkt_4}")

price_produkt_4 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №1 на странице.
price_value_produkt_4 = price_produkt_4.text

"""Информация о продукте №5 на странице."""
produkt_5 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_4_title_link']")       # Присваиваем переменной локатор название продукта №5 на странице.
value_produkt_5 = produkt_5.text
print(f"Название продукта №5: {value_produkt_5}")

price_produkt_5 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №1 на странице.
price_value_produkt_5 = price_produkt_5.text

"""Информация о продукте №6 на странице."""
produkt_6 = driver_g.find_element(
    By.XPATH, "//a[@id = 'item_0_title_link']")       # Присваиваем переменной локатор название продукта №6 на странице.
value_produkt_6 = produkt_6.text
print(f"Название продукта №6: {value_produkt_6}")

price_produkt_6 = driver_g.find_element(
    By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")  # Присваиваем переменной локатор цена продукта №1 на странице.
price_value_produkt_6 = price_produkt_6.text

# Формируем Список из продуктов магазина, заполняем его при помощи цикла.
list_product = []
for var in [value_produkt_1, value_produkt_2, value_produkt_3, value_produkt_4, value_produkt_5, value_produkt_6]:
    list_product.append(var)    # Зачем формировать список пока не понятно.

print("Список после добавления новых элементов:", list_product)

list_prise = []
for var in [price_value_produkt_1, price_value_produkt_2, price_value_produkt_3, price_value_produkt_4, price_value_produkt_5, price_value_produkt_6]:
    list_prise.append(var)    # Зачем формировать список пока не понятно.

# Создаём словарь Название продукта и его цена.
prod_prise = {list_product[i]: list_prise[i] for i in range(len(list_product))}
print(prod_prise)

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
# print(list_product)
answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4", "Ответ 5"]
"""Цикл выбора пользователем проверки продукта
С отработкой ввода только цифр, запрета ввода букв"""
while True:
    # До какого числа считаем количестов элементов в списке.
    number = input(f"Выберите продукт введя число от 1 до {len(list_product)}")

    try:
        index = int(number) - 1
        # Количесвто выбора цифр зависит от количесва элементов с списке товаров.
        if 0 <= index < len(list_product):
            # Забираем из списка название роодукта и его цену из списка цен.
            print(
                f"Вы выбрали {list_product[index]}, его цена: {list_prise[index]}")
              # Находим все кнопки add to card
            button_add_card = driver_g.find_elements(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
    #         if len(button_add_card) >= 6:
    #             button_add_card[index].click()
    # # нажмет на четвертую кнопку (элемент списка с индексом 3)
    #         else:
    #             print("Not enough buttons found")
    # выведет сообщение, если на странице меньше 4-х кнопок
            list_elem = len(button_add_card)    #Количестово кнопк добавть в корзину  на странице
            print(f"Количестов кнопок на станице {list_elem}")
            # if len(button_add_card) == 6:
            #     button_add_card[number].click()     # Кликаем на кнопку товара номер которого ввели с клавиатуры
            # Тут запускается функция - добавления в карзину
            #                         - Чек Апп
            #                         -
            # Для того товара которого выбрал пользователь.
            break  # выходим из цикла, если пользователь ввел правильное число
        else:
            print(f"Вы ввели число {number}, которого нет в списке")
    except ValueError:
        print("Вы ввели не число")

print("Test Over")
