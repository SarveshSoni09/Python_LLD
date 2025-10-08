import uuid
from datetime import date
from answer import Answer
from comment import Comment
from post import Post
from tag import Tag
from vote import Vote
from typing import List


class Question(Post):
    def __init__(self, post_id, title, content, author, tags):
        super().__init__(post_id, content, author)
        self.title = title
        self.answers: List[Answer] = []
        self.tags = tags if tags else []

    def add_answer(self, answer: Answer):
        with self.lock:
            self.answers.append(answer)

    # def accept_answer(self, answer: Answer):
    #     self.accepted_answer = answer

    # def vote(self, vote: Vote):
    #     pass

    # def get_vote_count(self) -> int:
    #     return self.votes

    # def add_comment(self, comment: Comment):
    #     self.comments.append(comment)

    # def get_comments(self) -> List:
    #     return self.comments

    # def get_id(self) -> str:
    #     return self.id

    # def get_author(self) -> str:
    #     return self.author

    # def get_title(self) -> str:
    #     return self.title

    # def get_content(self) -> str:
    #     return self.content

    # def get_tags(self) -> List:
    #     return self.tags
