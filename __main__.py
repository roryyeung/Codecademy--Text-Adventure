#This is the main game script.
#Story deals with the story.
from story.encounter_1 import encounter as encounter_1
#Engine deals with the engine.
from engine import *
#Characters contains character classes
from characters import *
#Items contains items
from items import *

player = Player('tempName',1,[sword])
gameover = False

print('What is your name, adventurer?')
player.name = input('Name: ')
print('Great - your name is: {name}'.format(name = player.name))
print('Lets start your adventure!')

encounter_1(player)

if gameover == True:
    print('Thats the end of the game!')
    quit()