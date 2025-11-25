def fibbonachi(number):
    fibosumlist = {1:1, 2:1}
    fibo = 0
    for i in range(1, number + 1):
        if number in fibosumlist:
            fibo = fibosumlist[number]
            return fibo
        else:
            if i > 1:
                fibosumlist[i + 1] = fibosumlist[i - 1] + fibosumlist[i]
    return fibo
number = int(input())
print(fibbonachi(number))