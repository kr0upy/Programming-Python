def string(nums):
    nums = nums.split()
    nums = [int(i) for i in nums]
    average = sum(nums) / len(nums)
    strs = str(average).split('.')
    if len(strs[1]) > 2:
        return f'{average:.2f}'
    return average
while True:
    text = input()
    if text == '':
        break
    print(string(text))