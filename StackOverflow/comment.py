from datetime import datetime


class Comment:
    def __init__(self, comment_id, content, author):
        self.id = comment_id
        self.content = content
        self.author = author
        self.creation_date = datetime.now()

    # def get_id(self) -> str:
    #     return self.id

    # def get_author(self) -> str:
    #     return self.author

    # def get_content(self) -> str:
    #     return self.content
