from colorama import deinit

from urls import URLS
from locators import MainPageLocators
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestConstructorSection:

    def test_switch_to_bread_in_constructor_success(self,driver):
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.list_sauces))
        driver.find_element(*MainPageLocators.list_sauces).click()
        driver.find_element(*MainPageLocators.list_bread).click()

        assert driver.find_element(*MainPageLocators.active_list_in_constructor).text == 'Булки'

    def test_switch_to_sauces_in_constructor_success(self,driver):
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.list_sauces))
        driver.find_element(*MainPageLocators.list_sauces).click()

        assert driver.find_element(*MainPageLocators.active_list_in_constructor).text == 'Соусы'

    def test_switch_to_topping_in_constructor_success(self,driver):
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver,15).until(ec.visibility_of_element_located(MainPageLocators.list_topping))
        driver.find_element(*MainPageLocators.list_topping).click()

        assert driver.find_element(*MainPageLocators.active_list_in_constructor).text == 'Начинки'
