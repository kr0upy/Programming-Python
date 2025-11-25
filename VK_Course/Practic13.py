def edit_text(text):
    if text[0] == '!':
        text = text.upper()
    else:
        text = text.lower()
    text = text.replace('%', '').replace('!', '').replace('@', '').replace('#', '')
    print(text)

while True:
    try:
        text = input()
        edit_text(text)
    except:
        break