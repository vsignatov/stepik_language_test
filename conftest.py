import pytest
from selenium import webdriver

# Ввод в консоли сокращенного наименования языка
def pytest_add_langeuage(parser):
    parser.addoption('--language', action='store', default=ru, help="Введите сокращенное название языка")
 
#запуск браузера с добавлением параметра языка 
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()