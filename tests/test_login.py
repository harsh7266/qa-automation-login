""" from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    assert "secure" in driver.current_url

    driver.quit() """

from pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")

    assert "secure" in driver.current_url


def test_invalid_login_wrong_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "wrong123")

    error = login.get_error_message()
    assert "password" in error.lower()


def test_invalid_login_wrong_username(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wronguser", "SuperSecretPassword!")

    error = login.get_error_message()
    assert "username" in error.lower()


def test_empty_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("", "")

    error = login.get_error_message()
    assert "invalid" in error.lower()

    