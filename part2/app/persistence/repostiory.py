from abc import ABC, abstractmethod

##consistent interface regardless of storage backend#

class Repository (ABC):
    @abstractmethod
    def add (self, obj) : pass

    @abstratmethod
    def get_all (self, obj_id): pass

    @abstractmethod
    def get_all (self): pass

    @abstractmethod
    def update (self, obj_id, data): pass

    @abstractmethod
    def delete (self, obj_id): pass

    @abstractmethod
    def get_by_attribute (self, attr_name, attr_value): pass


class InMemoryRepository (Repository):
    def__init__(self):
        ##for the database##

 def add (self, obj):
        ##storing the object where its id is the key##

    def get(self, obj_id):
        ##will return none if the key does not exist##

    def get_all(self):
        ##returns stored objects as a list##
        return list (self._storage.values())

    def update (self, obj_id, data):
        ##calls update() method ##

        obj = self.get (obj_id)
        if obj:
            obj.update(data)

    def delete (self, obj_id):
        if obj_id in self._storage:
            del self._storage [obj_id]

    def get_by_attribute (self, attr_name, attr_value):
        ## looks through all objects and returns the first match##

  ## next () returns NONE (by default) if there isn't a match##
        return nest
               (
                (obj for obj in self._storage,values ()
                 if getattr (obj. attr_name, None) == attr_value),

                None
                )

