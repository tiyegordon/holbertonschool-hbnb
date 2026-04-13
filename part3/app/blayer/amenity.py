from app.blayer.basemodel import BaseModel
from app.extensions import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
    # convert to dictionary for API response
        return{
                'id': self.id,
                'name': self.name
            }

