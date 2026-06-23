from src.repositories.history_repositorie import HistoryRepository

class HistoryService:
    def __init__(self):
        self.history_repository = HistoryRepository()

    def create_history(self, user_id: int, video_id: int):
        history = self.history_repository.create_history(user_id, video_id)
        return history

    def get_history_by_user_id(self, user_id: int):
        history_list = self.history_repository.get_history_by_user_id(user_id)
        return history_list
    
    def delete_history_by_id(self, history_id: int):
        self.history_repository.delete_history_by_id(history_id)
    
    def delete_history_by_user_id(self, user_id: int):
        self.history_repository.delete_history_by_user_id(user_id)

    def get_history_by_user_id(self, user_id: int):
        history_list = self.history_repository.get_history_by_user_id(user_id)
        return history_list
    
    def get_history_by_video_id(self, video_id: int):
        history_list = self.history_repository.get_history_by_video_id(video_id)
        return history_list
    
    def get_all_history(self):
        history_list = self.history_repository.get_all_history()
        return history_list