string = input()
string = string.replace('!', '').replace('%', '').replace('#', '').replace('@', '')
string = string.lower()
print(string)