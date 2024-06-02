import random

registration_name = 'test_testovich'
registration_email = 'kristinaabubakirova9000@yandex.ru'
registration_pass = '123456'
registration_wrong_pass = '12345'

login_email = 'mc_fish@yandex.ru'
login_password = '123456'


# Генерация email
def email_generator():
    random_name = random.choice(['test1_', 'test2_', 'test3_'])
    random_number = random.randint(1, 100)
    random_domain = random.choice(['@yandex.ru', '@gmail.com', '@mail.ru'])
    email = f'{random_name}{random_number}{random_domain}'
    return email
