# Pokemon

class Pokemon:
    def __init__(self, idNum, name, type1, type2, ability1, currentHp, hp, attack, defense, specAttack, specDefense, speed):
        self.idNum = idNum #number in the dex
        self.name = name #pokemon name
        self.type1 = type1 #pokemon's main type
        self.type2 = type2 #pokemon's second type (not all pokemon have 2 types)
        self.ability1 = ability1 ##pokemon's main ability
        self.currentHp = currentHp #pokemon's current hp
        self.hp = hp #pokemon's hp stat
        self.attack = attack #pokemon's attack stat
        self.defense = defense #pokemon's defense stat
        self.specAttack = specAttack #pokemon's special attack stat
        self.specDefense = specDefense #pokemon's special defense stat
        self.speed = speed #pokemon's speed