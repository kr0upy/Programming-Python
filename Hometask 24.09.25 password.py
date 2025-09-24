import random
import string
password_length = int(input('Введите длину пароля: '))
password = ''
letters = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
numbers = ''.join(str(random.choice(string.digits) for i in range(3)))
symbols = ''.join(random.choice('!@#$%^&*') for i in range(3))
for i in range(0, password_length):
    password += random.choice([letters[random.choice([0, 1, 2])], numbers[random.choice([0, 1, 2])], symbols[random.choice([0, 1, 2])]])
print('Ваш пароль:',password)