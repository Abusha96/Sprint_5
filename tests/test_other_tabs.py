from locators import *
from site_map import *
from selenium.webdriver.common.by import By


class TestTabs:
    # Переход к разделу "Булки"
    def test_breads(self, driver):
        driver.get(site)
        driver.find_element(By.XPATH, sauce).click()
        driver.find_element(By.XPATH, breads).click()
        assert driver.find_element(By.XPATH, element_is_active).text == driver.find_element(By.XPATH, breads).text

    # Переход к разделу "Соусы"
    def test_sauce(self, driver):
        driver.get(site)
        driver.find_element(By.XPATH, sauce).click()
        assert driver.find_element(By.XPATH, element_is_active).text == driver.find_element(By.XPATH, sauce).text

    # Переход к разделу "Начинки"
    def test_topping(self, driver):
        driver.get(site)
        driver.find_element(By.XPATH, topping).click()
        assert driver.find_element(By.XPATH, element_is_active).text == driver.find_element(By.XPATH, topping).text

