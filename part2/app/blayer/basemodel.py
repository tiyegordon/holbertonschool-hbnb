#Parent class - user, place, review, amenity inherit the user id, date created and date updated

import uuid
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4()) #generates a new id for every object created
        self.created_at = datetime.utcnow() #captures the time object is created
        self.updated_at = datetime.utcnow() #captures the time an object is updated

    def update(self, data: dict):
        for key, value in data.items():

            #prevents id and created date from being changed

            if key not in ('id', 'created+at'):
                setattr(self, key, value)

            #updates the timestamp to right now

            self.updated_at = datetime.utcnow()

