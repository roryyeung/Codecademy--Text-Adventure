from characters import *
from engine import *

def encounter(player):
    print('You enter the cave. It is dark.')
    print('There is a light ahead.')
    print('Do you continue ahead?')

    cont = yesNoChoice()
    if cont == 'N':
        print('You go back to town. Adventuring isnt for everyone.')
        return 'Gameover'
    elif cont == 'Y' or cont == 'y':
        print('You start ahead into the cave.')
    
    print('You enter a room with a small fire.')
    print('A goblin jumps out of nowhere and attacks you!')

    gobbers = Goblin('Gobbers',[sword])
    combat(gobbers,player)
    if player.isDead == True:
        print("You are dead!")
        return 'Gameover'
    print("You killed the goblin! Gain 1xp.")
    player.xp += 1
    print("You have {hp} hp remaining.".format(hp = str(player.hp)))

    print("Do you want to look around?")
    lookAround = yesNoChoice()
    if lookAround == 'Y':
        print('You find a gold coin on the floor!')
        player.gold += 1
    
    print("You continue on. The cave leads to a door.")

    print("Do you want to open the door?")
    cont = yesNoChoice()
    if cont == 'N':
        print('You go back to town. One kill is enough for now.')
        return
    elif cont == 'Y' or cont == 'y':
        print('You open the door.')
    print('Behind the door, you enter a dimly lit room. You find is has a spit-roast in the centre, over a fire. It smells rotten.')
    print('You see a troll skulking across the room.')

    print('Do you want to stay and fight?')
    cont = yesNoChoice()
    if cont == 'N':
        print('You start running. You hear the troll start to chase you.')
        print('On the way out you trip, and fall on your face. You loose 1hp.')
        player.hp -= 1
        if player.hp <= 0:
            print('The fall breifly knocks you out. Unfortunately, this is enough for the troll to catch up. It catches you and drags you to the fire.')
            player.isDead == True
            return "Gameover"
        print('You manage to get away, and make it back to town.')
        return
    elif cont == 'Y' or cont == 'y':
        print('You attack the Troll.')
    
    trolly = Troll('Trolly')
    combat(player,trolly)
    if player.isDead == True:
        print("You are dead!")
        return 'Gameover'
    print("You killed the Troll! Gain 5xp.")
    player.xp += 5
    print("You have {hp} hp remaining.".format(hp = str(player.hp)))

    print("You look around the room. You find a purse containing 10 gold coins!")
    player.gold += 10

    print("You head back to town, content with your finds!")