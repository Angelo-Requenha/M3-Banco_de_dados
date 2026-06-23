from src.repositories.user_repositorie import UserRepository
from src.models.user import User

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, name: str, email: str, password: str):
        user = self.user_repository.create_user(name=name, email=email, password=password)
        return user

    def get_user_by_id(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        return user
    
    def get_user_by_email(self, email: str):
        user = self.user_repository.get_user_by_email(email)
        return user
    
    def update_user(self, user_id: int, name: str = None, email: str = None, password: str = None):
        user = self.user_repository.update_user(user_id=user_id, name=name, email=email, password=password)
        return user
    
    def delete_user_by_id(self, user_id: int):
        self.user_repository.delete_user_by_id(user_id)
    
    def login_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and user.password == password:
            return user
        return None
    
    def change_user_password(self, user_id: int, new_password: str):
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            user.password = new_password
            self.user_repository.update_user(user_id=user.id, name=user.name, email=user.email, password=new_password)
            return user
        return None
    
    def get_all_users(self):
        users = self.user_repository.get_all_users()
        return users