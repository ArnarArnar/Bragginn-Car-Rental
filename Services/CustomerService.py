"""Service class for Customers"""
from Repositories.CustomerRepository import CustomerRepository
from Models.Customer import Customer
from Models.CreditCard import CreditCard
from ViewModels.CustomerViewModel import CustomerViewModel

# Testing, take out
import os

class CustomerService:

    def __init__(self):
        self._customer_repo = CustomerRepository()
        self._customer_view_list = []

# Post functions
    def add_customer(self, Customer):
        self._customer_repo.add_customer(Customer)

    def add_credit_card(self, CreditCard):
        self._customer_repo.add_credit_card(CreditCard)

# Get functions
    def get_customer_list(self):
        return self._customer_repo.get_customer_list()

    def get_customer(self, customer_id): # customer_id, customer_first_name, customer_last_name, country, card_number
        credit_card_list = []
        customers = self._customer_repo.get_customer_list()
        credit_cards = self._customer_repo.get_credit_card_list()
        for customer in customers:
            if customer._customer_id == customer_id:
                customer_first_name = customer._first_name
                customer_last_name = customer._last_name
                country = customer._country
                for credit_card in credit_cards:
                    if credit_card._customer_id == customer_id:
                        credit_card_list.append(credit_card._card_number)
            customer_to_view = CustomerViewModel(customer_id, customer_first_name,
                                                customer_last_name, country, credit_card_list)
        return customer_to_view