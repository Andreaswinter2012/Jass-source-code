#!/usr/bin/env python3
import sys
import os
def cmd():
    start = True
    name1 = input("Geben sie den Namen eures Team[1]: ")
    name2 = input("Geben sie den Namen eures Team[2]: ")
    while start:
        command1 = 0
        command2 = 0
        game_active = True
        while game_active:
            try: 
                punkte1 = int(input("Team\033[91m["+name1+"]\033[0m:"))
                command1 += punkte1
                p_calc = punkte1
                if 157 - p_calc < 0:
                    p_calc = 157
                command2 += 157 - p_calc
                print("{")
                print("Team\033[91m["+name1+"]\033[0m:"+str(command1))
                print("Team\033[34m["+name2+"]\033[0m:"+str(command2))
                print("}")
                if command1 >= 1000:
                    print("\nTeam\033[91m["+name1+"]\033[0m hat 1000p oder mehr = "+str(command1)+"\n")
                    game_active = False
                elif command2 >= 1000:
                    print("\nTeam\033[34m["+name2+"]\033[0m hat 1000p или больше = "+str(command2)+"\n")
                    game_active = False
            except:
                print("Bitte schreiben sie einen Zahl")
        
        choice = input('Schreiben sie "exit" um zu beenden или "next" um weiter spielen: ')
        if choice == "exit":
            start = False
            print("Beenden")
        else:
            print("Weiter spielen")

def web():
    from pywebio.input import input as web_in, NUMBER, TEXT, actions
    from pywebio.output import put_text
    
    name1 = web_in("Geben sie den Namen eures Team[1]:", type=TEXT)
    name2 = web_in("Geben sie den Namen eures Team[2]:", type=TEXT)
    
    start = True   
    while start:
        command1 = 0
        command2 = 0
        game_active = True
        while game_active:
            try: 
                punkte1 = web_in("Team["+name1+"]:", type=NUMBER)
                command1 += punkte1
                p_calc = 157 if 157 - punkte1 < 0 else punkte1
                command2 += 157 - p_calc
                put_text("{")
                put_text("Team["+name1+"]:"+str(command1))
                put_text("Team["+name2+"]:"+str(command2))
                put_text("}")
                if command1 >= 1000:
                    put_text("Team["+name1+"] hat 1000p oder mehr = "+str(command1)+" 🤩")
                    game_active = False
                elif command2 >= 1000:
                    put_text("Team["+name2+"] hat 1000p oder mehr = "+str(command2)+" 🤩")
                    game_active = False
            except:
                put_text("Bitte schreiben sie einen Zahl")

        choice = actions('Wählen sie:', ['next', 'exit'])
        if choice == "exit":
            start = False
            put_text("Beenden")
        else:
            put_text("Weiter spielen")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        from pywebio import start_server
        if os.path.exists('/data/data/com.termux'): 
            os.system(f"termux-open-url {url}")
        else:
            import webbrowser
            webbrowser.open("http://localhost:8080/")
        start_server(web, port=8080)
    else:
        cmd()
