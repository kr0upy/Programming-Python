entries = int(input())
sortmax = []
maxes = []
while True:
    nums = input().split()
    if nums == []:
        break
    nums = sorted([int(i) for i in nums])
    sortmax.append(nums)
for i in range(entries):
    maxes.append(max(sortmax[i]))
maxes = sorted(maxes, reverse=True)
maxes = [str(i) for i in maxes]
maxes = [i + ';' for i in maxes]
maxes = (''.join(maxes))[:-1]
print(maxes)