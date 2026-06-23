from config.database import connect_db
from src.models.history import History

class HistoryRepository:
    def __init__(self):
        self.connection = connect_db()

    def create_history(self, history: History):
        cursor = self.connection.cursor()
        query = "INSERT INTO history (user_id, video_id) VALUES (%s, %s)"
        cursor.execute(query, (history.user_id, history.video_id))
        self.connection.commit()
        cursor.close()

    def get_history_by_user_id(self, user_id: int) -> list[History]:
        cursor = self.connection.cursor()
        query = "SELECT id, user_id, video_id FROM history WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        cursor.close()
        return [History(id=result[0], user_id=result[1], video_id=result[2]) for result in results]
    
    def delete_history_by_user_id(self, user_id: int):
        cursor = self.connection.cursor()
        query = "DELETE FROM history WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        self.connection.commit()
        cursor.close()

    def delete_history_by_id(self, history_id: int):
        cursor = self.connection.cursor()
        query = "DELETE FROM history WHERE id = %s"
        cursor.execute(query, (history_id,))
        self.connection.commit()
        cursor.close()

    def get_all_history(self) -> list[History]:
        cursor = self.connection.cursor()
        query = "SELECT id, user_id, video_id FROM history"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return [History(id=result[0], user_id=result[1], video_id=result[2]) for result in results]
    
    def get_history_by_video_id(self, video_id: int) -> list[History]:
        cursor = self.connection.cursor()
        query = "SELECT id, user_id, video_id FROM history WHERE video_id = %s"
        cursor.execute(query, (video_id,))
        results = cursor.fetchall()
        cursor.close()
        return [History(id=result[0], user_id=result[1], video_id=result[2]) for result in results]
    