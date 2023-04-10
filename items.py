class Item:
    def __init__(self,name,attack_bonus):
        self.name = name
        self.attack_bonus = attack_bonus

class Weapon(Item):
    def __init__(self,name,attack_bonus):
        super().__init__(name,attack_bonus)

sword = Weapon('sword',3)
club = Weapon('club',1)