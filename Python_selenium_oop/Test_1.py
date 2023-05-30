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


class Test_1:  # Класс тестирование выбора продукта в корзину.

    def test_select_product(self):  # Метод открытия главное странице
        g = Service('C:\\Users\Dmitriy\\Python.Selenium_lesson\\Python_selenium\\chromedriver.exe')
        driver_g = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'  # начальный  url

        driver_g.get(base_url)  # Используем метод get для открытия url
        driver_g.maximize_window()  # Открываем окно на максимум
        print("Старт теста")

        login = "standard_user"  # Присваиваем переменной значение логина.
        password_all = "secret_sauce"  # Присваиваем переменной значение пароля.

        # Присваиваем переменной значение локатора поля ввода логин.
        user_name = driver_g.find_element(By.ID, 'user-name')
        user_name.send_keys(login)  # Вставляем в поле логин значение логина.
        print('Ввод логин')
        time.sleep(2)

        # Локатор поля ввода пароля
        password = driver_g.find_element(By.ID, 'password')
        password.send_keys(password_all)  # Ввод пароля.
        print('Ввод пароля')
        time.sleep(2)

        # Локатор кнопки авторизации.
        button_login = driver_g.find_element(By.ID, 'login-button')
        button_login.click()
        print('Клик кнопки авторизации')
        time.sleep(2)


test = Test_1()  # Экземпляр класса.

test.test_select_product()  # Обращение к примерной test и вызываем метод test_select_product
