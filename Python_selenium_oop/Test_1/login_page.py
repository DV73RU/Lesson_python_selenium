"""
Авторизация на сайте
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс авторизации на сайте.
    """
    def __init__(self, driver):
        self.error_message = None
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_credentials(self, login, password):
        """
        Метод ввода логина и пароля
        """

        login_input = self.wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        login_input.clear()     # Очистка поля ввода login
        login_input.send_keys(login)    # Вод в поле ввода login значение переменной
        print(f"В поле login введено: {login}")

        password_input = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        password_input.clear()      # Очистка поля password ввода
        password_input.send_keys(password)  # Вод в поле ввода password значение переменной
        print(f"В поле password введено: {password}")

    def err_text(self):
        """
        Метод проверки error сообщений при авторизации.
        """
        error_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test = 'error']")))
        return error_message.text

    def click_login_button(self):
        """
        Метод нажатия на кнопку авторизации
        """
        submit_button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
        submit_button.click()
        print("Нажата кнопка Login")
