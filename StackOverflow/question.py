# Import necessary classes for type hinting and functionality.
from answer import Answer
from post import Post
from typing import List


# Defines a Question, which is a specific type of Post.
# It inherits from Post and adds properties unique to questions, like a title and tags.
class Question(Post):
    def __init__(self, post_id, title, content, author, tags):
        """
        Initializes a Question object.

        Args:
            post_id: The unique ID for the question.
            title: The title of the question.
            content: The detailed body of the question.
            author: The User who posted the question.
            tags: A list of Tag objects associated with the question.
        """
        # Initialize the base Post attributes.
        super().__init__(post_id, content, author)

        self.title = title
        # Type hint to indicate this will be a list of Answer objects.
        self.answers: List[Answer] = []
        # Store the list of tags, defaulting to an empty list if none are provided.
        self.tags = tags if tags else []

    def add_answer(self, answer: Answer):
        """Thread-safely adds an Answer to this question."""
        with self.lock:
            self.answers.append(answer)
