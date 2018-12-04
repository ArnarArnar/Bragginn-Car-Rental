import databases
import views
import os

def mainInterface():
    print("\t********* Welcome to Bragginn Car Rental ********* \n"
            "\tblow your horn on a car from Bragginn car rental! \n"
            "\t************************************************** \n"
            "\t1. Rentals \n"
            "\t2. Fleet \n"
            "\t3. Customer \n"
            "\tEnter q to quit \n")
    userInput = input('What would you like to do? ')

    if userInput == "1":
        databases.add_car()
    if userInput == "2":
        fleetInterface()
    if userInput == "3":
        databases.add_car()

    return userInput

def fleetInterface():
    os.system('cls')
    print("\t********* Welcome to Bragginn Car Rental ********* \n"
            "\tblow your horn on a car from Bragginn car rental! \n"
            "\t************************************************** \n"
            "\t**************** Fleet Management **************** \n"
            "\t1. See fleet list \n"
            "\t2. See all in rental \n"
            "\t3. See all available cars \n"
            "\t4. Add car \n"
            "\t5. See car history \n"
            "\tEnter q to quit \n")
    userInput = input('What would you like to do? ')

    if userInput == "1":
        databases.add_car()
    if userInput == "2":
        databases.add_car()
    if userInput == "3":
        views.seeAllCars()
    if userInput == "4":
        databases.add_car()
    if userInput == "5":
        databases.add_car()
