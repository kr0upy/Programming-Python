left = int(input())
right = int(input())
segment = [i for i in range(left, right + 1)]
print(segment)
nums = list()
while True:
    try:
        num = input()
        num = int(num)
        nums.append(num)
    except:
        if num == "":
            break
        else:
            continue
isNums = True
print(nums)
for i in nums:
    if i not in segment:
        isNums = False
        break
print(isNums)