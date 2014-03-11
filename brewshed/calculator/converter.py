from pint import UnitRegistry

class Converter(object):

    ureg = UnitRegistry()

    @classmethod
    def convert(cls, amount, quantity, target_quantity):
        return amount*cls.ureg[quantity].to(target_quantity)
