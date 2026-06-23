from src.repositories.video_repositorie import VideoRepository

class VideoService:
    def __init__(self):
        self.video_repository = VideoRepository()

    def create_video(self, title: str, description: str, category: str, url: str):
        video = self.video_repository.create_video(title, description, category, url)
        return video

    def get_video_by_id(self, video_id: int):
        video = self.video_repository.get_video_by_id(video_id)
        return video

    def get_all_videos(self):
        videos = self.video_repository.get_all_videos()
        return videos
    
    def get_videos_by_category(self, category: str):
        videos = self.video_repository.get_videos_by_category(category)
        return videos
    
    def delete_video_by_id(self, video_id: int):
        deleted = self.video_repository.delete_video_by_id(video_id)
        return deleted
    
    def update_video(self, video_id: int, title: str, description: str, category: str, url: str):
        updated_video = self.video_repository.update_video(video_id, title, description, category, url)
        return updated_video
    
    def get_videos_by_user_id(self, user_id: int):
        videos = self.video_repository.get_videos_by_user_id(user_id)
        return videos
    
    def get_videos_by_title(self, title: str):
        videos = self.video_repository.get_videos_by_title(title)
        return videos
    
    def get_all_videos_paginated(self, page: int, page_size: int):
        videos = self.video_repository.get_all_videos_paginated(page, page_size)
        return videos
    