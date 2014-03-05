from brewshed.base import BaseItem
from brewshed.calculator.converter import Converter

class ModificationError(Exception):
    pass

class Item(BaseItem):

    def __init__(self, name, amount, quantity):
        self.name = name
        self.amount = amount
        self.quantity = quantity

    def add_amount(self, amount, quantity=None):
        if quantity is None or quantity == self.quantity:
            self.amount += amount
        else:
            self.amount += Converter.convert(amount, quantity, self.quantity)

    def subtract_amount(self, amount, quantity=None):
        if quantity is not None and quantity != self.quantity:
            amount = Converter.convert(amount, quantity, self.quantity)
        if amount > self.amount:
            raise ModificationError('Can not subtract {} {} of {}, only {} left'.format(amount,
                                                                                        self.quantity,
                                                                                        self.name,
                                                                                        self.amount))
