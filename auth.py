from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    """Simple User class"""

    users = {
        '1': {
            'id': '1',
            'username': 'admin',
            'password': generate_password_hash('admin123')
        }
    }

    def __init__(self, user_id):
        self.id = user_id
        user_date = self.users.get(user_id)
        if user_date:
            self.username = user_date['username']

    @classmethod
    def get(cls, user_id):
        if user_id in cls.users:
            return cls(user_id)
        return None
    
    @classmethod
    def authenticate(cls, username, password):
        """Testify username and password"""
        for user_id, user_date in cls.users.items():
            if user_date['username'] == username and check_password_hash(user_date['password'], password):
                return cls(user_id)
        return None
    