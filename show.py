from os import system, name 
from datetime import date
import time
import functions

def header():
    system('cls')
    today = date.today()
    print("\n\n")
    print("    _")
    print("   (_)")
    print("  <___>")
    print("   | |___________________________________________")
    print("   | ||||   |||   |||   |||   |||   |||   |||   |")
    print("   | |   |||   |||   |||   |||   |||   |||   ||||")
    print("   | ||||   |||   |||   |||   |||   |||   |||   |")
    print("   | |   |||   |||   |||   |||   |||   |||   ||||")
    print("   | ||||   |||     OVERKART 2022   |||   |||   |")
    print("   | |   |||   |||   |||   |||   |||   |||   ||||")
    print("   | ||||   |||   |||   |||   |||   |||   |||   |")
    print("   | |   |||   |||   |||   |||   |||   |||   ||||")
    print("   | ||||   |||   |||   |||   |||   |||   |||   |")
    print("   | |   |||   |||   |||   |||   |||   |||   ||||")
    print("   | |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   | |")
    print("   | |")
    print("   | |")
    print("   | |")
    print("   | |")
    print("   | | Data do sorteio", str(today))
    print("\n\n")

def menu():

    initContent = input("Deseja iniciar o sorteio? [S]im ou [N]ao\n")
    if initContent == 'S' or initContent == 's':
        #functions.executeContent()
        #system('cls')
        return 1
    elif initContent == 'N' or initContent == 'n':
        print("Program aborted.")
        return 0
    else:
        print("Opcao invalida")
        time.sleep(2)
        return 0

def participants(numDrivers):
    print('\n\n\n\n')
    #print("Pilotos inscritos para próxima etapa: \n")
    #print(functions.driversList)
    print("\nTotal de",numDrivers,"pilotos.\n")
