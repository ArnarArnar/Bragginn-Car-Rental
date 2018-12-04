import databases
from time import sleep

def seeAllCars():
    Cars = databases.get_cars()

    for c in Cars:
        print('Car: ')
        for key, value in c.items():
            print({"{key} => {value}".format(key=key, value=value)})
    sleep(5)