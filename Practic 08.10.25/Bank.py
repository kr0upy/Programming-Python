import random
import string

alph_low_eng = 'abcdefghijklmnoparstuvwxyz'
alph_high_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

profile_ID_length = 20

def create_password():
    global account
    global phone_number
    isTruePhone = False
    while isTruePhone == False:
        phone_number = input("Введите ваш номер телефона для регистрации (Россия): ")
        if (phone_number[:2] != '+7' and len(phone_number) != 12) or (phone_number[0] != '8' and len(phone_number) != 11):
            isTruePhone = True
        else:
            print("Вы ввели некорректный номер телефона")
    password = input("Придумайте пароль: ")
    accept_password = input("Подтвердите пароль: ")
    if password == accept_password:
        account = dict(phone_number = [password])
    return account


def create_profile():
    profile_ID = ""
    if account != None:
        for _ in range(profile_ID_length):
            profile_ID += random.choice([random.choice(alph_high_eng), random.choice(alph_low_eng), random.choice(string.digits)])
        user = input("Введите ваше ФИО: ")
        account["phone_number"].append(profile_ID)
        account["phone_number"].append(user)


def enter():
    global isEnter
    isEnter = False
    enter_number = input("Введите ваш номер телефона, указанный при регистрации: ")
    enter_password = input("Введите ваш пароль, указанный при регистрации: ")
    print(account["phone_number"])
    while isEnter == False:
        if phone_number == enter_number and enter_password == account["phone_number"][0]:
            print("Добро пожаловать!")
            isEnter = True
            break
        else:
            print("Неверная комбинация логин / пароль")

def create_check():
    if isEnter:
        try:
            check_name = input("Введите название своего счета: ")
            account["phone_number"].append([check_name])
            print(f"Вы создали счет {check_name}!")
        except:
            print("Ошибка.")

def balance():
    if isEnter:
        global money_amount
        money_amount = 0
        account["phone_number"][3].append(money_amount)
        print(f"Ваш баланс: {money_amount} руб.")

def add_money():
    try:
        trueMoney = False
        while trueMoney == False:
            money_plus = abs(int(input("Введите сумму, на которую хотите пополнить баланс: ")))
            check = input(f"Вы хотите пополнить баланс на {money_plus} руб. Введите + для поддтвержения: ")
            if check == "+":
                trueMoney = True
                account["phone_number"][3][1]  = account["phone_number"][3][1] + money_plus
                money_amount = account["phone_number"][3][1]
                print(f"Ваш баланс: {money_amount} руб.")#??
            else:
                print("Отмена действия")
                trueMoney = True
    except:
        print("Ошибка.")

def decrease_money():
    try:
        trueMoney = False
        while trueMoney == False:
            money_minus = abs(int(input("Введите сумму, которую вы хотите списать со счета: ")))
            if account["phone_number"][3][1] >= money_minus:
                check = input(f"Вы хотите списать со счета {money_minus} руб. Введите + для поддтвержения: ")
                if check == "+":
                    trueMoney = True
                    account["phone_number"][3][1] = account["phone_number"][3][1] - money_minus
                    money_amount = account["phone_number"][3][1]
                    print(f"Ваш баланс: {money_amount} руб.")
                else:
                    print("Отмена действия")
                    trueMoney = True
            else:
                print("Недостаточно средств")
    except:
        print("Ошибка.")

def transfer():
    try:
        true_Transfer = False
        while true_Transfer == False:
            money_transfer_account = input("Введите номер телефона, привязанного к акканту, на который вы хотите осуществить перевод: ")
            if (money_transfer_account[:2] != '+7' and len(money_transfer_account) != 12) or (money_transfer_account[0] != '8' and len(money_transfer_account) != 11):
                money_transfer= abs(int(input("Введите сумму, которую вы хотите перевести: ")))
                if account["phone_number"][3][1] >= money_transfer:
                    check = input(f"Перевод по номеру {money_transfer_account} на сумму {money_transfer}. Введите + для подтвержения: ")
                    if check == "+":
                        if money_transfer_account in account:
                            account["phone_number"][3][1]  = account["phone_number"][3][1] - money_transfer
                            money_amount = account["phone_number"][3][1]
                            account[money_transfer_account] = account[money_transfer_account] + money_transfer
                            print(f"Ваш баланс: {money_amount} руб.")
                        else:
                            account["phone_number"][3][1]  = account["phone_number"][3][1] - money_transfer
                            money_amount = account["phone_number"][3][1]
                            account[money_transfer_account] = money_transfer
                            print(f"Ваш баланс: {money_amount} руб.")
                        true_Transfer = True
                else:
                    print("Недостаточно средств")
                    true_Transfer = True
            else:
                print("Вы ввели некорректный номер")
    except:
        print("Ошибка")

def check_balance():
    money_amount = account["phone_number"][3][1]
    print(f"Ваш баланс: {money_amount} руб.")

def check_profile():
    FIO = account['phone_number'][2]
    profile_ID = account['phone_number'][1]
    cash = account['phone_number'][3][1]
    print(f"ФИО: {FIO}, ID профиля: {profile_ID}, Баланс: {cash}")
    
create_password()
create_profile()
enter()
create_check()
balance()
print(account["phone_number"])
while True:
    try:
        print("? - Узнать баланс, > - Совершить перевод, + - Пополнить баланс, - - Списать сумму со счета, @ - Профиль, ! - Выйти из банка")
        action = input("Введите команду: ")
        if action == "?":
            check_balance()
        elif action == ">":
            transfer()
        elif action == "+":
            add_money()
        elif action == "-":
            decrease_money()
        elif action == "@":
            check_profile()
        elif action == "!":
            print("До свидания!")
            break
        else:
            print("Некорректная команда")
    except:
        print("Ошибка")