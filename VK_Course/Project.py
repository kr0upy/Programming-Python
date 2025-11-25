text = input().lower().split()
symbols = '!,.?;:#$%^&*(),'
for i in range(len(text)):
    for symb in symbols:
        if symb in text[i]:
            text[i] = text[i].replace(symb, '')
text = sorted(set([word for word in text if len(word) >= 5 and len(set([i for i in word])) >= 4 and text.count(word) > 2]))
for word in text:
    print(word)