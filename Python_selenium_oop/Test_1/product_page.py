"""
Парсинг уникальности название продуктов, фотографии на странице
"""
import os
import time
from selenium.webdriver.common.by import By


class ProductPage():

    def __init__(self, driver):
        self.login = None
        self.driver = driver

    def pars_404_img(self, login):
        self.login = login

        products_img = self.driver.find_elements(
            By.XPATH, "//img[@class='inventory_item_img']")
        filename_list = []
        if len(products_img) == 0:  # Проверка наличие на страницы продуктов.
            print(f"У пользователя {login} товары на странице Product не отображаются.")
        else:
            for i in range(len(products_img)):
                # Выводим название картинок продукта.
                img_src = products_img[i].get_attribute("src")
                filename = os.path.basename(img_src)
                filename_list.append(filename)  # Получаем список из названий файлов картинок продуктов.

            # print(filename_list)
            print(f"Количество продуктов: {len(products_img)} шт. на станице пользовотеля {login}")

        img_404 = "sl-404.168b1cce.jpg"
        if img_404 in filename_list:
            print(f"У пользователя {login} на странице продуктов присутствует 404 картинки продукта.")

    def logout(self):
        """Функция разлогинивания"""
        button_menu = self.driver.find_element(
            By.XPATH, "//button[@id = 'react-burger-menu-btn']")
        button_menu.click()
        time.sleep(2)
        button_logout = self.driver.find_element(
            By.XPATH, "//a[@id = 'logout_sidebar_link']")
        button_logout.click()
        time.sleep(2)
