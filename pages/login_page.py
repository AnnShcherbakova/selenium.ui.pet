# Импортируем модуль 'time', который позволяет управлять временем в коде
import time
# Импортируем класс 'BasePage' из файла 'base_page'
from .base_page import BasePage
# Импортируем класс 'LoginPageLocators' из файла 'locators'
from .locators import LoginPageLocators

# Создаем класс 'LoginPage', который наследует функциональность от класса 'BasePage'
class LoginPage(BasePage):
    # Определяем метод 'go_to_login' для перехода к вводу email на странице входа
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)# Ищем элемент для ввода email на
        # странице с помощью локатора 'LOGIN_EMAIL' из 'LoginPageLocators'
        login_email.send_keys("mypet@gmail.com")# Вводим "www.anuyta@mail.ru" в найденное поле ввода

    # Определяем метод 'go_to_password' для перехода к вводу пароля на странице входа
    def go_to_password(self):
        password_email = self.browser.find_element(*LoginPageLocators.LOGIN_PASS) # Ищем элемент для ввода пароля на
        # странице с помощью локатора 'LOGIN_PASS' из 'LoginPageLocators'
        password_email.send_keys("987654321pet") # Вводим "987654321qaqa" в найденное поле ввода пароля

    # Определяем метод 'go_to_button' для нажатия на кнопку входа на странице входа.
    def go_to_button(self):
        # Ищем элемент кнопки на странице с помощью локатора 'LOGIN_BTN' из 'LoginPageLocators'
        button_email = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)# Ищем элемент кнопки на странице с помощью
        # локатора 'LOGIN_BTN' из 'LoginPageLocators'
        button_email.submit() # локатора 'LOGIN_BTN' из 'LoginPageLocators'
        # Нажимаем на найденную кнопку
        time.sleep(5)# Ожидаем 5 секунд, чтобы дать странице время выполнить какие-либо действия
