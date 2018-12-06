"""Service class for Customers"""
from Repositories.CustomerRepository import CustomerRepository
from Models.Customer import Customer
from Models.CreditCard import CreditCard
from ViewModels.CustomerViewModel import CustomerViewModel


class CustomerService:

    def __init__(self):
        self._customer_repo = CustomerRepository()
        self._customer_view_list = []

# Post functions
    def add_customer(self, Customer):
        self._customer_repo.add_customer(Customer)

    def add_credit_card(self, CreditCard):
        self._customer_repo.add_credit_card(CreditCard)

    def delete_customer(self, customer_to_del):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_del: #Maybe need to find a more efficient way
                customer_list.remove(customer)
        self._customer_repo.overwrite_customer_list(customer_list)
        credit_card_list = self._customer_repo.get_credit_card_list()
        for credit_card in credit_card_list:
            if credit_card._customer_id == customer_to_del: #Maybe need to find a more efficient way
                credit_card_list.remove(credit_card)
        self._customer_repo.overwrite_credit_card_list(credit_card_list)

#Update function
    def update_customer_id(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._customer_id = new_value
        self._customer_repo.overwrite_customer_list(customer_list)

    def update_customer_first_name(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._first_name = new_value
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_last_name(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._last_name = new_value
        self._customer_repo.overwrite_customer_list(customer_list)

    def update_customer_phone(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._phone = new_value
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_street(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._street = new_value
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_zip(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._zip = new_value
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_town(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._town = new_value
        self._customer_repo.overwrite_customer_list(customer_list)

    def update_customer_country(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._country = new_value
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_license(self, customer_to_change, new_value):
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer._customer_id == customer_to_change._customer_id:
                customer._drivers_license = new_value
        self._customer_repo.overwrite_customer_list(customer_list)

# Get functions
    def get_customer_list(self):
        return self._customer_repo.get_customer_list()

    def get_customer(self, customer_id):
        customers = self._customer_repo.get_customer_list()
        for customer in customers:
            if customer._customer_id == customer_id:
                customer_to_return = customer
        return customer_to_return

    def get_customer_viewmodel(self, customer_id):
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