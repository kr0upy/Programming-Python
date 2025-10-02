digit = input('Введите число, которое нужно конвертировать в римское (не более 3999!): ')
solos = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
duos = ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
trios = ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
quadro = 'M'
digit_places = [0] * 4
element = 1
for i in range(len(digit)):
    digit_places[-element] = int(digit[len(digit) - element]) #309
    element += 1
def roman_digit_create():
    roman_digit = quadro * digit_places[0] + trios[digit_places[1]] + duos[digit_places[2]] + solos[digit_places[3]]
    print(roman_digit)
if int(digit) <= 3999:
    roman_digit_create()
else:
    print('Вы ввели недопустимое для конвертации в римский вид число')