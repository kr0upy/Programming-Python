string = input().lower()
print(string)
string = [i for i in string]
stringSet = set()
for i in range(len(string)):
    stringSet.add(string[i])
print(sorted(stringSet))