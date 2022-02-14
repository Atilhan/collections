from random import choice 
from random import randint
#List
game_list = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet' , 'Cluedo']



#Functions 
def spelProgramma(spelList,Minimum,Maximum): #3 parameters have been made & they get their value in line 15, SpelList gets the value from the list game_list and 3 , 10 gets added to the parameter Minimum value & Maximum value
    game_program = [] #empty list so a list can be printed without creating addition variables as a output.
    for y in range (randint (Minimum,Maximum)):# Gets a random number to loop.
        game_program.append (choice(spelList))
    return game_program

print (spelProgramma(game_list, 3 , 10))