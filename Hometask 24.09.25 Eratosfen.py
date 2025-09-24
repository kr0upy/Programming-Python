Natural_digits = int(input('Введите натуральное число: '))
input_list = [i for i in range(Natural_digits + 1)]
input_list[1] = 0
num = 2
while num <= Natural_digits:
    if input_list[num] != 0:
        krat = num * 2
        while krat < Natural_digits:
            input_list[krat] = 0
            krat += num
    num += 1
input_list = [i for i in input_list if i != 0]
print(f'Простые числа от 0 до {Natural_digits}: {input_list}')

