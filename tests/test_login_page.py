from locators import *
from data import *
from site_map import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginSection:

    # Проверяем авторизацию через личный кабинет на странице /login
    def test_login_in_service_via_personal_account(self, driver):
        check = 'Оформить заказ'

        driver.get(site_login_page)

        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, order_button)))

        assert check in driver.find_element(By.XPATH, order_button).text

    # Вход по кнопке "Войти в аккаунт" на главном сайте .site
    def test_login_in_service_by_button_on_site_page(self, driver):
        check = 'Оформить заказ'

        driver.get(site)
        driver.find_element(By.XPATH, site_page_login_button).click()

        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, order_button)))

        # Проверка того, что элемент на следующей странице прогрузился
        assert check in driver.find_element(By.XPATH, order_button).text

    # Авторизация через страницу регистрации
    def test_login_from_registration_page(self, driver):
        check = 'Оформить заказ'

        driver.get(site_registration_page)
        driver.find_element(By.XPATH, registration_page_login_button).click()

        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, order_button)))

        assert check in driver.find_element(By.XPATH, order_button).text

    # Авторизация через страницу восстановления пароля
    def test_login_from_forgot_password_page(self, driver):
        check = 'Оформить заказ'

        driver.get(site_forgot_password_page)
        driver.find_element(By.XPATH, forgot_password_page_login_button).click()
        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, order_button)))

        assert check in driver.find_element(By.XPATH, order_button).text
