text = input().split()
print(text, len(text))
avarage = sum([len(i) for i in text]) / len(text)
print(avarage)