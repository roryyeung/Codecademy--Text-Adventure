def attack(attacker,target):
    damage = attacker.attack
    start_hp = target.hp
    attacker_name = attacker.name
    target_name = target.name
    if damage >= start_hp:
        target.isDead = True
        print("{attacker_name} did {damage} damage to {target_name}, killing them.".format(attacker_name = attacker_name, damage = str(damage), target_name = target_name))
    else:
        target.hp = start_hp - damage
        print("{attacker_name} attacked {target_name}, causing {damage} damage.".format(attacker_name = attacker_name, target_name = target_name,damage = str(damage)))

def combat(attacker,target):
    while attacker.isDead == False and target.isDead == False:
        attack(attacker,target)
        if target.isDead == True:
            return
        attack(target,attacker)
        if attacker.isDead == True:
            return

def yesNoChoice():
    choice = 'undecided'
    while choice == 'undecided':
        selection = input('Y/N: ')
        if selection == 'N' or selection == 'n':
            return 'N'
        elif selection == 'Y' or selection == 'y':
            return 'Y'
        else:
            print('Please try that again!')
