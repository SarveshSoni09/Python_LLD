import uuid


class User:
    def __init__(self, email: str, name: str):
        self.user_id = str(uuid.uuid4())
        self.email = email
        self.name = name
        self.reputation = 0

    def update_reputation(self):
        pass

    def get_user_id(self) -> str:
        return self.user_id

    def get_name(self) -> str:
        return self.name

    def get_reputation(self) -> int:
        return self.reputation
