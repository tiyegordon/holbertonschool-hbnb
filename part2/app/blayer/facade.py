#facade instructions for handling user operations

from app.persistence.repository import InMemoryRepository
from app. blayer.user import User
from app.blayer. place import Place
from app.blayer.review import Review
from app.blayer .amenity import Amenity


class Facade:
    def __init__(self):

        #created storage for each entity0

        self.user_repo = InMemoryRepsotiroy()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
