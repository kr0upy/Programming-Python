start, end, step = input().split()
nums = range(int(start), int(end), int(step))
for i in (map(lambda num: -num if num % 2 == 0 else num ** 2, nums)):
    print(i)