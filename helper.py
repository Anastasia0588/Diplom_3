import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_user_creds():
    credentials = {'email': generate_random_string(10) + '@yandex.ru',
                   'password': generate_random_string(10),
                   'name': generate_random_string(10)}
    return credentials
