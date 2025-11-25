text = input().lower().split()
wordcount = []
for word in text:
    wordcount.append([text.count(word), word])
print(sorted(wordcount)[-1][1], sorted(wordcount)[-1][0])
