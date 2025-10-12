import random

lower_limit = int(input("Введите нижнюю границу: "))
higher_limit = int(input("Введите верхнюю границу: "))

attemps = (3)
guessed = False

digit = random.randrange(lower_limit, higher_limit + 1)

for _ in range(attemps):
    supposition = int(input("Введите предполагаемое число: "))
    if supposition == digit:
        print(f"Вы угадали число за {_+1} попытки(у)!")
        guessed = True
        break
    else:
        if supposition > digit:
            print("Загаданное число меньше")
        else:
            print("Загаданное число больше")
if guessed == False:
    if digit % 2 == 0:
        print("Загаданное число четное")
    else:
        print("Загаданное число нечетное")
    print("У вас осталась одна попытка!")
    supposition = int(input("Введите предполагаемое число: "))
    if supposition == digit:
        print("Вы угадали число за  4 попытки!")
    else:
        print(f"Вы не угадали число {digit}")