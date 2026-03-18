#Entry point between API layer and business logic

from app.persistence.repsoitory import InMemoryRepository
from app.blayer.user import User
from app.blayer.place import Place
from app.blayer.review import Review
from app.blayer.amenity import Amenity

class Facade:
   
    def __init__(self):

        #repository instances for each entity
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

# **data = dictionary unpacking - unpacks data dictiony into the User cosntructor as individual named arguments

    #User

    def create user (self,data):  #creates a user and returns the user information
        user = User(**data) 
        self.user_repo.add(user)
        return user  
    
    def get_user(self, user_id): # Looks up a single user by their unique id; returns what's in storage field or NONE if not found
        return self.user_repo.get(user_id)

    def get_user_by_email(self,email): #Looks up a single user by their email address; returns user with matching email field
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self): #Pulls every user that's in storage; returns the full list
        return self.user_repo.get_all()

    def update_user(self, user_id, data):  #Updates existing user with new info; Returns updated user info
        self.user_repo.update(user_id, data)
        return self.user_repo.get(user_id)

    #Amenities

    def create_amentiry (self, data):  #Creates amenities and retursn amenity information
        amenity = Amenity(**data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amentiy_id): #Looks amenity by its unique id; Returns what's in storage
        return self.amenity_repo.get(amentiy_id)

    def get_all_amenities(self): #Gets every amenity in storage; Returns the full list of amenities
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, data): #Updates an existing amentiy with new info
        self.amenity_repo.update(amenity_id, data)
        return self.amentiy_repo.get(amenity_id)

    #Place

    def create_place(self, data): #Creates a place and returns the place info
        place = Place(**data)
        self.place_repo.add(place)
        return place

    def get_place(self,place_id): #Looks up a single palce by its unique ID
        return self.place_repo.get_all()

    def get_all_places(self): #Gets every place and returns the full list
        return self.place_repo.get_all()

    def update_place(self,place_id, data): #Updates the existing place with new info
        self.place_repo.update(place_id, data)
        return self.place_repo.get(place_id)

    #Reviews

    def create_review(self, data): #creates a revew and saves it in storage
        review = Review (**data)
        self.review_repo.add(review)
        return review

    def get_review (self, review_id) #Looks up a review by its unique ID
        return self.review_repo.get(review_id)

    def get_all_reviews (self): #Gets every review in storage
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id): #Get only a review tied to the specifc place - captured by the place ID
        return [r for r in self.review_repo.get_all() if r.place_id == place_id]

    def update_review(self, review_id, data): #Updates an existing review with new info
        self.review_repo.update(review_id, data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id): #Delete review
        self.review_repo.delete(review_id)

