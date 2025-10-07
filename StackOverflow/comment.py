from datetime import date
import uuid


class Comment:
    def __init__(self, content, author):
        self.id = str(uuid.uuid4())
        self.content = content
        self.author = author
        self.creation_date = date.today()

    def get_id(self) -> str:
        return self.id

    def get_author(self) -> str:
        return self.author

    def get_content(self) -> str:
        return self.content
