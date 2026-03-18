from app.blayer.base_model import BaseModel

class Amenity(BaseModel):
   
    #BaseModel to set ID and timestamp for Amenity

    def __init__(self,name):
        super(),__init__()

        self.name = name

    def to_dict(self):
    # convert to dictionary for API response

        return{
                'id': self.id,
                'name': self.name
            }
