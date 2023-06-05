from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список логинов
login_names = ['standard_user', 'problem_user', 'performance_glitch_user']

# Общий пароль
password = 'secret_sauce'
# Настройки Chrome WebDriver
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-gpu')

# Путь к драйверу Chrome WebDriver
driver_path = 'C:\\path\\to\\chromedriver.exe'

# Создание сервиса WebDriver
service = Service(driver_path)

# Создание экземпляра Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Открытие страницы авторизации
driver.get('https://www.saucedemo.com/')

# Итерация по списку логинов
for login_name in login_names:
    # Ожидание поля ввода логина
    login_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'user-name')))

    # Очистка поля ввода логина и ввод логина
    login_input.clear()
    login_input.send_keys(login_name)

    # Ожидание поля ввода пароля
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))

    # Очистка поля ввода пароля и ввод пароля
    password_input.clear()
    password_input.send_keys(password)

    # Отправка формы
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'login-button')))
    submit_button.click()

    # Добавить обработку логики после успешной авторизации
    # Например, проверка наличия элемента на странице после входа

    # Ожидание страницы после входа
    WebDriverWait(driver, 10).until(EC.url_contains('https://www.saucedemo.com/inventory.html'))

    # Дополнительная логика после успешной авторизации
    print(f'Пользователь {login_name} успешно авторизован')

# Закрытие браузера
driver.quit()