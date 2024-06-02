ФИНАЛЬНЫЙ ПРОЕКТ 5-ГО СПРИНТА
Автотесты для сервиса https://stellarburgers.nomoreparties.site/
Браузер: Google Chrome

~ Тесты (по порядку) ~

    Регистрация пользователя (test_registration_page.py):
# Регистрация с валидными данными (требования см. в условиях задачи)
1. test_registration_with_correct_credential
# Регистрация с невалидными данными
2. test_registration_with_a_passwd_less_than_six_chars_lon


    Авторизация пользователя (test_login_page.py):
# Авторизация через личный кабинет
1. test_login_in_service_via_personal_account
# Авторизация через кнопку "Войти в аккаунт"
2. test_login_in_service_by_button_on_site_page
# Авторизация через страницу регистрации 
3. test_login_from_registration_page
# Авторизация через восстановление пароля
4. test_login_from_forgot_password_page


    Переход по страницам (test_site_redirect.py):
# Переход в личный кабинет
1. test_redirect_from_site_to_account_profile
# Переход в Конструктор
2. test_redirect_from_personal_account_page_on_builder
# Переход по нажатию на лого Stellar Burgers
3. test_redirect_from_personal_account_page_on_builder_via_logo


    Переход к разделам (test_other_tabs.py):
# Раздел "Булки"
1. test_breads
# Раздел "Соусы"
2. test_sauce
# Раздел "Начинки"
3. test_topping


    Выход из аккаунта (test_logout.py):
# Выход из аккаунта
1. test_logout_from_site

~ Дополнительные файлы ~

### Conftest
Фикстуры для работы тестов

### Data
Данные для тестирования регистрации и авторизации

### Locators
Информация о локаторах, используемых в проекте

### Site_map
Информация о карте сайта
