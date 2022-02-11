#List with numbers to be substracted , multiplied etc etc.
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [2,4,6,8,10,12,14,16,18,20]

#def forloops
def addAndDisplayLists (list_1, list_2):
    for i in range (10):
        print (list_1[i] ,"+" , list_2[i] ,"=" , list_1[i] + list_2[i])

def substractAndDisplayLists (list1, list2):
    for i in range (10):
        print (list_1[i] ,"-" , list_2[i] ,"=" , list_1[i] - list_2[i])

def multiplyAndDisplayLists (list1, list2):
    for i in range (10):
        print (list_1[i] ,"*" , list_2[i] ,"=" , list_1[i] * list_2[i])

def divideAndDisplayLists (list1, list2):
    for i in range (10):
        print (list_1[i] ,"/" , list_2[i] ,"=" , list_1[i] / list_2[i])


#def execution
addAndDisplayLists(list_1,list_2)
substractAndDisplayLists (list_1, list_2)
multiplyAndDisplayLists (list_1, list_2)
divideAndDisplayLists (list_1, list_2)