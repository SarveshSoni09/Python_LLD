from user import User
from question import Question
from answer import Answer
from comment import Comment
from tag import Tag
from typing import List


class StackOverflow:

    _instance = None

    def __init__(self):
        if StackOverflow._instance is not None:
            raise Exception("This class is a Singleton")
        self.users: List[User] = []
        self.questions: List[Question] = []
        self.answers: List[Answer] = []
        self.comments: List[Comment] = []
        self.tags: List[Tag] = []

    @staticmethod
    def get_instance():
        if StackOverflow._instance is None:
            StackOverflow._instance = StackOverflow()
        return StackOverflow._instance

    def create_user(self, user: User):
        self.users.append(user)

    def post_question(self, question: Question):
        self.questions.append(question)

    def post_answer(self, answer: Answer):
        self.answers.append(answer)

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def vote(self):
        pass

    def accept_answer(self):
        pass

    def search_questions(self):
        pass

    def get_questions_by_user(self):
        pass
