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
        """Sends Customer object to repo layer to add to database"""
        self._customer_repo.add_customer(Customer)

    def add_credit_card(self, CreditCard):
        """credit card object to repo layer to add to database"""
        self._customer_repo.add_credit_card(CreditCard)

    def delete_customer(self, customer_to_del):
        """Delete customer from database"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_del: #Maybe need to find a more efficient way
                customer_list.remove(customer)
        self._customer_repo.overwrite_customer_list(customer_list)
        credit_card_list = self._customer_repo.get_credit_card_list()
        for credit_card in credit_card_list:
            if credit_card.get_customer_id() == customer_to_del: #Maybe need to find a more efficient way
                credit_card_list.remove(credit_card)
        self._customer_repo.overwrite_credit_card_list(credit_card_list)

#Update function
    def update_customer_id(self, customer_to_change, new_value):
        """Change value of customer ID"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_customer_id(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)

    def update_customer_first_name(self, customer_to_change, new_value):
        """Change value of first name"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_first_name(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_last_name(self, customer_to_change, new_value):
        """Change value of customer last name"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_last_name(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)

    def update_customer_phone(self, customer_to_change, new_value):
        """Change value of customer phone"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_phone(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_street(self, customer_to_change, new_value):
        """Change value of customer street"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_street(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_zip(self, customer_to_change, new_value):
        """Change value of customer zip"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_zip(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_town(self, customer_to_change, new_value):
        """Change value of customer town"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_town(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)

    def update_customer_country(self, customer_to_change, new_value):
        """Change value of customer country"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_country(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)
    
    def update_customer_license(self, customer_to_change, new_value):
        """Change value of customer license"""
        customer_list = self._customer_repo.get_customer_list()
        for customer in customer_list:
            if customer.get_customer_id() == customer_to_change.get_customer_id():
                customer.set_drivers_license(new_value)
        self._customer_repo.overwrite_customer_list(customer_list)

# Get functions
    def get_customer_list(self):
        """Get list of customers"""
        return self._customer_repo.get_customer_list()

    def get_customer(self, customer_id):
        """Get one customer"""
        customers = self._customer_repo.get_customer_list()
        for customer in customers:
            if customer.get_customer_id() == customer_id:
                customer_to_return = customer
        return customer_to_return

    def get_customer_credit_cards(self, customer_id):
        """Get list of credit cards belonging to customer"""
        customer_credit_card_list = []
        credit_cards = self._customer_repo.get_credit_card_list()
        for credit_card in credit_cards:
                    if credit_card.get_customer_id() == customer_id:
                        customer_credit_card_list.append(credit_card.get_card_number())
        return customer_credit_card_list
        

    # Maybe not being used anymore, we just use customer and credit card seperately
    def get_customer_viewmodel(self, customer_id):
        """Create viewmodel of customer along with creditcards owned"""
        credit_card_list = []
        customers = self._customer_repo.get_customer_list()
        credit_cards = self._customer_repo.get_credit_card_list()
        for customer in customers:
            if customer.get_customer_id() == customer_id:
                customer_first_name = customer.get_first_name()
                customer_last_name = customer.get_last_name()
                country = customer.get_country()
                for credit_card in credit_cards:
                    if credit_card.get_customer_id() == customer_id:
                        credit_card_list.append(credit_card.get_card_number())
                customer_to_view = CustomerViewModel(customer_id, customer_first_name,
                                                customer_last_name, country, credit_card_list)
        return customer_to_view