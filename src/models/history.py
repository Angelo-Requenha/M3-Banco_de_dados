from datetime import datetime

class History:
    def __init__(self, id: int, user_id: int, video_id: int, timestamp: datetime):
        self.id: int = id
        self.user_id: int = user_id
        self.video_id: int = video_id
        self.timestamp: datetime = timestamp
    
    def get_id(self) -> int:
        return self.id

    def get_user_id(self) -> int:
        return self.user_id

    def get_video_id(self) -> int:
        return self.video_id
    
    def get_timestamp(self) -> datetime:
        return self.timestamp
    