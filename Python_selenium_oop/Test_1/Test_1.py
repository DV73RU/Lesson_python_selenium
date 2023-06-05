"""
Смок. Поочередная авторизации трех пользователей
1. Пользователь авторизуется, открывается страница с товароми.
2. Проверка заголовка страница с товарами.
3. Проверка количества товаров на странице.
4. Проверка отсутствия картинки '404' на станице товаров.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from product_page import ProductPage
from parsing import Parsing     # Парсинг пароля и логина.
from login_page import LoginPage
from selenium.common.exceptions import TimeoutException

# Настройки Chrome WebDriver
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-gpu')

# Путь к драйверу Chrome WebDriver
driver_path = 'C:\\Users\Dmitriy\\Python.Selenium_lesson\\Python_selenium\\chromedriver.exe'

# Создание сервиса WebDriver
service = Service(driver_path)

# Создание экземпляра Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Открытие страницы авторизации
driver.get('https://www.saucedemo.com/')

# Создание экземпляра класса Parsing и получение списка логинов и пароля.
list_login = Parsing(driver)
login_names = list_login.parsing_login()
password = list_login.parsing_password()

# Создание экземпляра LoginPage
login_page = LoginPage(driver)
# Итерация по списку логинов
print("Старт теста")
for login_name in login_names:
    login_page.enter_credentials(login_name, password)  # Водим спаренные логин и пароль.
    login_page.click_login_button()     # Нажатиe кнопки Login
    try:
        # Добавить обработку логики после успешной авторизации
        # Проверка наличия заголовка на странице товаров после входа.

        # Ожидание страницы после входа
        wait = WebDriverWait(driver, 10)
        product_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
        assert product_header.text == "Products"

        # Дополнительная логика после успешной авторизации
        print(f'Пользователь {login_name} успешно авторизован')
        product_pages = ProductPage(driver)
        product_pages.pars_404_img(login_name)    # Вызываем метод проверки наличия 404 картинки товара.
        logout = product_pages.logout()     # Вызываем метод разлогинивания.
        print(f"Разлогинирование пользователя {login_name} ")
        print("----------------------------------------------")
    except TimeoutException:
        print(f'Ошибка при авторизации пользователя {login_name}')
        print("Обработка ошибки. Страница с продуктами не доступна.")
        error_message = login_page.err_text() #
        print(f"Текст ошибки: {error_message}")  # Выводим сообщение со странице авторизации.

    except AssertionError:
        print(f'Ошибка при авторизации пользователя {login_name}')
        try:
            error_message = login_page.err_text()
            print(f"Текст ошибки: {error_message}")
        except Exception as e:
            print(f"Не удалось получить текст ошибки: {str(e)}")
        print("Обработка ошибки. Дополнительные действия при несоответствии заголовка")






print("Тест пройден")
# Закрытие браузера
driver.quit()
