# Import the main controller class and the vote type enum for the demo.
from stack_overflow import StackOverflow
from vote_type import VoteType


# This class demonstrates the functionality of the Stack Overflow system.
class StackOverflowDemo:
    @staticmethod
    def run():
        """Executes a step-by-step demonstration of the system's features."""

        # Get the single instance of the StackOverflow system (Singleton pattern).
        so = StackOverflow.get_instance()
        print("Starting Stack Overflow Demo...")

        # STEP 1: Create several users to interact with the system.
        print("\n## 1. Creating Users ##")
        user_alice = so.create_user("Alice", "alice@example.com")
        user_bob = so.create_user("Bob", "bob@example.com")
        user_charlie = so.create_user("Charlie", "charlie@example.com")
        print(f"Users created: {user_alice.name}, {user_bob.name}, {user_charlie.name}")

        # Helper function to neatly display the current reputation of all users.
        def print_reputations():
            print("--- Reputation Report ---")
            for user in [user_alice, user_bob, user_charlie]:
                print(f"  - {user.name}: {user.reputation} reputation")
            print("-------------------------")

        print_reputations()

        # STEP 2: A user posts a new question.
        print("\n## 2. Alice Posts a Question ##")
        q1 = so.post_question(
            user_alice.user_id,
            "What are Python decorators?",
            "I'm new to Python and keep seeing the '@' symbol. What does it do?",
            ["python", "decorators", "metaprogramming"],
        )
        print(f"'{user_alice.name}' posted: '{q1.title}'")

        # STEP 3: Another user provides an answer to the question.
        print("\n## 3. Bob Answers the Question ##")
        a1 = so.post_answer(
            user_bob.user_id,
            q1.id,
            "Decorators are functions that take another function as an argument to extend its behavior.",
        )
        print(f"'{user_bob.name}' answered the question.")

        # STEP 4: Users add comments to both the question and the answer.
        print("\n## 4. Users Add Comments ##")
        c1 = so.add_comment(
            user_charlie.user_id, q1.id, "Great question! I was wondering this too."
        )
        print(f"'{user_charlie.name}' commented on the QUESTION: '{c1.content}'")

        c2 = so.add_comment(user_alice.user_id, a1.id, "Thanks, Bob! That makes sense.")
        print(f"'{user_alice.name}' commented on Bob's ANSWER: '{c2.content}'")

        # STEP 5: Demonstrate the voting system and its effect on user reputation.
        print("\n## 5. Voting and Reputation Changes ##")
        print("Initial state before voting:")
        print_reputations()
        print(f"Bob's answer vote count: {a1.get_vote_count()}")

        print("\n--> Charlie UPVOTES Bob's answer (+10 to Bob)...")
        so.vote(user_charlie.user_id, a1.id, VoteType.UPVOTE)
        print_reputations()
        print(f"Bob's answer vote count: {a1.get_vote_count()}")

        print("\n--> Alice also UPVOTES Bob's answer (+10 to Bob)...")
        so.vote(user_alice.user_id, a1.id, VoteType.UPVOTE)
        print_reputations()
        print(f"Bob's answer vote count: {a1.get_vote_count()}")

        print("\n--> Charlie DOWNVOTES Bob's answer (-2 to Bob, -1 to Charlie)...")
        so.vote(user_charlie.user_id, a1.id, VoteType.DOWNVOTE)
        print_reputations()
        print(f"Bob's answer vote count: {a1.get_vote_count()}")

        # STEP 6: Display a summary of the question, its comments, and answers.
        print("\n## 6. Final State of Alice's Question ##")
        print("=====================================================================")
        print(f"Q: '{q1.title}' by {q1.author.name}")
        print(f"   Tags: {[tag.name for tag in q1.tags]}")
        print(f"   Content: {q1.content}")
        print("\n   --- Comments on Question ---")
        for comment in q1.comments:
            print(f"   - {comment.author.name}: '{comment.content}'")

        print("\n   --- Answers ---")
        for answer in q1.answers:
            print(f"   A: By {answer.author.name} (Votes: {answer.get_vote_count()})")
            print(f"      '{answer.content}'")
            print("      --- Comments on Answer ---")
            for comment in answer.comments:
                print(f"      - {comment.author.name}: '{comment.content}'")
        print("=====================================================================")

        print("\n Demo Complete.")


# This standard Python construct ensures the demo runs only when the script is executed directly.
if __name__ == "__main__":
    StackOverflowDemo.run()
