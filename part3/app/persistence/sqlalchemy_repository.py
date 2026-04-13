from abc import ABC, abstractmethod
from typing import List, Any, Optional

#creating the storage template for the repositories

class Repository(ABC):

    @abstractmethod
    def add(self, obj) -> Any:
        pass

    @abstractmethod
    def get(self, obj_id) -> Optional[Any]:
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        pass

    @abstractmethod
    def update(self, obj_id, data) -> Optional[Any]:
        pass

    @abstractmethod
    def delete(self, obj_id) -> bool:
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value) -> Optional[Any]:
        pass

#Storage in the form of a Python dictionary

class InMemoryRepository (Repository):

    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())
     
    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            return obj
        return None

    def get_by_attribute(self, attr_name, attr_value):
        return next (
                (obj for obj in self._storage.values()
                 if getattr(obj, attr_name, None) == attr_value),
                None
            )

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]
            return True
        return False

