from config.database import connect_db
from src.models.user import User

class UserRepository:
    def __init__(self):
        self.connection = connect_db()

    def create_user(self, name: str, email: str, password: str):
        cursor = self.connection.cursor()
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        self.connection.commit()
        cursor.close()

    def get_user_by_id(self, user_id: int) -> User:
        cursor = self.connection.cursor()
        query = "SELECT id, username, email, password FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return User(id=result[0], name=result[1], email=result[2], password=result[3])
        return None
    
    def delete_user_by_id(self, user_id: int):
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        self.connection.commit()
        cursor.close()

    def update_user(self, user_id: int, name: str = None, email: str = None, password: str = None):
        cursor = self.connection.cursor()
        query = "UPDATE users SET "
        params = []
        if name:
            query += "username = %s, "
            params.append(name)
        if email:
            query += "email = %s, "
            params.append(email)
        if password:
            query += "password = %s, "
            params.append(password)
        query = query.rstrip(", ")
        query += " WHERE id = %s"
        params.append(user_id)
        cursor.execute(query, tuple(params))
        self.connection.commit()
        cursor.close()

    def get_user_by_email(self, email: str) -> User:
        cursor = self.connection.cursor()
        query = "SELECT id, username, email, password, created_at FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return User(id=result[0], name=result[1], email=result[2], password=result[3], created_at=result[4])
        return None
    
    def get_all_users(self)  -> list[User]:
        cursor = self.connection.cursor()
        query = "SELECT id, username, email, password, created_at FROM users"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return [User(id=row[0], name=row[1], email=row[2], password=row[3], created_at=row[4]) for row in results]