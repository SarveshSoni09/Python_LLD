import uuid
from datetime import datetime
import threading
from vote import Vote
from comment import Comment


class Post:
    def __init__(self, post_id, content, author) -> None:
        self.id = post_id
        self.content = content
        self.author = author
        self.votes = []
        self.comments = []
        self.creation_date = datetime.now()
        self.lock = threading.Lock()

    def add_vote(self, vote: Vote):
        with self.lock:
            self.votes.append(vote)

    def add_comment(self, comment: Comment):
        with self.lock:
            self.comments.append(comment)

    def get_vote_count(self):
        return sum(vote.vote_type.value for vote in self.votes)
