"""Entity model for returns"""

class CarReturn:

    def __init__(self, order_id, days_late, gas_level, return_comment, extra_fee):
        self._order_id = order_id
        self._days_late = days_late
        self._gas_level = gas_level
        self._return_comment = return_comment
        self._extra_fee = extra_fee

    def __repr__(self):
        return "CarReturn('{}', '{}', '{}', '{}', '{}')".format(self._order_id,
                self._days_late, self._gas_level, self._return_comment, self._extra_fee)

    def __str__(self):
        return '   {:^4}   |     {:^4}    |   {:>6} kr   | {}  '.format(self._days_late,
         self._gas_level, self._extra_fee, self._return_comment)

#GetFunctions

    def get_order_id(self):
        return self._order_id

    def get_days_late(self):
        return self._days_late

    def get_gas_level(self):
        return self._gas_level

    def get_return_comment(self):
        return self._return_comment

    def get_extra_fee(self):
        return self._extra_fee

#SetFunctions

    def set_order_id(self, order_id):
        self._order_id = order_id

    def set_days_late(self, days_late):
        self._days_late = days_late

    def set_gas_level(self, expiry):
        self._expiry = expiry

    def set_return_comment(self, return_comment):
        self._return_comment = return_comment

    def set_extra_fee(self, extra_fee):
        self._extra_fee = extra_fee
