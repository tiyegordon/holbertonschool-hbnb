
from app.blayer.base_model import BaseModel

class Review(BaseModel):
    
    def__init__(self, text, rating, place_id, user_id):
        super().__init__()

        self.text = text #review content
        self.rating = rating #review rating
        self.place_id = place_id #review id tied to the place
        self.user_id = user_id #id of user who wrote the review

    def to_dict(self):
        
        #convert review to dictionary for API response
          
          return{
                'id': self.id,
                'text': self.text,
                'rating': self.rating,
                'place_id': self.place_id,
                'user_id': self.user_id,

            }

    

