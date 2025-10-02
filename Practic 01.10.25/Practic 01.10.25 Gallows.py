import os

alph_high_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_low_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def gallows(string, attempts):
    made_attempts = 0
    opened_symbols = '_' * len(string)
    while made_attempts != attempts:
        made_attempts += 1
        print(f'Осталось {attempts - made_attempts} попытки(ок)')
        print(f'Загаданное слово: {opened_symbols}')
        opened_symbols_list = [i for i in opened_symbols]
        ready_answer = bool(int(input('Введите 0, если не знаете, что это за слово, или любое другое число, если уверены в нём: ')))
        if ready_answer:
            guess = input('Введите предполагаемое слово: ')
            guess = [i for i in guess]
            for i in range(len(guess)):
                if guess[i] in alph_low_ru:
                    guess[i] = alph_high_ru[alph_low_ru.index(guess[i])]
            string = [i for i in string]
            print(f'guess {guess}') #test
            print(f'string {string}')# test
            if guess == string:
                string_list = string
                string = ''
                for i in range(len(string_list)):
                    string += string_list[i]
                print(f'Вы выиграли! Загаданное слово: {string}')
                return print(f'Вы угадали слово за {made_attempts} попытки(ок)')
            else:
                return print(f'Вы не угадали слово {string} за {attempts} попытки(ок)')
        else:
            guess = input('Введите предполагаемую букву: ')
            if len(guess) > 1:
                return print('Необходимо вводить только по одной букве!')
            if guess in alph_low_ru:
                guess = alph_high_ru[alph_low_ru.index(guess)]

            if guess == string or opened_symbols == string:
                string_list = string
                string = ''
                for i in range(len(string_list)):
                    string += string_list[i]
                print(f'Вы выиграли! Загаданное слово: {string}')
                return print(f'Вы угадали слово за {made_attempts} попытки(ок)')
            else:
                for i in range(len(string)):
                    if guess in string:
                        if guess == string[i]:
                            opened_symbols_list[i] = guess
                opened_symbols = ''
                for i in range(len(opened_symbols_list)):
                    opened_symbols += opened_symbols_list[i]
            string = [i for i in string]
            if guess == string or opened_symbols_list == string:
                string_list = string
                string = ''
                for i in range(len(string_list)):
                    string += string_list[i]
                print(f'Вы выиграли! Загаданное слово: {string}')
                return print(f'Вы угадали слово за {made_attempts} попытки(ок)')
        string_list = string
        string = ''
        for i in range(len(string_list)):
            string += string_list[i]
    print(f'guess {opened_symbols}') #test
    print(f'guess {opened_symbols_list}') #test
    print(f'string {string}')# test
    return print(f'Вы не угадали слово {string} за {attempts} попытки(ок)')

string = input('Введите загаданное слово: ')
for i in range(len(string)):
    if string[i] in alph_low_ru:
        string = string.replace(string[i], alph_high_ru[alph_low_ru.index(string[i])])
string = [i for i in string]
attempts = int(input('Введите количество попыток на угадывание этого слова: '))
os.system('cls' if os.name == 'nt' else 'clear') #взял из гугла для того, чтобы не было видно загадываемое слово в терминале
print(f'На угадывание слова из {len(string)} букв выделено {attempts} попытки(ок)')
gallows(string, attempts)
