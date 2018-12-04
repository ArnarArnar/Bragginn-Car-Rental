import os
from Services.CarService import CarService
from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from Models.Car import Car
from Models.Customer import Customer
from Models.Rental import Rental
from ViewModels.RentalViewModel import RentalViewModel 

class salesmanUI:

    def __init__(self):
        self._car_service = CarService()
        self._customer_service = CustomerService()
        self._rental_service = RentalService()


#Main menu 
    def mainMenu(self):
        """Display's the main menu"""
        while (input != "q" and input != "Q"):
            os.system('cls')
            print("\t********* Welcome to Bragginn Car Rental ********* \n"  #Create a seperate function called displayTitlebar
                "\tblow your horn on a car from Bragginn car rental! \n"
                "\t************************************************** \n"
                "\t1. Rentals \n"
                "\t2. Fleet \n"
                "\t3. Customer \n"
                "\tEnter q to quit \n")  #Need to fix a quit function so it actually exits the program
            userInput = input('What would you like to do? ')

            if userInput == "1":
                self.rentalInterface()
            if userInput == "2":
                self.fleetInterface()
            if userInput == "3":
                self.customerInterface()
            if userInput == "q" or userInput == "Q":
                print("Thank you come again")
                return

#SubMenus
    def fleetInterface(self):
        """Display's the fleet submenu"""
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
            self.seeFleetList()
        if userInput == "2":
            self.mainMenu()
        if userInput == "3":
            self.mainMenu()
        if userInput == "4":
            carID = input("Enter carID: ")  #Hafa kannski ser get user input fall sem er ur user input interface klasa
            brand = input("Enter car brand: ")
            year = input("Enter year of car model: ")
            price_per_day = input("Enter price per day: ")
            carType = input("Enter car type: ")
            newCar = Car(carID, brand, year, price_per_day, carType)
            self._car_service.add_car(newCar)
        if userInput == "5":
            self.mainMenu()

    def customerInterface(self):
        """Display's the customer submenu"""
        os.system('cls')
        print("\t********* Welcome to Bragginn Car Rental ********* \n"
                "\tblow your horn on a car from Bragginn car rental! \n"
                "\t************************************************** \n"
                "\t**************** Customer Management **************** \n"
                "\t1. Register New Customer \n"
                "\t2. Search Customers \n"
                "\t3. Deactivate Customer \n"
                "\t4. Change Customer Info \n"
                "\t5. See Customer History \n"
                "\t6. See All Customers \n"
                "\tEnter q to quit \n")
        userInput = input('What would you like to do? ')

        if userInput == "1":
            #Hafa kannski ser get user input fall sem er ur user input interface klasa
            customerID = input("Enter customer ID: ")
            firstName = input("Enter customer first name: ")
            lastName = input("Enter customer last name: ")
            phone = input("Enter customer phone: ")
            street = input("Enter customer street: ")
            zip = input("Enter customer zip: ")
            town = input("Enter customer town: ")
            country = input("Enter customer country: ")
            driversLicense = input("Enter customer driver's license number: ")
            newCustomer = Customer(customerID, firstName, lastName, phone, street, zip, town, country, driversLicense)
            self._customer_service.add_customer(newCustomer)
        if userInput == "2":
            self.mainMenu()
        if userInput == "3":
            self.mainMenu()
        if userInput == "4":
            self.mainMenu()
        if userInput == "5":
            self.mainMenu()
        if userInput == "6":
            self.seeCustomerList()

    def rentalInterface(self):
        """Display's the rentals submenu"""
        os.system('cls')
        print("\t********* Welcome to Bragginn Car Rental ********* \n"
                "\tblow your horn on a car from Bragginn car rental! \n"
                "\t************************************************** \n"
                "\t**************** Rental Management **************** \n"
                "\t1. Rent a Car \n"
                "\t2. Rental History \n"
                "\t3. Return Car \n"
                "\t4. Cancel Order \n"
                "\t5. Change Order \n"
                "\t6. See All Orders \n"
                "\tEnter q to quit \n")
        userInput = input('What would you like to do? ')

        if userInput == "1":
            #Hafa kannski ser get user input fall sem er ur user input interface klasa
            customerID = input("Enter ID for customer: ")
            carID = input("Enter ID of car to rent: ")
            startDate = input("Select start date: ")
            length = input("Enter how many days to rent: ")
            #totalPrice = 0 #spurning hvort her turfi ad fara ofan i grunninn, reikna ut total price og skila upp, kannski bara gert i middle layer
            newRental = Rental(customerID, carID, startDate, length, 0)
            self._rental_service.add_rental(newRental)
        if userInput == "2":
            #Hafa kannski ser get user input fall sem er ur user input interface klasa
            carID = input("Enter ID of car to see rental history: ")
            rentalView = self._rental_service.getCarRentalHistory(carID)
            self.seeRentalViewList(rentalView)
            #Senda rentalView svo i view sem prentar ut listann
        if userInput == "3":
            self.mainMenu()
        if userInput == "4":
            self.mainMenu()
        if userInput == "5":
            self.mainMenu()
        if userInput == "6":
            self.seeRentalList()


#Viems
    def seeFleetList(self):
        fleet_list = self._car_service.getFleetList()
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Total Fleet List **************** \n"
                "\tID:     Brand:       Year:      Price:      Type:       \n")
        for car in fleet_list:
            print("\t" + car._carID + ":     " + car._brand + ":      " + car._year + ":    " 
                  + car._price_per_day + ":      " + car._carType)
        os.system('pause')

    def seeCustomerList(self):
        customer_list = self._customer_service.getCustomerList()
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Customer List **************** \n"
                "\tID:     Name:       phone:      street:      zip:       town:      country:      license: \n")
        for customer in customer_list:
            print("\t" + customer._customerID + ":  " + customer._firstName + " " + customer._lastName + ":  " 
                  + customer._phone + ":  " + customer._street + ":  " + customer._zip + ":  "
                  + customer._town + ":  " + customer._country + ":  " + customer._driversLicense)
        os.system('pause')

    def seeRentalList(self):
        rental_list = self._rental_service.getRentalList()
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Rental List **************** \n"
                "\tcustomerID:     carID:       startDate:      days:      total price: \n")
        for rental in rental_list:
            print("\t" + rental._customerID + ":     " + rental._carID + "      " + rental._startDate + ":      " 
                  + rental._length + ":      " + rental._totalPrice)
                  #customerID, carID, startDate, length, totalPrice
        os.system('pause')

    def seeRentalViewList(self, rvList): #Rental viewlist kemur inn
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Rental List **************** \n"
                "\tcustomerID:     carID:       startDate:      days:      total price: \n")
        for rental in rvList:
            print("\t" + rental._customerID + ":     " + rental._customerFirstName + "      " + rental._customerLastName + 
                  ":      " + rental._carID + ":      " + rental._carBrand + ":  " + rental._startDate + ":  " +
                  rental._length + ":  " + rental._totalPrice)
                  #customerID, customerFirstName, customerLastName, carID, carBrand, startDate, length, totalPrice
        os.system('pause')
