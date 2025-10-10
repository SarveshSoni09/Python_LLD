# Imports the threading module for creating locks.
import threading


# Defines a User of the system.
class User:
    def __init__(self, user_id, email: str, name: str):
        """
        Initializes a User object.

        Args:
            user_id: The unique identifier for the user.
            email: The user's email address.
            name: The user's display name.
        """
        self.user_id = user_id
        self.email = email
        self.name = name
        self.reputation = 0  # All users start with 0 reputation.
        # A lock to ensure reputation updates are thread-safe.
        self.lock = threading.Lock()

    def update_reputation(self, change):
        """Atomically updates the user's reputation score."""
        with self.lock:
            self.reputation += change
