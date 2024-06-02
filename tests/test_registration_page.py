from locators import *
from data import *
from site_map import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    # Регистрация с валидными данными
    def test_registration_with_correct_credential(self, driver):
        driver.get(site_registration_page)
        driver.find_element(By.XPATH, registation_page_name_input).send_keys(registration_name)
        driver.find_element(By.XPATH, registation_page_email_input).send_keys(email_generator())
        driver.find_element(By.XPATH, registation_page_password_input).send_keys(registration_pass)
        driver.find_element(By.XPATH, registration_page_submit_button).click()

        # Задаем ожидание
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, page_login_registation_button)))

        # Получаем значение элемента кнопки
        check_button = driver.find_element(By.XPATH, page_login_registation_button).text

        # Проверяем что значение кнопки соответствует ожидаемому результату
        assert check_button == 'Зарегистрироваться'

    # Регистрация с невалидными данными (длина пароля < 6 символов)
    def test_registration_with_a_passwd_less_than_six_symbols(self, driver):
        driver.get(site_registration_page)
        driver.find_element(By.XPATH, registation_page_name_input).send_keys(registration_name)
        driver.find_element(By.XPATH, registation_page_email_input).send_keys(email_generator())
        driver.find_element(By.XPATH, registation_page_password_input).send_keys(registration_wrong_pass)
        driver.find_element(By.XPATH, registration_page_submit_button).click()

        # Получаем значение из элемента оповещения о некорректном пароле
        attention = driver.find_element(By.XPATH, wrong_pass_attention).text

        # Проверяем что полученное значение соответствует ожидаемому результату
        assert attention == 'Некорректный пароль'
