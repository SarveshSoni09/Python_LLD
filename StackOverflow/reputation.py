class Reputation:
    def __init__(self):
        self.q_upvote = 0
        self.q_downvote = 0
        self.a_upvote = 0
        self.a_downvote = 0
        self.a_accepted = 0
        self.points = (
            self.q_upvote
            + self.q_downvote
            + self.a_upvote
            + self.a_downvote
            + self.a_accepted
        )

    def get_points(self) -> int:
        return self.points
