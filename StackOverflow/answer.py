# Imports the Post class, which will serve as the base class for this Answer.
from post import Post


# Defines an Answer to a question.
# An Answer is a type of Post, so it inherits all the properties of a Post
# (like content, author, votes, comments) and adds its own specific details.
class Answer(Post):
    def __init__(self, post_id, content, author, question):
        """
        Initializes an Answer object.

        Args:
            post_id: The unique identifier for this answer.
            content: The text content of the answer.
            author: The User object who wrote the answer.
            question: The Question object that this answer is associated with.
        """
        # Call the constructor of the parent Post class to initialize common attributes.
        super().__init__(post_id, content, author)

        # Store a reference to the parent question this answer belongs to.
        self.question = question
