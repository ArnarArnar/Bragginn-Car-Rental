import csv

#Get all the cars from the csv files
#Nota sem set frekar
def get_cars():
    """Get all the cars from the csv files"""
    Cars = []
    with open('Cars.csv') as carsFile:
        carsReader = csv.reader(carsFile, delimiter=';')
        carsList = list(carsReader)
        for row in carsList:
            Cars.append({'Number': row[0], 'Name': row[1]})
    return Cars

#Get all the customers from the csv files
def get_customers():
    with open('Customers.csv') as customersFile:
        customersReader = csv.reader(customersFile, delimiter=';')
        customers = list(customersReader)
    return customers

#Get all the rental orders from the csv files
def get_rentals():
    with open('Rentals.csv') as rentalsFile:
        rentalsReader = csv.reader(rentalsFile, delimiter=';')
        rentals = list(rentalsReader)
    return rentals

#Let user add car to database with user input
def add_car():
    carNumber = input('Enter car number: ')
    carName = input('Enter car name: ')

    with open('Cars.csv', 'a', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=';')
        csvWriter.writerow([carNumber, carName])