from abc import ABC, abstratmethod

#creating the storage template for the repositories

class Repository(ABC):

    @abstractmethod
    def add(self.obj): pass

    @abstractmethod
    def get(self, obj_id):pass

    @abstractmethod
    def get_all(self): pass

    @abstratmethod
    def update(self, obj_id, data): pass

    @abstractmethod
    def delete(self, obj_id):pass

    @abstratmethod
    def get_by_attribute(self, attr_name, attr_value): pass

#Storage in the form of a Python dictionary

class InMemoryRepository (Repository):

    def__init__(self):
        self._storage = {}

    def add (self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._sotrage.values())
    
    def update(self, obj_id, data):
        obj =self.get(obj_id)
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        return next (
                (obj for obj in self._storage.values()
                 if getattr(obj, attr_name, None) == attr_value),
                 None
            )
