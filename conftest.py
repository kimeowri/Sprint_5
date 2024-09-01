import pytest
from selenium import webdriver
from locators import MainPageLocators, AuthorizationPageLocators
from urls import URLS
from data import User

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.BASE_URL)
    driver.find_element(*MainPageLocators.personal_account_btn).click()
    driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
    driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
    driver.find_element(*AuthorizationPageLocators.login_account_btn).click()
