"""Smoke testing https://www.saucedemo.com/
Проверка подсчёта итоговой суммы к оплате товара.
Выбор проверяемого товара через консоль"""

# 1.Проверка ожидаемой url страници авторизации.
# 2. Авторизация на странице.
# 3. Проверка ожидаемой url страницы с товарами.
# 3.1 Парсинг название продуктов на странице и их цены.
# 3.2 Вывести название продуктов, их цену и присвоить им порядковые номера
# 4. Добавить продукт в корзину выбором номера товара введя присвоенный номер через клавиатуру.
# 4.1 Вывести название выбранного прудукта и его цену.
# 4.2 Добавть выбранный продукт в корзину.
# 5. Проверка количество добавленного продукта в корзине.
# 5.1 Перейти в корзину.
# 5.2 Проверить ожидаемый URL корзины.
# 6. Проверка названия выбранного продукта с названием добавленного продукта в корзине.
# 7. Проверка цены выбранного продукта с ценой добавленного продукта в корзине.
# 7.1 Перейти на страницу checkout.
# 7.3 Проверка ожидаемой URL checkout страници.
# 7.4 Ввод данных пользователя на странице "checkout" Первый этап.
# 7.5 Перейти на второй этап "checkout".
# 8.1 Проверка название выбранного продукта товара на странице "checkout".
# 8.2 Проверка цены выбранного продукта с ценой добавленного продукта "checkout"
# 9. Проверка ожидаемой URL checkout страници второго этапа "checkout".
# 9.1  Проверка название выбранного продукта с названием продукта на втром этапе checkout.
# 9.2 Проверка цены выбранного продукта с ценой добавленного продукта "checkout"
# 10. Проврека итоговой суммы на отбражаемой на странице checkout с фактической суммой прдукта и доп. расходов.

from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import datetime
import time

"""Данные для авторизации"""
login = "standard_user"     # Присваиваем переменной значение логина.
password = "secret_sauce"   # Присваиваемм переменной значение пароля.

"""Данные для заполнения формы о пользователе checkout."""
first = "Dmitriy"
last = "Barsukov"
zip_code = "433734"

"""Ожидаемые URL"""

base_url = 'https://www.saucedemo.com/'  # URL стариницы авторизации.
url_products = 'https://www.saucedemo.com/inventory.html'  # URL старницы товаров.
url_card = 'https://www.saucedemo.com/cart.html'    # URL страницы Your Cart.
url_checkout = 'https://www.saucedemo.com/checkout-step-one.html'   # URL страницы checkout ввода данных пользователя.
url_checkout_2 = 'https://www.saucedemo.com/checkout-step-two.html' # URL страницы checkout Overview.


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


"""Создаём уникальное имя файла скриншётов с текущей датой и временем"""

now = datetime.datetime.now()
scr_filename = "screenshot_{}.png".format(now.strftime("%Y-%m-%d_%H-%M-%S"))

driver_g.get(base_url)
driver_g.maximize_window()


username_input = driver_g.find_element(By.ID, 'user-name')  # Присваиваем значение переменной локатор поля ввода username.
password_input = driver_g.find_element(By.ID, 'password')   # Локатор кнопки "Login".
submit_button = driver_g.find_element(By.ID, 'login-button')    # Водим в поле ввода значение переменой login.
username_input.send_keys(login)
print(f"Введён логин: {login}")   # Выводим сообщение о введённом login
password_input.send_keys(password)
print(f"Введён пароль: {password}")
submit_button.click()  # Кликаем на кенопку Login.
print("Нажата кнопка 'Login'")

# Проверяем, успешность авторизации и находимся на странице продуктов.
try:
    wait = WebDriverWait(driver_g, 10)
    # Проверяем URL
    if url_products not in driver_g.current_url:
        raise Exception(
            f"URL не соотвествует: {driver_g.current_url} ожидаемому")
    # Проверяем наличие элемента "Products"
    # Локатор заголовка страницы.
    product_list_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
    assert product_list_header.text == "Products"
    print("Перешли на страницу с продуктами.")
except Exception as e:
    # Выводим сохраненную информацию об ошибке в переменной e.
    print(f"Error: {str(e)}")
    driver_g.save_screenshot(scr_filename)  # Создаём файл скриншёта.

# Получаем список продуктов и их цены
products = driver_g.find_elements(
    By.XPATH, "//div[@class='inventory_item_name']")    # Присваиваем значение переменной локатор название продуктов.
prices = driver_g.find_elements(
    By.XPATH, "//div[@class='inventory_item_price']")   # Присваиваем значение переменной локаторов цен продуктов.

# Выводим список продуктов с их ценами и порядковыми номерами.
print("Список продуктов на странице 'Products':")
if len(products) == 0:  # Проверка наличие на страницы продуктов.
    print("Товаров на странице нет.")
else:
    for i in range(len(products)):
        # Печатаем название, цену и присваиваем порядковый номер продукта.
        print(f"{i+1}. {products[i].text} - {prices[i].text}")
    print(f"Количество продуктов: {len(products)} шт.")

# TODO Написать функию. Есть ли продукты без цены или цены без названия продукта.

# Запрашиваем у пользователя номер товара для добавления в корзину.
while True:
    try:
        product_num = int(
            input("Введите порядковый номер продукта для добавления в корзину: "))
        if product_num < 1 or product_num > len(products):
            raise ValueError
        break
    # Обработка ошибки, от ввода цисла отличного от количества товара на странице.
    except ValueError:
        print(f"Номер должен быть от 1 до {len(products)}")

product_name = products[int(product_num)-1].text
product_price = prices[int(product_num)-1].text

print(f'Вы добавили {product_name} в корзину. Его цена: {product_price}')

# Выбираем и добавляем выбранный товар в корзину
add_to_cart_button = driver_g.find_elements(
    By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")  # Локаторы всех кнопок 'Add to cart'
# Нажимаем на кнопку 'Add to cart' у выбранного товара(-1 так как индексы начин. с 0)
add_to_cart_button[product_num-1].click()

# Переходим в корзину и проверим ожидаемый URL
# Локатор иконки количества товара в корзине.
view_cart_button = driver_g.find_element(
    By.XPATH, '//span[@class="shopping_cart_badge"]')
cart_count = view_cart_button.text
print(f"Количество добавленого товара в корзине {cart_count}")
view_cart_button.click()    # Клик на кнопку корзины
print("Нажата кнопка 'Корзина'")

try:
    wait = WebDriverWait(driver_g, 10)
    # Проверяем URL
    if url_card not in driver_g.current_url:
        raise Exception(
            f"URL не соотвествует: {driver_g.current_url} ожидаемому")
    # Проверяем наличие элемента "Your Cart"
    card_list_header = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='title']")))   # Локатор заголовка страницы
    assert card_list_header.text == "Your Cart"
    print("Перешли в 'Корзину'")
except Exception as m:
    # Выводим сохраненную информацию об ошибке в переменной m.
    print(f"Error: {str(m)}")
    driver_g.save_screenshot(scr_filename)  # Создаём файл скриншёта

# Проверяем, что название продукта на странице корзины совпадает с выбранным названием продукта.
try:
    product_title_cart_page = driver_g.find_element(
        By.XPATH, '//div[@class="inventory_item_name"]')    # Локатор название продукта вкорзине
    if product_title_cart_page.text == product_name:
        print("Название продукта на странице корзины совпадает с выбранным названием продукта.")
    else:
        print("Ошибка: название продукта на странице корзины не совпадает с выбранным названием продукта.")
except NoSuchElementException:
    print("Ошибка: элемент не найден на странице.")

# Проверяем, что цена продукта на странице корзины совпадает с ценой выбранного продукта.
try:
    product_price_cart_page = driver_g.find_element(
        By.XPATH, '//div[@class="inventory_item_price"]')   # Локатор цены продукта вкорзине
    if product_price_cart_page.text == product_price:
        print("Цена продукта на странице корзины совпадает с ценой выбранным продуктом.")
    else:
        print("Ошибка: Цена продукта на странице корзины не совпадает с ценой выбранного продукта.")
except NoSuchElementException:
    print("Ошибка: элемент не найден на странице.")


# 7.1 Перейдем на страницу оформления заказа и проверим ожидаемый URL
# Локатор кнопки checkout.
checkout_button = driver_g.find_element(
    By.XPATH, '//button[@class="btn btn_action btn_medium checkout_button"]')
checkout_button.click()  # Кликаем на кнопку checkout.

try:
    wait = WebDriverWait(driver_g, 10)
    # Проверяем URL
    if url_checkout not in driver_g.current_url:
        raise Exception(
            f"URL не соотвествует: {driver_g.current_url} ожидаемому")
    # Проверяем наличие элемента "Your Information"
    information_list_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
    assert information_list_header.text == "Checkout: Your Information"
    print("Перешли на страницу 'Checkout: Your Information'")
except Exception as e:
    # Выводим сохраненную информацию об ошибке в переменной e.
    print(f"Error: {str(e)}")
    driver_g.save_screenshot(scr_filename)  # Создаём файл скриншёта

# 7.2 Заполним данные пользователя на странице оформления заказа и перейдем к второму шагу.
first_name_input = driver_g.find_element(
    By.XPATH, "//input[@id = 'first-name']")
last_name_input = driver_g.find_element(By.XPATH, "//input[@id = 'last-name']")
postal_code_input = driver_g.find_element(
    By.XPATH, "//input[@id = 'postal-code']")
first_name_input.send_keys(first)
print(f"В поле ввода 'First Name' введено: {first}")
last_name_input.send_keys(last)
print(f"В поле ввода 'Last Name' введено: {last}")
postal_code_input.send_keys(zip_code)
print(f"В поле ввода 'Zip/Postal Code' введено: {zip_code}")
time.sleep(2)

# 7.1 Перейдем на страницу Checkout: Overview оформления заказа и проверим ожидаемый URL
# Локатор кнопки checkout.
checkout_button = driver_g.find_element(
    By.XPATH, '//input[@class="submit-button btn btn_primary cart_button btn_action"]')
checkout_button.click()  # Кликаем на кнопку Continue.
print("Нажата кнопка 'Continue'")
try:
    wait = WebDriverWait(driver_g, 10)
    # Проверяем URL
    if url_checkout_2 not in driver_g.current_url:
        raise Exception(
            f"URL не соотвествует: {driver_g.current_url} ожидаемому")
    # Проверяем наличие элемента "Continue"
    checkout_2_header = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='title']")))
    assert checkout_2_header.text == "Checkout: Overview"
    print("Перешли на страницу Checkout: Overview")
except Exception as e:
    # Выводим сохраненную информацию об ошибке в переменной e.
    print(f"Error: {str(e)}")
    driver_g.save_screenshot(scr_filename)  # Создаём файл скриншёта
time.sleep(1)


# Проверяем, что название продукта на странице Checkout: Overview: совпадает с выбранным названием продукта.
try:
    product_title_overview_page = driver_g.find_element(
        By.XPATH, '//div[@class="inventory_item_name"]')
    if product_title_overview_page.text == product_name:
        print("Название продукта на странице Checkout: Overview: совпадает с выбранным названием продукта.")
    else:
        print("Ошибка: название продукта на странице Checkout: Overview: не совпадает с выбранным названием продукта.")
except NoSuchElementException:
    print("Ошибка: элемент не найден на странице Checkout: Overview:.")

# Проверяем, что цена продукта на странице Checkout совпадает с ценой выбранного продукта.
try:
    product_price_overview_page = driver_g.find_element(
        By.XPATH, '//div[@class="inventory_item_price"]')
    if product_price_overview_page.text == product_price:
        print("Цена продукта на странице Checkout совпадает с ценой выбранным продуктом.")
    else:
        print("Ошибка: Цена продукта на странице Checkout не совпадает с ценой выбранного продукта.")
except NoSuchElementException:
    print("Ошибка: элемент не найден на странице.")

# Проверяем цену продукта на ст. Checkout и в поле Item total:
total_price_overview_page = driver_g.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")    # Локатор итоговой суммы на странице Checkout.
value = total_price_overview_page.text.split(": ")[-1][1:]  #  разбиваем текст на части с помощью метода split и выбираем последнюю часть, убираем знак $
# print(f"Сумма на сайте Total: {value}")

# Проверяем цену продукта на ст. Checkout и в поле Item total:
try:
    subtotal_label_price = driver_g.find_element(
        By.XPATH, "//div[@class='summary_subtotal_label']")   # Локатор цены в поле Item total
    value_subtotal_label_price = subtotal_label_price.text.split(": ")[-1][1:]
    if value_subtotal_label_price == product_price[1:]:
        print("Цена продукта на странице Checkout совпадает с ценой в поле Item total.")
    else:
        print("Ошибка: Цена продукта на странице Checkout не совпадает с ценой в поле Item total.")
except NoSuchElementException:
    print("Ошибка: элемент не найден на странице.")

# Проверяем фактическую сумму.
# Локатор Tax: продукта на странице.
tax_overview_page = driver_g.find_element(
    By.XPATH, "//div[@class='summary_tax_label']")
# разбиваем текст на части с помощью метода split и выбираем последнюю часть, убираем знак $
tax_overview_price = tax_overview_page.text.split(": ")[-1][1:]
# Cкладываем значение тз Item total с значением Tax.
samm = float(value_subtotal_label_price) + float(tax_overview_price)
print(f"Цена записанная в поле Item total равна: {value}")
print(f"Цена Tax:  {tax_overview_price}")
print(f"Cкалькулированная сумма тах + прайс равна: {samm}")

try:
    if float(samm) == float(value):
        print(f"Общая фактическая сумма {samm} за товара совпадает с ценой {value} в поле Total.")
    else:
        print(f"Ошибка: Общая фактическая сумма {samm} за товара не совпадает с ценой {value} в поле Total.")
except Exception as e:
    # Выводим сохраненную информацию об ошибке в переменной e.
    print(f"Error: {str(e)}")
    driver_g.save_screenshot(scr_filename)  # Создаём файл скриншёта

driver_g.quit()
