from array import array
from doctest import DocTest

from data import User
from conftest import driver
from locators import MainPageLocators, AuthorizationPageLocators, RegistrationPageLocators, PersonalAccountLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:

    def test_button_log_personal_account_success(self,driver):
        driver.get(URLS.BASE_URL)
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.place_order_btn))
        order_btn = driver.find_element(*MainPageLocators.place_order_btn).text

        assert (driver.current_url == URLS.BASE_URL) and (order_btn == 'Оформить заказ')

    def test_button_log_login_in_to_account_success(self,driver):
        driver.get(URLS.BASE_URL)
        driver.find_element(*MainPageLocators.login_account_btn).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.place_order_btn))
        order_btn = driver.find_element(*MainPageLocators.place_order_btn).text

        assert (driver.current_url == URLS.BASE_URL) and (order_btn == 'Оформить заказ')

    def test_log_using_registration_form_success(self,driver):
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_btn).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(MainPageLocators.place_order_btn))
        order_btn = driver.find_element(*MainPageLocators.place_order_btn).text

        assert (driver.current_url == URLS.BASE_URL) and (order_btn == 'Оформить заказ')

    def test_log_recover_form_success(self,driver):
        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.place_order_btn))
        order_btn = driver.find_element(*MainPageLocators.place_order_btn).text

        assert (driver.current_url == URLS.BASE_URL) and (order_btn == 'Оформить заказ')