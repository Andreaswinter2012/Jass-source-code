from colorama import Fore, Back, Style
command1 = 000
#erste variable
command2 = 000
#zweite variable
start = True
while start:

    try: 
      punkte1 = int(input("Team"+Fore.RED+"[1]"+Style.RESET_ALL+":"))
      #input1 variable
      command1 += punkte1
      #dann wird erste variable addiert mit input variable
      command2 += 157 - punkte1
      #dann wird zweite variable addiert mit erste variable und minus 157
      print("{")
      print("Team"+Fore.RED+"[1]"+Style.RESET_ALL+":"+str(command1))
      print("Team"+Fore.BLUE+"[2]"+Style.RESET_ALL+":"+str(command2))
      print("}")
      if command1 >= 1000:
          print()
          print("Team"+Fore.RED+"[1]"+Style.RESET_ALL+"hat 1000p oder mehr als 1000 = "+str(command1))
          print()
          start = False
      if command2 >= 1000:
          print()
          print("Team"+Fore.BLUE+"[2]"+Style.RESET_ALL+"hat 1000p oder mehr als 1000 = "+str(command2))
          print()
          start = False

    except:
            print("Bitte screiben sie einen Zahl")

input("press enter to exit")
