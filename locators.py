# Страница регистрации .site/registation
registation_page_name_input = './/input[@name="name"]'  # Input для имени
registation_page_email_input = './/label[text()="Email"]/following-sibling::input'  # Input для email
registation_page_password_input = './/input[@name="Пароль"]'  # Input для пароля

registration_page_submit_button = './/button[text()="Зарегистрироваться"]'  # Кнопка подтверждения регистрации
registration_page_login_button = './/a[text()="Войти"]'  # Кнопка "Войти"

# Страница авторизации .site/login
page_login_header = './/h2[text()="Вход"]'  # Заголовок

# Страница регистрация
page_login_registation_button = './/a[text()="Зарегистрироваться"]'  # Кнопка регистрации

# Уведомления
wrong_pass_attention = './/p[text(  )="Некорректный пароль"]'  # Информация о некорректном пароле
text_about_changes_current_data = './/p[text()="В этом разделе вы можете изменить свои персональные данные"]' # Информирование о возможности изменения данных

# Страница восстановления паролья .site/forgot_password
forgot_password_page_login_button = './/a[text()="Войти"]'

# Домашняя страница .site
site_page_login_button = './/button[text()="Войти в аккаунт"]'  # Кнопка входа в ЛК
site_from_home_site_to_personal_account_redirect_button = './/p[text()="Личный Кабинет"]'
order_button = './/button[text()="Оформить заказ"]'  # Кнопка оформления заказа

login_page_submit_button = './/button[text()="Войти"]'  # Кнопка "Войти"

# Страница авторизации
login_page_email_input = './/label[text()="Email"]/following-sibling::input'  # Поле ввода почты
login_page_password_input = './/input[@name="Пароль"]'  # Поле ввода пароля

# Личный кабинет
builder_button = './/p[text()="Конструктор"]'  # Иконка Конструктора
logo_button = 'AppHeader_header__logo__2D0X2'  # Логотип
exit_button = './/button[text()="Выход"]'  # Кнопка выхода из ЛК

# Конструктор
breads = './/span[text()="Булки"]'  # Булки
sauce = './/span[text()="Соусы"]'  # Cоусы
topping = './/span[text()="Начинки"]'  # Начинки

builder_header = './/h1[text()="Соберите бургер"]'  # Заголовок раздела "Конструктор"

# Текущий статус элемента
element_is_active = '//*[contains(@class, "type_current")]'  # Активный элемент
