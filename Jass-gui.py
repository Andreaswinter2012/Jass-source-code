from pywebio.input import *
from pywebio.output import put_text
start = True
while start:
    command1 = 000
    #erste variable
    command2 = 000
    #zweite variable
    while start:
        try: 
            punkte1 = input("Team[1]:",type=NUMBER)
            #input1 variable
            command1 += punkte1
            #dann wird erste variable addiert mit input variable
            if 157 - punkte1 < 0:
                punkte1 = 157
            command2 += 157 - punkte1
            #dann wird zweite variable addiert mit erste variable und minus 157
            put_text("{")
            put_text("Team[1]:"+str(command1))
            put_text("Team[2]:"+str(command2))
            put_text("}")
            if command1 >= 1000:
                put_text()
                put_text("Team[1] hat 1000p oder mehr als 1000 = "+str(command1)+"🤩")
                put_text()
                start = False
            if command2 >= 1000:
                put_text()
                put_text("Team[2] hat 1000p oder mehr als 1000 = "+str(command2)+"🤩")
                put_text()
                start = False

        except:
                put_text("Bitte screiben sie einen Zahl")

    start = input('Screiben sie "exit" um zu beenden oder "next" um weiter spielen', type=TEXT)
    if start == "exit":
        start = False
        put_text("Beenden")
    if start == "next":
        start = True
        put_text("Weiter spielen")
