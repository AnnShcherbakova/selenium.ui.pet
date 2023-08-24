 # Импортируем класс 'BasePage' из файла 'base_page'.
from .base_page import BasePage
 # Импортируем инструмент 'By' для поиска элементов на веб-странице
 # Импортируем класс 'MainPageLocators' из файла 'locators'
from .locators import MainPageLocators


# Создаем класс 'MainPage', который наследует функциональность от класса 'BasePage'
class MainPage(BasePage):
    # Определяем метод 'go_to_login_page' для перехода на страницу входа
    def go_to_login_page(self):  # Определяем метод 'go_to_login_page' для перехода на страницу входа
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # Находим элемент ссылки для входа
        # на главной странице
        # с помощью локатора 'LOGIN_LINK' из 'MainPageLocators'.
        login_link.click()  #Нажимаем на найденную ссылку.


