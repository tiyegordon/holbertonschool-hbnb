#Parent class - user, place, review, amenity inherit the user id, date created and date updated

from app.extensions import db
from datetime import datetime
import uuid

class BaseModel(db.Model):
    __abstract__ = True  # This makes it an abstract base class

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def update(self, data: dict):
        for key, value in data.items():
            # prevents id and created date from being changed
            if key not in ('id', 'created_at'):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()


