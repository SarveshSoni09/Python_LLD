# Import all the data model classes that the system will manage.
from user import User
from question import Question
from answer import Answer
from comment import Comment
from vote import Vote
from vote_type import VoteType
from tag import Tag
import threading
import uuid


# The main controller class for the Stack Overflow system.
# It manages all data and operations.
# Implements the Singleton pattern to ensure only one instance of the system exists.
class StackOverflow:

    # Class-level variables to hold the single instance and a lock for thread-safe creation.
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        """Initializes the system's in-memory databases."""
        # This check prevents direct instantiation after the first object is created.
        if StackOverflow._instance is not None:
            raise Exception("This class is a Singleton")

        # Dictionaries to store objects, using their UUIDs as keys for fast lookups.
        self.questions = {}
        self.users = {}
        self.tags = {}

    @staticmethod
    def get_instance():
        """A static method to get the single, shared instance of the class."""
        if StackOverflow._instance is None:
            # This logic is simplified; a thread-safe version would use the lock.
            StackOverflow._instance = StackOverflow()
        return StackOverflow._instance

    def create_user(self, username, email):
        """Creates a new user and adds them to the system."""
        user_id = uuid.uuid4()
        user = User(user_id, username, email)
        self.users[user_id] = user
        return user

    def post_question(self, author_id, title, content, tag_names=None):
        """Creates a new question, manages its tags, and adds it to the system."""
        author = self.users[author_id]
        question_tags = []
        if tag_names:
            # Process each tag name.
            for name in tag_names:
                # Reuse existing tags or create a new one if it doesn't exist.
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
        """Creates a new answer and links it to its parent question."""
        author, question = self.users[author_id], self.questions[question_id]
        answer_id = uuid.uuid4()
        answer = Answer(answer_id, content, author, question)
        question.add_answer(answer)
        return answer

    def vote(self, user_id, post_id, vote_type):
        """Applies a vote to a post and updates user reputations."""
        # Find the post to be voted on (it could be a question or an answer).
        post = self.questions.get(post_id)
        if not post:
            # If not found in questions, search within the answers of each question.
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
        # Add the vote to the post's vote list.
        post.add_vote(Vote(user, vote_type))
        # Update reputations based on the vote type.
        if vote_type == VoteType.UPVOTE:
            post.author.update_reputation(10)  # Author gets +10
        elif vote_type == VoteType.DOWNVOTE:
            post.author.update_reputation(-2)  # Author gets -2
            user.update_reputation(-1)  # Voter loses -1

    def add_comment(self, author_id, post_id, content):
        """Adds a comment to a specific post."""
        if author_id not in self.users:
            raise ValueError("User not found.")
        author = self.users[author_id]

        # Logic to find the post is identical to the vote method.
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
        """Searches for questions based on a keyword in the title, content, or tags."""
        results, keyword_lower = [], keyword.lower()
        for q in self.questions.values():
            if (
                keyword_lower in q.title.lower()
                or keyword_lower in q.content.lower()
                or any(keyword_lower in t.name for t in q.tags)
            ):
                results.append(q)
        return results
