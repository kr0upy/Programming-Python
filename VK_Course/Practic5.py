first = int(input())
second = float(input())
third = abs(int(input()))

if first < 0:
    first = '-' + '0' * (9 - len(str(abs(first)))) + str(abs(first))
else: 
    first = '+' + '0' * (9 - len(str(abs(first)))) + str(abs(first))

second = ('#' * (10 - len(f'{second:.2f}')) + str(f'{second:.2f}'))

third = [i for i in str(bin(third))[2:].zfill(16)]
for i in range(1 ,len(third)):
    if i % 4 == 0:
        third[i - 1] = third[i - 1] + '_'
third = ''.join(third)
if len(third) > 19:
    third = third[::len(third)-19]
print(first)
print(second)
print(third)