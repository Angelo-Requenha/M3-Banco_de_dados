from datetime import datetime

class User:
    def __init__(self, id: int, name: str, email: str, password: str, created_at):
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.password: str = password
        self.created_at: datetime = created_at

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password
    
    def get_created_at(self) -> datetime:
        return self.created_at
    