from abc import ABC, abstractmethod
from typing import List, Any, Optional
from app.persistence.repository import Repository

class SQLAlchemyRepository(Repository):
    """SQLAlchemy implementation of the Repository interface"""

    def __init__(self, model):
        self.model = model
        self.db = None

    def init_app(self, db):
        """Initialize the repository with database instance"""
        self.db = db

    def _get_db_session(self):
        """Get DB session"""
        if self.db is None:
            from app.extensions import db
            self.db = db
        return self.db.session

    def add(self, obj: Any) -> Any:
        """Add a new object to the database"""
        session = self._get_db_session()
        session.add(obj)
        session.commit()
        return obj

    def get(self, obj_id: Any) -> Optional[Any]:
        """Get an object by its ID"""
        session = self._get_db_session()
        return session.query(self.model).get(obj_id)

    def get_all(self) -> List[Any]:
        """Get all objects"""
        session = self._get_db_session()
        return session.query(self.model).all()

    def update(self, obj_id: Any, data: dict) -> Optional[Any]:
        """Update an object by ID"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            session = self._get_db_session()
            session.commit()
            return obj
        return None

    def delete(self, obj_id: Any) -> bool:
        """Delete an object by ID"""
        obj = self.get(obj_id)
        if obj:
            session = self._get_db_session()
            session.delete(obj)
            session.commit()
            return True
        return False

    def get_by_attribute(self, attr_name: str, attr_value: Any) -> Optional[Any]:
        """Get an object by a specific attribute"""
        session = self._get_db_session()
        return session.query(self.model).filter_by(**{attr_name: attr_value}).first()
