from user import User
from question import Question
from answer import Answer
from comment import Comment
from vote import Vote
from vote_type import VoteType
from tag import Tag
import threading
import uuid


class StackOverflow:

    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if StackOverflow._instance is not None:
            raise Exception("This class is a Singleton")
        # self.users: List[User] = []
        # self.questions: List[Question] = []
        # self.answers: List[Answer] = []
        # self.comments: List[Comment] = []
        # self.tags: List[Tag] = []
        self.questions = {}
        self.users = {}
        self.tags = {}

    @staticmethod
    def get_instance():
        if StackOverflow._instance is None:
            StackOverflow._instance = StackOverflow()
        return StackOverflow._instance

    def create_user(self, username, email):
        user_id = uuid.uuid4()
        user = User(user_id, username, email)
        self.users[user_id] = user
        return user

    def post_question(self, author_id, title, content, tag_names=None):
        author = self.users[author_id]
        question_tags = []
        if tag_names:
            for name in tag_names:
                tag = self.tags.get(name.lower())
                if not tag:
                    tag = Tag(uuid.uuid4(), name.lower())
                    self.tags[name.lower()] = tag
                question_tags.append(tag)
        question_id = uuid.uuid4()
        question = Question(question_id, title, content, author, question_tags)
        self.questions[question_id] = question
        return question

    def post_answer(self, author_id, question_id, content):
        author, question = self.users[author_id], self.questions[question_id]
        answer_id = uuid.uuid4()
        answer = Answer(answer_id, content, author, question)
        question.add_answer(answer)
        return answer

    def vote(self, user_id, post_id, vote_type):
        post = self.questions.get(post_id)
        if not post:
            for q in self.questions.values():
                for a in q.answers:
                    if a.id == post_id:
                        post = a
                        break
                if post:
                    break
        if not post:
            raise ValueError("Post not found.")

        user = self.users[user_id]
        post.add_vote(Vote(user, vote_type))
        if vote_type == VoteType.UPVOTE:
            post.author.update_reputation(10)
        elif vote_type == VoteType.DOWNVOTE:
            post.author.update_reputation(-2)
            user.update_reputation(-1)

    def add_comment(self, author_id, post_id, content):
        if author_id not in self.users:
            raise ValueError("User not found.")
        author = self.users[author_id]

        # Find the post (question or answer)
        post = self.questions.get(post_id)
        if not post:
            for q in self.questions.values():
                for a in q.answers:
                    if a.id == post_id:
                        post = a
                        break
                if post:
                    break

        if not post:
            raise ValueError("Post not found.")

        comment_id = uuid.uuid4()
        comment = Comment(comment_id, content, author)
        post.add_comment(comment)
        return comment

    def search(self, keyword):
        results, keyword_lower = [], keyword.lower()
        for q in self.questions.values():
            if (
                keyword_lower in q.title.lower()
                or keyword_lower in q.content.lower()
                or any(keyword_lower in t.name for t in q.tags)
            ):
                results.append(q)
        return results
