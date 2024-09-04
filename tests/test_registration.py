from dbm import error

from selenium.webdriver.support.expected_conditions import visibility_of
from data import User, RandomUser
from conftest import driver, open_reg_page
from locators import RegistrationPageLocators, AuthorizationPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestRegistrationPage:

    def test_registration_success(self,open_reg_page,driver):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomUser.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(AuthorizationPageLocators.login_account_btn))
        login_button_displayer = driver.find_element(*AuthorizationPageLocators.login_account_btn).is_enabled()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_button_displayer

    def test_registration_with_invalid_password_error(self,open_reg_page,driver):
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys('gfhj')
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(RegistrationPageLocators.error_message_incorrect_password))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REG_PAGE_URL)

    def test_error_message_displayed_duplicate_registration(self,open_reg_page,driver):
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(RegistrationPageLocators.error_message_double_registration))
        error = driver.find_element(*RegistrationPageLocators.error_message_double_registration).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REG_PAGE_URL)