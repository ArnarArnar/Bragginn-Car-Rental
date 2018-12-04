"""Service class for Customers"""
from Repositories.CustomerRepository import CustomerRepository
from Models.Customer import Customer

class CustomerService:

    def __init__(self):
        self._customer_repo = CustomerRepository()

    def add_customer(self, Customer):
        if self.is_customer_valid(Customer) == True:
            self._customer_repo.add_customer(Customer)

    def is_customer_valid(self, Customer):
        #Validation check
        return True

    def get_customer_list(self):
        return self._customer_repo.get_customer_list()