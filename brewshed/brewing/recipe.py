
class Recipe(object):
    """
    A recipe should contain resources consumed during brewing, and a schedule for when various events occur.
    """

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)