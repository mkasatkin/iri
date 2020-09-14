import pytest
from selenium import webdriver

link = "http://iri-content.dev.htc-cs.ru/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def Author(self):
        browser.get(link)
        email = browser.find_element_by_xpath('//input[@name="email"]')
        email.sendkeys('producer@mail.ru')

        passw = browser.find_element_by_xpath('//input[@name="password"]')
        passw.sendkeys('producer@mail.ru')

        passw = browser.find_element_by_css_selector('button')
        passw.sendkeys('password')
