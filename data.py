from random import randint

class User:
    user_name = 'qa-mesto_rula_10'
    email = 'qa-mesto_rula_10@gmail.com'
    password = 'qa-mesto_rula_10'

class RandomUser:
    user_name = f'testqa{randint(0, 999)}'
    email = f'testqa{randint(0, 999)}@gmail.com'
    password = f'pass{randint(0,999)}word'
