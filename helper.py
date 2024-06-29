# Генерация email
import random
def email_generator():
    random_name = random.choice(['test1_', 'test2_', 'test3_'])
    random_number = random.randint(1, 100)
    random_domain = random.choice(['@yandex.ru', '@gmail.com', '@mail.ru'])
    email = f'{random_name}{random_number}{random_domain}'
    return email
