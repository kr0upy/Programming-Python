import random
high_dict = "QWERTYUIOPASDFGHJKLZXCVBNM"
high_dict_ru = "ЙЦУКЕНГШЩЗХЪЁФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
low_dict = "qwertyuiopasdfghjklzxcvbnm"
low_dict_ru = "йцукенгшщзхъёфывапролджэячсмитьбю"
bot_variables = ["paper", "stone", "scissors"]
bot_variables_ru = ["бумага", "камень", "ножницы"]
 
print("Игра в камень - ножницы - бумага!")
trueWins = False
while trueWins == False:
    try:
        wins_count = int(input("Введите количество выигрышей для победы: "))
        trueWins = True
    except:
        print("Вы ввели некорректное число!")

bot_wins = 0
player_wins = 0
while bot_wins != wins_count or player_wins != wins_count:
    try:
        player_var = input("Введите ваш ход: ")
        edited_player_var = ""
        for symbol in player_var:
            if symbol in high_dict:
                edited_player_var += high_dict.index(symbol)
            elif symbol in high_dict_ru:
                edited_player_var += high_dict_ru.index(symbol)
            else:
                edited_player_var += symbol
        player_var = edited_player_var
        if player_var in bot_variables:
            bot_var = random.choice(bot_variables)
            print(f"Bot choice: {bot_var}")
            if bot_var == player_var:
                print("Draw!")
            elif bot_var == "paper":
                if player_var == "stone":
                    print("Point to the bot!")
                    bot_wins += 1
                elif player_var == "scissors":
                    print("Point to you!")
                    player_wins += 1
            elif bot_var == "stone":
                if player_var == "scissors":
                    print("Point to the bot!")
                    bot_wins += 1
                elif player_var == "paper":
                    print("Point to you")
                    player_wins += 1
            elif bot_var == "scissors":
                if player_var == "stone":
                    print("Point to you")
                    player_wins += 1
                elif player_var == "paper":
                    print("Point to the bot!")
                    bot_wins += 1
        elif player_var in bot_variables_ru:
            bot_var = random.choice(bot_variables_ru)
            print(f"Ход бота: {bot_var}")
            if bot_var == player_var:
                print("Ничья!")
            elif bot_var == "бумага":
                if player_var == "камень":
                    print("Очко боту!")
                    bot_wins += 1
                elif player_var == "ножницы":
                    print("Очко тебе!")
                    player_wins += 1
            elif bot_var == "камень":
                if player_var == "ножницы":
                    print("Очко боту!")
                    bot_wins += 1
                elif player_var == "бумага":
                    print("Очко тебе")
                    player_wins += 1
            elif bot_var == "ножницы":
                if player_var == "камень":
                    print("Очко тебе")
                    player_wins += 1
                elif player_var == "бумага":
                    print("Очко боту")
                    bot_wins += 1
        elif player_var == "!":
            print("Technical stop...")
            break
        else:
            print("Некорректный ход!")
    except:
        print("Ошибка")
    print(f"Счёт: {player_wins} : {bot_wins}")
    if player_wins == wins_count:
            print("Ты победил!")
            break
    elif bot_wins == wins_count:
        print("Победа бота!")
        break
