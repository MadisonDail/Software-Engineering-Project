# Pokemon

class Pokemon:
    def __init__(self, idNum, name, type1, type2, ability1, currentHp, hp, attack, defense, specAttack, specDefense, speed, move1=None, move2=None, move3=None, move4=None, status="None"):
        self.idNum = idNum #number in the dex
        self.name = name #pokemon name
        self.type1 = type1 #pokemon's main type
        self.type2 = type2 #pokemon's second type (not all pokemon have 2 types)
        self.ability1 = ability1 ##pokemon's main ability
        self.currentHp = currentHp #pokemon's current hp
        self.hp = hp #pokemon's hp stat
        self.attack = attack #pokemon's attack stat
        self.currentAttack = attack #pokemon's current attack (in battle)
        self.defense = defense #pokemon's defense stat
        self.currentDefense = defense #pokemon's current defense (in battle)
        self.specAttack = specAttack #pokemon's special attack stat
        self.currentSpecAttack = specAttack #pokemon's current special attack (in battle)
        self.specDefense = specDefense #pokemon's special defense stat
        self.currentSpecDefense = specDefense #pokemon's current special defense (in battle)
        self.speed = speed #pokemon's speed
        self.currentSpeed = speed #pokemon's current speed (in battle)
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.status = status