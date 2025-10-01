cakes_count = abs(int(input('Введите количество заказываемых пирожных: ')))
def print_pack_report(cakes_count):
    if cakes_count % 3 == 0 and cakes_count % 5 == 0:
        print('Расфасуем по 3 или по 5')
    elif cakes_count % 3 == 0 and cakes_count % 5 != 0:
        print('Расфасуем по 3')
    elif cakes_count % 3 != 0 and cakes_count % 5 == 0:
        print('Расфасуем по 5')
    else:
        print('Не заказываем!')
print_pack_report(cakes_count)