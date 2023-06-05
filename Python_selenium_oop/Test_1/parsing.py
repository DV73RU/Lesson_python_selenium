from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Parsing():
    """
    Парсинг логинов и пароля размещённых на странице авторизации.
    """

    def __init__(self, driver):
        self.driver = driver

    def parsing_login(self):
        """
        Метод парсинг логинов и передачи их в виде списка
        """
        wait = WebDriverWait(self.driver, 15)
        # Элемент парсинг логины.
        logins_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='login_credentials']")))  #
        # Дожидаемся видимости элемента
        logins = logins_element.text.split('\n')[1:]  # Разделяем по символу новой строки. Удаляем первую строку
        # не относящиеся к значению логина.
        return logins  # Возвращаем значения логинов.

    def parsing_password(self):
        """
        Метод парсинг паролей и передачи их в строку.
        """
        wait = WebDriverWait(self.driver, 15)
        # Элемент парсинг пароль.
        pass_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='login_password']")))
        password = pass_element.text.split(':')[1].strip()  # Разделяем текст, выбираем второй элемент, удаляем
        # пробелы до и после.
        return password  # Возвращаем значение пароля.
