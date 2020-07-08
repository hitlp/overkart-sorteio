from os import system, name 
from time import sleep
from datetime import date 
import random
import time

teamA = []
teamB = []
driversList = []

def sortData():
    driversNumber = 0
    f = open("participantes.txt","r")
    if f.mode == 'r':
        content = f.readlines()
        for i in range(len(content)):
            driversList.append(content[i].strip('\n'))
            driversNumber = driversNumber + 1
        
        teamSelector = 0
        time.sleep(2)
        
        #save teamA
        filehandle = open('RESULTADO_SORTEIO.csv', 'w')
        filehandle.write("BATERIA A;BATERIA B\n")
       
        for y in range(0, len(driversList)):
            numberDraw = random.randint(0,len(driversList)-1)
            if teamSelector == 0:
                print("BATERIA A", driversList[numberDraw])
                teamSelector = 1
                teamA.append(driversList[numberDraw])
                time.sleep(2)
                filehandle.write('%s;' % driversList[numberDraw])
            elif teamSelector == 1:
                print("BATERIA B", driversList[numberDraw])
                teamSelector = 0
                teamB.append(driversList[numberDraw])
                time.sleep(2)
                filehandle.write('%s;' % driversList[numberDraw])
                filehandle.write('\n')
            del driversList[numberDraw]
    else:
        print("List of drivers not found. Please create a list of drivers and rename as 'participantes.txt'")
    return driversNumber
#end sortData()