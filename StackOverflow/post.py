# Import necessary modules and classes.
import uuid
from datetime import datetime
import threading  # Used for thread-safe operations on shared data.
from vote import Vote
from comment import Comment


# Defines the base class for user-generated content like Questions and Answers.
# It contains shared functionality, such as handling votes and comments.
class Post:
    def __init__(self, post_id, content, author) -> None:
        """
        Initializes a Post object.

        Args:
            post_id: The unique identifier for the post.
            content: The main text content of the post.
            author: The User object who created the post.
        """
        self.id = post_id
        self.content = content
        self.author = author
        self.votes = []  # A list to store Vote objects.
        self.comments = []  # A list to store Comment objects.
        self.creation_date = datetime.now()

        # A lock to prevent race conditions when multiple users vote or comment
        # at the same time. This ensures data consistency.
        self.lock = threading.Lock()

    def add_vote(self, vote: Vote):
        """Thread-safely adds a vote to this post."""
        # The 'with' statement ensures the lock is automatically acquired and released.
        with self.lock:
            self.votes.append(vote)

    def add_comment(self, comment: Comment):
        """Thread-safely adds a comment to this post."""
        with self.lock:
            self.comments.append(comment)

    def get_vote_count(self):
        """Calculates and returns the net vote score (upvotes - downvotes)."""
        # Sums the integer values of the VoteType enum (+1 for upvote, -1 for downvote).
        return sum(vote.vote_type.value for vote in self.votes)
