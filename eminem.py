from random import randint
from random import choice

eminem = ['rood','orange','groen','blauw','geel','bruin']


def eminem_bag(eminem_amount : int):
    eminemBag = []
    for y in range (eminem_amount):
        eminemBag.append (choice(eminem)) #append pakt van eminem en doet het in eminemBag
    print(eminemBag)


#input
how_many_mm = int(input ('How many M&Ms would you like?'))

#function  execution
eminem_bag(how_many_mm)




    

