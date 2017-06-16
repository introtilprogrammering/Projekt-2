import numpy as np
from inputNumber import inputNumber 

# Viser en menu, beder brugeren om at vælge en af mulighederne ret og returnerer den valgte mulighed
def displayMenu(options):
    
    # Viser menuen
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
        
    # For at sikre at den valgte mulighed er gyldig.
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Vælg venligst en handling: ")
    return choice