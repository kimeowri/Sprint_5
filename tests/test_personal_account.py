from urls import URLS
from conftest import driver, get_login_driver
from locators import MainPageLocators, PersonalAccountLocators, AuthorizationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalAccount:

    def test_navigation_to_personal_account_from_main_page_success(self,driver,get_login_driver):
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_btn))
        save_button_displayed = driver.find_element(*PersonalAccountLocators.save_btn).is_enabled()

        assert driver.current_url == URLS.PROFILE_PAGE_URL and save_button_displayed

    def test_navigation_from_personal_account_to_constructor_success(self,driver,get_login_driver):
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_btn))
        driver.find_element(*PersonalAccountLocators.constructor_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.place_order_btn))
        order_button = driver.find_element(*MainPageLocators.place_order_btn)

        assert driver.current_url == URLS.BASE_URL and order_button.text == 'Оформить заказ'

    def test_click_through_to_the_constructor_logo_stellar_burgers_success(self,driver,get_login_driver):
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_btn))
        driver.find_element(*PersonalAccountLocators.logo_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_btn))
        order_button = driver.find_element(*MainPageLocators.place_order_btn)

        assert driver.current_url == URLS.BASE_URL and order_button.text == 'Оформить заказ'

    def test_logout_from_personal_account_success(self,driver,get_login_driver):
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_btn))
        driver.find_element(*PersonalAccountLocators.exit_btn).click()
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(AuthorizationPageLocators.login_account_btn))
        login_button = driver.find_element(*AuthorizationPageLocators.login_account_btn)

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_button.text == 'Войти'
