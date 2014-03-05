
class Converter(object):

    @classmethod
    def convert(cls, amount, quantity, target_quantity):
        # TODO: Use Scientific's physical quantities to convert amount from qty to target
        assert quantity == target_quantity
        return amount