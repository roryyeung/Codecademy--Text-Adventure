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
        self.base_hp = 10
        self.hp = self.base_hp + self.level
        self.base_attack = 5
        self.attack = self.base_attack + self.level + self.equipped.attack_bonus

    def __repr__(self):
        return "Yourself, {name}, equipped with a {item}".format(name = self.name, item = self.equipped.name)


class Goblin(Character):
    def __init__(self,name,items):
        super().__init__(name,2,items)
        self.hp = 7
        self.base_attack = 2
        self.attack = self.base_attack + self.equipped.attack_bonus
    
    def __repr__(self):
        return "A goblin, {name}, equipped with a {item}".format(name = self.name, item = self.equipped.name)
