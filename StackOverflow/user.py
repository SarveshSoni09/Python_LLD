import threading


class User:
    def __init__(self, user_id, email: str, name: str):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.reputation = 0
        self.lock = threading.Lock()

    def update_reputation(self, change):
        with self.lock:
            self.reputation += change

    # def get_user_id(self) -> str:
    #     return self.user_id

    # def get_name(self) -> str:
    #     return self.name

    # def get_reputation(self) -> int:
    #     return self.reputation
