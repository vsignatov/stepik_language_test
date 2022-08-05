from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

def test_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert( None != button)
    