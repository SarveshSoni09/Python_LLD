from question import Question
from comment import Comment
from vote import Vote
from datetime import date
import uuid
from typing import List


class Answer:
    def __init__(self, content, author, question):
        self.id = str(uuid.uuid4())
        self.content = content
        self.author = author
        self.question = question
        self.is_accepted = False
        self.creation_date = date.today()
        self.comments: List[Comment] = []
        self.votes = 0

    def vote(self):
        pass

    def get_vote_count(self) -> int:
        return self.votes

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments(self) -> List[Comment]:
        return self.comments

    def get_question(self) -> Question:
        return self.question

    def mark_as_accepted(self):
        self.is_accepted = True

    def get_id(self) -> str:
        return self.id

    def get_author(self) -> str:
        return self.author

    def get_content(self) -> str:
        return self.content

    def get_is_accepted(self) -> bool:
        return self.is_accepted
