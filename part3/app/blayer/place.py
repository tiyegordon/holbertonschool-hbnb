from app.blayer.basemodel import BaseModel
from app.extensions import db
from app.blayer.association_tables import place_amenities
from typing import List

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relationships
    amenities = db.relationship('Amenity', secondary=place_amenities, lazy='subquery',
                              backref=db.backref('places', lazy=True))
    reviews = db.relationship('Review', backref='place', lazy=True, cascade='all, delete-orphan')

    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'amenities': [amenity.id for amenity in self.amenities] if self.amenities else [],
            'reviews': [review.id for review in self.reviews] if self.reviews else []
        }

