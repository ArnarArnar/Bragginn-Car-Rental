"""Service class for Customers"""
from Repositories.CustomerRepository import CustomerRepository
from Models.Customer import Customer
from Models.CreditCard import CreditCard

class CustomerService:

    def __init__(self):
        self._customer_repo = CustomerRepository()

    def add_customer(self, Customer):
        self._customer_repo.add_customer(Customer)

    def add_credit_card(self, CreditCard):
        self._customer_repo.add_credit_card(CreditCard)

    def get_customer_list(self):
        return self._customer_repo.get_customer_list()