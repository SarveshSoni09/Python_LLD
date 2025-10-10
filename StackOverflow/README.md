# Stack Overflow System: Low-Level Design (LLD)

## 1. Project Overview

This document outlines the Low-Level Design (LLD) for a **Q&A Platform**, modeled after Stack Overflow. The system is designed to allow users to post questions, provide answers, engage in discussions through comments, and build a reputation based on community feedback. It emphasizes efficient searching, content organization via tags, and data consistency in a concurrent environment.

---

## 2. System Requirements

The design addresses the following core functional requirements:

1.  **Content Creation:** Users must be able to post **Questions**, **Answers**, and **Comments**.
2.  **Voting System:** The system must allow users to **upvote** and **downvote** questions and answers to signify quality.
3.  **Content Organization:** Questions must be categorized using one or more **Tags** for easy discovery.
4.  **Search Functionality:** Users must be able to search for questions based on **keywords**, **tags**, or **users**.
5.  **Reputation Management:** The system must track and assign a **reputation score** to users based on their contributions and the community's votes.
6.  **Concurrency:** The system must handle simultaneous user interactions (e.g., multiple users voting on the same answer) in a thread-safe manner.

---

## 3. Project Structure

The project is organized into modular, single-responsibility files:

/
|-- user.py # Defines the User class.
|-- post.py # Defines the Post base class.
|-- question.py # Defines the Question class, inheriting from Post.
|-- answer.py # Defines the Answer class, inheriting from Post.
|-- comment.py # Defines the Comment class.
|-- vote.py # Defines the Vote class.
|-- tag.py # Defines the Tag class.
|-- vote_type.py # Defines the VoteType enumeration.
|-- stack_overflow.py # The main Singleton controller class for the system.
|-- stack_overflow_demo.py # The executable script to demonstrate functionality.

---

## 4. Low-Level Components

The design is composed of the following core classes and enumerations:

### Classes

| Component               | Type  | Responsibility                                                                                                                                                    |
| :---------------------- | :---- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`StackOverflow`**     | Class | The **central facade** and **singleton instance** of the system. Manages users, questions, and tags, providing a simplified interface for all primary operations. |
| **`User`**              | Class | Represents a user account. Manages user details like name and email, and tracks their **reputation score** in a thread-safe manner.                               |
| **`Post`**              | Class | A **base class** for user-generated content. Contains shared attributes and methods for `Question` and `Answer`, such as handling votes and comments.             |
| **`Question`**          | Class | Inherits from `Post`. Represents a user-submitted question, containing a title, associated `Tag` objects, and a collection of `Answer` objects.                   |
| **`Answer`**            | Class | Inherits from `Post`. Represents a user-submitted answer to a `Question` and is linked back to its parent question.                                               |
| **`Comment`**           | Class | Represents a comment attached to a `Post` (either a `Question` or an `Answer`). Contains its text content and author.                                             |
| **`Tag`**               | Class | Represents a metadata tag used for categorizing questions.                                                                                                        |
| **`Vote`**              | Class | Represents a single upvote or downvote cast by a `User` on a `Post`.                                                                                              |
| **`StackOverflowDemo`** | Class | Contains the application entry point (`run` method) to demonstrate the creation and interaction of the system's components.                                       |

### Enumerations

| Enumeration    | Definition                                                                                                          |
| :------------- | :------------------------------------------------------------------------------------------------------------------ |
| **`VoteType`** | Defines the type of vote (`UPVOTE`, `DOWNVOTE`) with associated integer values (`+1`, `-1`) for calculating scores. |

---

## 5. Design Patterns & Concurrency

### Design Patterns Used

The design incorporates several key patterns:

1.  **Singleton Pattern:** Applied to the **`StackOverflow`** class.

    - **Rationale:** The system requires a single, globally accessible entry point (`get_instance()`) to manage the shared state of all questions and users. This ensures data consistency across the application.

2.  **Facade Pattern:** The **`StackOverflow`** class also acts as a facade.

    - **Rationale:** It provides a simplified, high-level API (e.g., `post_question()`, `add_comment()`) that hides the complex underlying interactions between the various model classes.

3.  **Inheritance (Polymorphism):** A `Post` base class is used for `Question` and `Answer`.
    - **Rationale:** This promotes code reuse by centralizing common logic, such as adding votes and comments, in the `Post` class. It allows methods like `vote()` and `add_comment()` to treat `Question` and `Answer` objects interchangeably.

### Concurrency Strategy

To ensure data integrity, critical sections that modify shared data are synchronized using `threading.Lock`.

Key synchronized operations include:

- **Casting a vote (`Post.add_vote`)**: Modifying a post's list of votes is an atomic operation.
- **Adding content (`Post.add_comment`, `Question.add_answer`)**: Modifying a post's list of comments or answers is atomic.
- **Updating reputation (`User.update_reputation`)**: A user's reputation score is updated atomically to prevent lost updates from simultaneous votes.
