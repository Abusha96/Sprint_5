from locators import *
from data import *
from site_map import *
from selenium.webdriver.common.by import By


class TestLogout:
    # Авторизация, затем дальнейший выход из ЛК
    def test_logout_from_site(self, driver):
        # Авторизация
        driver.implicitly_wait(10)
        driver.get(site_login_page)
        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()
        # Переход в личный кабинет
        driver.find_element(By.XPATH, site_from_home_site_to_personal_account_redirect_button).click()
        # Выход
        driver.find_element(By.XPATH, exit_button).click()
        assert driver.find_element(By.XPATH, login_page_submit_button).is_displayed()
