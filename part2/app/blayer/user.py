#user sending information to persistence level

from app.blayer.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self,first_name, last_name, email, password, is_admin = False):
        super().__init__()

        self.first_name = first_name  #user first name
        self.last_name = last_name   #user last name
        self.email = self._validate_email(email) #validate email
        self.password = password #store password
        self.is_admin = is_admin #admin permission

    @staticmethod
    def _validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        return email

    def to_dict (self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
        }
