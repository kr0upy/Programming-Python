import random
import math
import json

minweight = 50
maxweight = 150
minspeed = 40
maxspeed = 100
minhp = 50
maxhp = 150
default_damage = 10
min_dodge_chance = 5
max_dodge_chance = 16

with open("infos.json") as file:
    json_file = file.read()
names = (json.loads(json_file))['Names']

types = {#    Тип,          exponentHp, exponentSpeed, exponentDamage, attackSpeed, isShield?
        '1': ["Swordsman",     1.00,        1.00,            1.27,          1.00,    False], 
        '2': ["Archer",        0.89,        1.12,            1.08,          1.43,    False], 
        '3': ["Tank",          1.65,        0.54,            1.78,          0.79,    True]
         } 

class Knight:
    def __init__(self, name, type, weight):
        self.name = random.choice(names)
        isWarriorChosen = False
        while isWarriorChosen == False:
            try: 
                self.type_glob = input(f"Choose your warrior`s type (write number) 1: {types['1'][0]}, 2: {types['2'][0]}, 3: {types['3'][0]}: ")
                self.type = [types[self.type_glob], self.type_glob]
                isWarriorChosen = True
            except: print("Wrong choice")
        self.weight = weight
    
class KnightCharacteristics(Knight):
    def __init__(self, name:str, type:list, weight:int, speed:float, hp:int, damage: float, exponentSpeed, exponentHP):
        self.exponentSpeed = exponentSpeed
        normaled_weight = (weight - minweight) / (maxweight - minweight)

        speed_curve = 1 - math.pow(normaled_weight, exponentSpeed)
        self.speed = minspeed + speed_curve * (maxspeed - minspeed) #Скорость относительно веса

        hp_curve = math.pow(normaled_weight, exponentHP)
        self.hp = int(minhp + hp_curve * (maxhp - minhp)) #Хп относительно веса
        super().__init__(name, type, weight)
    
    def warrior_characteristics(self):
        exponentHp=types[self.type[1]][1]
        exponentSpeed=types[self.type[1]][2]
        exponentDamage=types[self.type[1]][3]
        self.attackSpeed=types[self.type[1]][4]
        isShield=types[self.type[1]][5]

        self.damage = default_damage * (self.weight ** 1/80) * exponentDamage
        self.speed = self.speed * exponentSpeed
        self.hp *= exponentHp
        print(isShield)
        if isShield == False:
            normalized_speed = (self.speed - minspeed) / (maxspeed - minspeed)
            normalized_speed = max(0, min(1, normalized_speed))
            self.dodge_chanse = min_dodge_chance + (max_dodge_chance - min_dodge_chance) * math.sqrt(normalized_speed)
        else:
            self.dodge_chanse = min_dodge_chance + (max_dodge_chance - min_dodge_chance) * (self.speed / maxspeed) + 25
        
    def info(self):
        print(f'Name: {self.name}, Type: {self.type[0][0]}, Weight: {self.weight}, Speed: {self.speed}, Hp: {self.hp}, Dodge: {self.dodge_chanse}%, Damage: {self.damage}, AttackSpeed: {self.attackSpeed}')
    


knight = KnightCharacteristics(None, None, random.randint(minweight, maxweight), None, None, None, 0.7, 0.8)
knight.warrior_characteristics()
print(knight.info())
