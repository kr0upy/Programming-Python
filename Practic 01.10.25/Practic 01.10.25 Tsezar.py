alph_high_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_low_eng = 'abcdefghijklmnoparstuvwxyz'
alph_high_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_low_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
task = bool(int(input('Введите 0, если хотите декодировать шифр, или любое другое число, если хотите закодировать предложение: ')))

def tsezar_code():
    new_phrase = ''
    phrase = input('Введите предложение, которое вы хотите закодировать: ')
    move_symbol = abs(int(input('Введите сдвиг для шифрования: ')))
    for i in phrase:
        if i in alph_high_eng or i in alph_low_eng:
            if i in alph_high_eng:
                for k in alph_high_eng:
                    if k == i:
                        ind = alph_high_eng.index(k)
                if ind + move_symbol <= len(alph_high_eng):
                    new_phrase += alph_high_eng[ind + move_symbol]
                else:
                    new_phrase += alph_high_eng[(ind + move_symbol) % len(alph_high_eng)]
            else:
                for k in alph_low_eng:
                    if k == i:
                        ind = alph_low_eng.index(k)
                if ind + move_symbol <= len(alph_low_eng):
                    new_phrase += alph_low_eng[ind + move_symbol]
                else:
                    new_phrase += alph_low_eng[(ind + move_symbol) % len(alph_low_eng)]
        elif i in alph_high_ru or i in alph_low_ru:
            if i in alph_high_ru:
                for k in alph_high_ru:
                    if k == i:
                        ind = alph_high_ru.index(k)
                if ind + move_symbol <= len(alph_high_ru):
                    new_phrase += alph_high_ru[ind + move_symbol]
                else:
                    new_phrase += alph_high_ru[(ind + move_symbol) % len(alph_high_ru)]
            else:
                for k in alph_low_ru:
                    if k == i:
                        ind = alph_low_ru.index(k)
                if ind + move_symbol <= len(alph_low_ru):
                    new_phrase += alph_low_ru[ind + move_symbol]
                else:
                    new_phrase += alph_low_ru[(ind + move_symbol) % len(alph_low_ru)]
        else:
            new_phrase += i
    print(new_phrase)

def tsezar_decode():
    new_phrase = ''
    phrase = input('Введите предложение, которое вы хотите декодировать: ')
    move_symbol = int(input('Введите сдвиг для дешифрования: '))
    for i in phrase:
        if i in alph_high_eng or i in alph_low_eng:
            if i in alph_high_eng:
                for k in alph_high_eng:
                    if k == i:
                        ind = alph_high_eng.index(k)
                if ind - move_symbol <= len(alph_high_eng):
                    new_phrase += alph_high_eng[ind - move_symbol]
                else:
                    new_phrase += alph_high_eng[(ind - move_symbol) % len(alph_high_eng)]
            else:
                for k in alph_low_eng:
                    if k == i:
                        ind = alph_low_eng.index(k)
                if ind - move_symbol <= len(alph_low_eng):
                    new_phrase += alph_low_eng[ind - move_symbol]
                else:
                    new_phrase += alph_low_eng[(ind - move_symbol) % len(alph_low_eng)]
        elif i in alph_high_ru or i in alph_low_ru:
            if i in alph_high_ru:
                for k in alph_high_ru:
                    if k == i:
                        ind = alph_high_ru.index(k)
                if ind - move_symbol <= len(alph_high_ru):
                    new_phrase += alph_high_ru[ind - move_symbol]
                else:
                    new_phrase += alph_high_ru[(ind - move_symbol) % len(alph_high_ru)]
            else:
                for k in alph_low_ru:
                    if k == i:
                        ind = alph_low_ru.index(k)
                if ind - move_symbol <= len(alph_low_ru):
                    new_phrase += alph_low_ru[ind - move_symbol]
                else:
                    new_phrase += alph_low_ru[(ind - move_symbol) % len(alph_low_ru)]
        else:
            new_phrase += i
    print(new_phrase)

if task == True:
    tsezar_code()
else:
    tsezar_decode()