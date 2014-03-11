version = '1.0'

class NotImplementedError(Exception):
    pass

class Serializer(object):
    """
    Base class for serializers to key stores
    """

    def __init__(self, backend=None, nameaspace=None):
        backend = CouchBackend if backend is None else backend
        self.namespace = ''
        self.backend = backend

    def save(self, obj, key=None):
        data = obj.__dict__.copy()
        data['__kind'] = type(obj)
        return self.backend.dump(data, key)

    def load(self, key):
        data = self.backend.get(key)
        kind = data.pop('__kind')
        eval('{}(**data)'.format(kind))


class BaseBackend(object):

    def dump(self, data, key):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError


class CouchBackend(BaseBackend):

    def __init__(self, namespace):
        self.namespace = namespace
        self.backend = None

    def dump(self, data, key):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError


class MigrationException(Exception):

    def __init__(self, cls, model_required, model_read):
        self.cls = cls
        self.model_required = model_required
        self.model_read = model_read


class BaseModel(object):

    serializer = None
    version = version
    date_created = None
    date_modified = None

    def save(self):
        data = self.__dict__
        pass

    @classmethod
    def load(cls, key):

        # Find out how to load item with key for object store
        data = {}

        if cls.model_number != data['model_number']:
            raise MigrationException(cls, version, data['model_number'])
        return cls(**data)

