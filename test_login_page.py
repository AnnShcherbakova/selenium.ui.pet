# Импортируем класс LoginPage из файла pages.login_page
from pages.login_page import LoginPage



# Определяем тестовую функцию с именем test_go_to_login, которая принимает фикстуру browser

def test_go_to_login(browser):

    link = "http://34.141.58.52:8080/#/login"  # Задаем ссылку на веб-страницу, на которую хотим перейти
    page = LoginPage(browser, link)  # Создаем экземпляр класса LoginPage, передавая ему браузер и ссылку
    page.open()  # Открываем страницу по заданной ссылке.

    page.go_to_login()   # Вызываем метод go_to_login() на объекте page, чтобы перейти к вводу email

    page.go_to_password()  # Вызываем метод go_to_password() на объекте page, чтобы перейти к вводу пароля

    page.go_to_button()  # Вызываем метод go_to_button() на объекте page, чтобы выполнить нажатие на кнопку входа

    browser.save_screenshot("result6.png")  # Сохраняем снимок экрана браузера в файл "result6.png".
