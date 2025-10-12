vowels_dict = "aeiouAEIOUуеёыаоэяиюУЕЁЫАОЛЭЯИЮ"
consonants_dict = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZйцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБп"
symbols_dict = "`~[]!@#$%^&*()_+-=%:,.;?/|'<>"

string = input("Введите строку: ")
vowels_count = 0
consonants_count = 0
spaces_count = 0
words_count = 0
symbols_count = 0
undetected_count = 0

if string != "":
        words_count += 1

for _ in string:
    if _ in vowels_dict:
        vowels_count += 1
    elif _ in consonants_dict:
        consonants_count += 1
    elif _ == " ":
        spaces_count += 1
    elif _ in symbols_dict:
        symbols_count += 1
    else:
        undetected_count += 1
    if " " + _ in string and _ != " ":
        words_count += 1
print(f"Количество слов в строке: {words_count}")
print(f"Количество гласных букв в строке: {vowels_count}")
print(f"Количество согласных букв в строке: {consonants_count}")
print(f"Количество пробелов в строке: {spaces_count}")
print(f"Количество символов в строке: {symbols_count}")
print(f"Количество необнаруженных символов в строке: {undetected_count}")