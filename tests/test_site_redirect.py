from locators import *
from data import *
from site_map import *
from selenium.webdriver.common.by import By

class TestRedirect:
    # Переход в личный кабинет после успешной авторизации
    def test_redirect_from_site_to_account_profile(self, driver):
        driver.implicitly_wait(10)
        driver.get(site_login_page)
        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()
        driver.find_element(By.XPATH, site_from_home_site_to_personal_account_redirect_button).click()
        text_on_personal_account_page = 'В этом разделе вы можете изменить свои персональные данные'
        assert text_on_personal_account_page in driver.find_element(By.XPATH, text_about_changes_current_data).text


    # Переход в конструктор после успешной авторизации
    def test_redirect_from_personal_account_page_on_builder(self, driver):
        driver.implicitly_wait(10)
        driver.get(site_login_page)
        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()
        driver.find_element(By.XPATH, site_from_home_site_to_personal_account_redirect_button).click()
        driver.find_element(By.XPATH, builder_button).click()
        check = 'Соберите бургер'
        assert check in driver.find_element(By.XPATH, builder_header).text


    # Переход в конструктор со страницы ЛК по нажатию на логотип
    def test_redirect_from_personal_account_page_on_builder_via_logo(self, driver):
        driver.implicitly_wait(10)
        driver.get(site_login_page)
        driver.find_element(By.XPATH, login_page_email_input).send_keys(login_email)
        driver.find_element(By.XPATH, login_page_password_input).send_keys(login_password)
        driver.find_element(By.XPATH, login_page_submit_button).click()
        driver.find_element(By.XPATH, site_from_home_site_to_personal_account_redirect_button).click()
        driver.find_element(By.CLASS_NAME, logo_button).click()
        check_header = 'Соберите бургер'
        assert check_header in driver.find_element(By.XPATH, builder_header).text
