days = [
    "Maandag" ,
    "Dinsdag" , 
    "Woensdag", 
    "Donderdag" , 
    "Vrijdag" , 
    "Zaterdag" , 
    "Zondag"
]

#---- Functions ----#
def werkdagen(): #1
    print (days[0:5])

def weekend_dagen(): #2
    print (days[5:7])

def weekend_alle_dagen(): #3
    print (days)

def omgekeerde_weekend_dagen():#4
    days.reverse()
    print (days)

def omgekeerde_werkdagen(): #5
    days.reverse()
    print (days[2:7])

def omgekeerde_weekend():
    days.reverse()
    print (days[0:2])

#----Weekend Dagen Gevraagd----#
choice = int (input("Welke opties wilt u zien ? kies uit (Nummers invullen) : \n 1. Werkdagen \n 2. Weekend Dagen \n 3. Alle Dagen \n 4. Omgekeerde Werkdagen \n 5. Omgekeerde Weekend Dagen \n 6. Omgekeerde Weekend \n"))

if choice == 1:
    werkdagen()

elif choice == 2:
    weekend_dagen()

elif choice == 3:
    weekend_alle_dagen()

elif choice == 4:
    omgekeerde_weekend_dagen()

elif choice == 5:
    omgekeerde_werkdagen()

elif choice == 6:
    omgekeerde_weekend()




#-----Function Execution-----#
# werkdagen()
# weekend_dagen()
