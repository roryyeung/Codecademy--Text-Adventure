from items import *

class Character:
    def  __init__(self,name,level,items):
        self.name = name
        self.level = level
        self.items = items
        self.isDead = False
        self.equipped = items[0]

class Player(Character):
    def __init__(self,name,level,items):
        super().__init__(name,level,items)
        self.xp = 0
        self.base_hp = 25
        self.hp = self.base_hp + self.level
        self.base_attack = 7
        self.attack = self.base_attack + self.level + self.equipped.attack_bonus
        self.gold = 0

    def __repr__(self):
        return "Yourself, {name}, equipped with a {item}".format(name = self.name, item = self.equipped.name)


class Goblin(Character):
    def __init__(self,name,items):
        super().__init__(name,2,items)
        self.hp = 14
        self.base_attack = 4
        self.attack = self.base_attack + self.equipped.attack_bonus
    
    def __repr__(self):
        return "A goblin, {name}, equipped with a {item}".format(name = self.name, item = self.equipped.name)

class Troll(Character):
    def __init__(self,name):
        super().__init__(name,2,[club])
        self.hp = 20
        self.base_attack = 6
        self.attack = self.base_attack
    
    def __repr__(self):
        return "A troll! You should run!"

