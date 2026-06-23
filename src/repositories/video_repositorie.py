from config.database import connect_db
from src.models.video import Video

class VideoRepository:
    def __init__(self):
        self.connection = connect_db()

    def create_video(self, title: str, description: str, category: str, url: str) -> Video:
        cursor = self.connection.cursor()
        query = "INSERT INTO videos (title, description, category, url) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (title, description, category, url))
        self.connection.commit()
        cursor.close()

    def get_video_by_id(self, video_id: int) -> Video:
        cursor = self.connection.cursor()
        query = "SELECT id, title, description, category, url FROM videos WHERE id = %s"
        cursor.execute(query, (video_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Video(id=result[0], title=result[1], description=result[2], category=result[3], url=result[4])
        return None
    
    def delete_video_by_id(self, video_id: int) -> bool:
        cursor = self.connection.cursor()
        query = "DELETE FROM videos WHERE id = %s"
        cursor.execute(query, (video_id,))
        self.connection.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        return deleted
    
    def get_videos_by_category(self, category: str) -> list[Video]:
        cursor = self.connection.cursor()
        query = "SELECT id, title, description, category, url FROM videos WHERE category = %s"
        cursor.execute(query, (category,))
        results = cursor.fetchall()
        cursor.close()
        return [Video(id=row[0], title=row[1], description=row[2], category=row[3], url=row[4]) for row in results]
    
    def get_all_videos_paginated(self, page: int, page_size: int) -> list[Video]:
        cursor = self.connection.cursor()
        offset = (page - 1) * page_size
        query = "SELECT id, title, description, category, url FROM videos LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        results = cursor.fetchall()
        cursor.close()
        return [Video(id=row[0], title=row[1], description=row[2], category=row[3], url=row[4]) for row in results]
    
    def get_videos_by_user_id(self, user_id: int) -> list[Video]:
        cursor = self.connection.cursor()
        query = "SELECT id, title, description, category, url FROM videos WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        cursor.close()
        return [Video(id=row[0], title=row[1], description=row[2], category=row[3], url=row[4]) for row in results]
    
    def get_videos_by_title(self, title: str) -> list[Video]:
        cursor = self.connection.cursor()
        query = "SELECT id, title, description, category, url FROM videos WHERE title LIKE %s"
        cursor.execute(query, (f"%{title}%",))
        results = cursor.fetchall()
        cursor.close()
        return [Video(id=row[0], title=row[1], description=row[2], category=row[3], url=row[4]) for row in results]
    
    def update_video(self, video_id: int, title: str, description: str, category: str, url: str) -> Video:
        cursor = self.connection.cursor()
        query = "UPDATE videos SET title = %s, description = %s, category = %s, url = %s WHERE id = %s"
        cursor.execute(query, (title, description, category, url, video_id))
        self.connection.commit()
        cursor.close()
        return self.get_video_by_id(video_id)
    
    def get_all_videos(self) -> list[Video]:
        cursor = self.connection.cursor()
        query = "SELECT id, title, description, category, url, created_at FROM videos"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return [Video(id=row[0], title=row[1], description=row[2], category=row[3], url=row[4], created_at=row[5]) for row in results]
    