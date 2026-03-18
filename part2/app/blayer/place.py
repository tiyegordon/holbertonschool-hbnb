
from app.blayer.base_model import BaseModel

class Place(BaseModel):
#Calls BaseModel assigning place a unique ID and timestamps

    def __init__(self, title, description, price, latitude, longitude, owner_id):
        
        #Runs BaseModel's setup tog ive this object an id and timestamp

        super().__init__()

        self.title = title  #place name
        self.description = description #place description
        self.price = price #place price
        self.latitude = latitude #latitude cordinates for place
        self.longitude = longitude #place longitude cordinates
        self.owner_id = owner_id #place user ID

        self.amentities = [] #list of amenity ID attached to place
        self.reviews = [] # list of review ID attached to place

    def to_dict(self):
        
        #converts the Place object into a dictionay, sends back as JSON in the API response

        return{
                'id': self.id, 
                'title': self.title,
                'description': self.description,
                'price': self.price,
                'latitude': self.latitude,
                'longitude': self.longitude,
                'owner_id': self.owner_id,
                'amenities': self.amenities,
                'reviews': self.reviews
                
            }
