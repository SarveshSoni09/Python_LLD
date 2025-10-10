# Imports the datetime module to timestamp when a comment is created.
from datetime import datetime


# Defines a Comment that can be added to a Question or an Answer.
# This is a simple data class to hold information about a comment.
class Comment:
    def __init__(self, comment_id, content, author):
        """
        Initializes a Comment object.

        Args:
            comment_id: The unique identifier for this comment.
            content: The text content of the comment.
            author: The User object who wrote the comment.
        """
        self.id = comment_id
        self.content = content
        self.author = author
        # Automatically set the creation timestamp to the current time.
        self.creation_date = datetime.now()
