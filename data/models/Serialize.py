from collections import OrderedDict
from sqlalchemy.ext.declarative import DeclarativeMeta

class Serializable(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        
        for attr, relation in self.__mapper__.relationships.items():
            value = getattr(self, attr)
            if value is not None:
                if isinstance(value.__class__, DeclarativeMeta):
                    result[relation.key] = value._asdict()
        return result