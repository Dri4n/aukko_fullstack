import datetime
from collections import OrderedDict
from sqlalchemy.ext.declarative import DeclarativeMeta

class Serializable(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if isinstance(value, datetime.datetime):
                value = value.__str__()
            result[key] = value
        
        for attr, relation in self.__mapper__.relationships.items():
            value = getattr(self, attr)
            if value is not None:
                if isinstance(value.__class__, DeclarativeMeta):
                    result[relation.key] = value._asdict()
        return result