command1 = 000
#erste variable
command2 = 000
#zweite variable
start = True
while start:

    try: 
      punkte1 = int(input("Team\033[91m[1]\033[0m:"))
      #input1 variable
      command1 += punkte1
      #dann wird erste variable addiert mit input variable
      command2 += 157 - punkte1
      #dann wird zweite variable addiert mit erste variable und minus 157
      print("{")
      print("Team\033[91m[1]\033[0m:"+str(command1))
      print("Team\033[34m[2]\033[0m:"+str(command2))
      print("}")
      if command1 >= 1000:
          print()
          print("Team\033[91m[1]\033[0m hat 1000p oder mehr als 1000 = "+str(command1))
          print()
          start = False
      if command2 >= 1000:
          print()
          print("Team\033[34m[2]\033[0m hat 1000p oder mehr als 1000 = "+str(command2))
          print()
          start = False

    except:
            print("Bitte screiben sie einen Zahl")

input("press enter to exit")

