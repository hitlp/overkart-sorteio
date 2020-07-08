#######################
## OverKart - Sorteio #
#######################

import functions
import show
import time

show.header()
if show.menu() == 1:
    #call content
    numDrivers = functions.sortData()
    show.participants(numDrivers)
elif show.menu() == 0:
    #end
    exit()

    
print("------ Resultado -------\n")
#print("Bateria A: ", functions.teamA)
#print("Bateria B: ", functions.teamB, "\n")