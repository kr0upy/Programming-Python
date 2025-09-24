string = input('Введите что-нибудь:')
string_set = set()
for i in string:
    string_set.add(i)
frequent_symbols = []
string_set = sorted(string_set)
if len(string) >= 3:
    for i in string_set:
        print('Символ', i ,'встречается', string.count(i), 'раз(а)')
        frequent_symbols.append((string.count(i), i))
    frequent_symbols = sorted(frequent_symbols, reverse=True)
    print(f'Три самых частых символа: {frequent_symbols[0][1]} {frequent_symbols[1][1]} {frequent_symbols[2][1]}')
else:
    for i in string_set:
        frequent_symbols.append((string.count(i), i))
    frequent_symbols = sorted(frequent_symbols, reverse=True)
    print(f'В строке {len(string)} символ(а): {frequent_symbols[0][1]}, {frequent_symbols[1][1]}')
# Есть метод 2 (через словарь) (лекцию смотрел полностью, но пока не до конца разобрался со словарями, поэтому сделал через множество)



