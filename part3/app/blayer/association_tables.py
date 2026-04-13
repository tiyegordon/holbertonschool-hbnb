from app.extensions import db

# Association table for many-to-many relationship between Place and Amenity
place_amenities = db.Table('place_amenities',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id')),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'))
)
