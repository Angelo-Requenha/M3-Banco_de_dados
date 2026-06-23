from datetime import datetime

class Video:
    def __init__(self, id: int, title: str, description: str, category: str, url: str, created_at):
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.category: str = category
        self.url: str = url
        self.created_at: datetime = created_at

    def get_id(self) -> int:
        return self.id

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_category(self) -> str:
        return self.category
    
    def get_url(self) -> str:
        return self.url

    def get_created_at(self) -> datetime:
        return self.created_at
    