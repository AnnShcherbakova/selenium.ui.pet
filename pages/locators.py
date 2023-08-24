# Импортируем из библиотеки selenium специальный инструмент для поиска элементов на веб-странице
from selenium.webdriver.common.by import By

# Создаем класс с именем MainPageLocators
# В этом классе мы определяем различные способы поиска элементов на главной странице веб-сайта
class MainPageLocators:
    # Здесь мы определяем локатор (способ поиска) для ссылки на вход (логин)
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(1) > a > span")

# Создаем класс с именем LoginPageLocators.
# В этом классе мы определяем способы поиска элементов на странице входа (страница логина) веб-сайта
class LoginPageLocators:
    # Здесь мы определяем локаторы для поля ввода email, поля ввода пароля и кнопки входа
    # Каждый локатор представляет собой кортеж с двумя элементами: типом селектора
    # (например, ID или CSS_SELECTOR) и самим селектором.
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
