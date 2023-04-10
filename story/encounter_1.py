from characters import *
from engine import *

def encounter(player):
    print('You enter the cave. It is dark.')
    print('There is a light ahead.')
    print('Do you continue ahead?')

    cont = yesNoChoice()
    if cont == 'N':
        gameover = True
        print('You go back to town. Adventuring isnt for everyone.')
        return
    elif cont == 'Y' or cont == 'y':
        print('You start ahead into the cave.')
    
    print('You enter a room with a small fire.')
    print('A goblin jumps out of nowhere and attacks you!')

    gobbers = Goblin('Gobbers',[sword])
    combat(gobbers,player)