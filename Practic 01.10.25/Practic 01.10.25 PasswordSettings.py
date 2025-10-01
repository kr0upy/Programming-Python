import random
import string

alph_low_eng = 'abcdefghijklmnoparstuvwxyz'
alph_high_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password_length = abs(int(input('Введите желаемую длину пароля: ')))
is_low_letters = bool(int(input('Нужно ли наличие строчных букв в пароле? Введите 1 - если да, 0 - если нет: ')))
is_high_letters = bool(int(input('Нужно ли наличие заглавных букв в пароле? Введите 1 - если да, 0 - если нет: ')))
is_symbols = bool(int(input('Нужно ли наличие специальных символов в пароле? Введите 1 - если да, 0 - если нет: ')))
is_digits = bool(int(input('Нужно ли наличие цифр в пароле? Введите 1 - если да, 0 - если нет: ')))
print(is_low_letters)
def password_create(password_length, is_low_letters, is_high_letters, is_symbols, is_digits):
    password = ''
    password_symbols = []
    letters_high = ''.join(random.choice(alph_high_eng) for i in range(password_length) if is_high_letters)
    letters_low = ''.join(random.choice(alph_low_eng) for i in range(password_length) if is_low_letters)
    digits = ''.join(random.choice(string.digits) for i in range(password_length) if is_digits)
    symbols = ''.join(random.choice('!@#$%^&*') for i in range(password_length) if is_symbols)
    if is_high_letters:
        password_symbols.append(letters_high)
    if is_low_letters:
        password_symbols.append(letters_low)
    if is_digits:
        password_symbols.append(digits)
    if is_symbols:
        password_symbols.append(symbols)
    while len(password) < password_length:
        password += random.choice(random.choice(password_symbols))
    print(password)
password_create(password_length, is_low_letters, is_high_letters, is_symbols, is_digits)

