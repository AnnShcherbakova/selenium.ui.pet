

# Импортируем класс MainPage из файла pages.main_page
from pages.main_page import MainPage



# Определяем тестовую функцию с именем test_go_to_login_page, которая принимает фикстуру browser
def test_go_to_login_page(browser):
    # Задаем ссылку на веб-страницу, на которую хотим перейти.
    link = "http://34.141.58.52:8080/#/" # Задаем ссылку на веб-страницу, на которую хотим перейти
    # Создаем экземпляр класса MainPage, передавая ему браузер и ссылку.
    page = MainPage(browser, link)  # Создаем экземпляр класса MainPage, передавая ему браузер и ссылку
    page.open() # Открываем главную страницу по заданной ссылке

    # Вызываем метод go_to_login_page() на объекте page, чтобы перейти на страницу входа.
    page.go_to_login_page()  # Вызываем метод go_to_login_page() на объекте page, чтобы перейти на страницу входа

    browser.save_screenshot("result5.png")  # Вызываем метод go_to_login_page() на объекте page,
    # чтобы перейти на страницу входа
