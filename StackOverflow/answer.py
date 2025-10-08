from question import Question
from comment import Comment
from vote import Vote
from post import Post
from datetime import date
import uuid
from typing import List


class Answer(Post):
    def __init__(self, post_id, content, author, question):
        super().__init__(post_id, content, author)
        self.question = question
        # self.is_accepted = False
        # self.creation_date = date.today()
        # self.comments: List[Comment] = []
        # self.votes = 0

    # def vote(self):
    #     pass

    # def get_vote_count(self) -> int:
    #     return self.votes

    # def add_comment(self, comment: Comment):
    #     self.comments.append(comment)

    # def get_comments(self) -> List[Comment]:
    #     return self.comments

    # def get_question(self) -> Question:
    #     return self.question

    # def mark_as_accepted(self):
    #     self.is_accepted = True

    # def get_id(self) -> str:
    #     return self.id

    # def get_author(self) -> str:
    #     return self.author

    # def get_content(self) -> str:
    #     return self.content

    # def get_is_accepted(self) -> bool:
    #     return self.is_accepted
