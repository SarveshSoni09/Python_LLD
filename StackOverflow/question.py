import uuid
from datetime import date
from answer import Answer
from comment import Comment
from tag import Tag
from vote import Vote
from typing import List


class Question:
    def __init__(self, title, content, author, tags):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.author = author
        self.creation_date = date.today()
        self.answers: List[Answer] = []
        self.comments: List[Comment] = []
        self.tags = tags
        self.votes = 0
        self.accepted_answer = None

    def add_answer(self, answer: Answer):
        self.answers.append(answer)

    def accept_answer(self, answer: Answer):
        self.accepted_answer = answer

    def vote(self, vote: Vote):
        pass

    def get_vote_count(self) -> int:
        return self.votes

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments(self) -> List:
        return self.comments

    def get_id(self) -> str:
        return self.id

    def get_author(self) -> str:
        return self.author

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content

    def get_tags(self) -> List:
        return self.tags
