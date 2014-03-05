model_number = '1.0'


class MigrationException(Exception):

    def __init__(self, cls, model_required, model_read):
        self.cls = cls
        self.model_required = model_required
        self.model_read = model_read


class BaseItem(object):

    model_number = model_number

    def save(self):
        data = self.__dict__
        pass

    @classmethod
    def load(cls, key):

        # Find out how to load item with key for object store
        data = {}

        if cls.model_number != data['model_number']:
            raise MigrationException(cls, model_number, data['model_number'])
        return cls(**data)

