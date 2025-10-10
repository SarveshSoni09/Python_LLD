# Defines a Tag, which is used to categorize questions.
# This is a simple data class.
class Tag:
    def __init__(self, tag_id, name):
        """
        Initializes a Tag object.

        Args:
            tag_id: The unique identifier for the tag.
            name: The name of the tag (e.g., "python").
        """
        self.id = tag_id
        self.name = name
