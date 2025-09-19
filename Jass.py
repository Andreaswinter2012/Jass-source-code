command1 = 000
#erste variable
command2 = 000
#zweite variable
start = True
while start:
    try: 
      punkte1 = int(input("punkte1:"))
      #input1 variable
      punkte2 = int(input("punkte2:"))
      #input2 variable
      command1 += punkte1
      #dann wird erste variable addiert mit input variable
      command2 += punkte2
      #dann wird zweite variable addiert mit input variable
    except:
            print("Bitte screiben sie einen Zahl")
         
    if command1 == 1000:
          print("Gruppe1 hat 1000p")
          start = False
    if command2 == 1000:
          print("Gruppe2 hat 1000p")
          start = False
    if command1 > 1000:
          print("Gruppe1 hat mehr als 1000p = "+(str(command1)))
          start = False
    if command2 > 1000:
          print("Gruppe2 hat mehr als 1000p = "+(str(command2)))
          start = False
print(input())
