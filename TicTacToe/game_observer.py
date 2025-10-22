from abc import ABC, abstractmethod


class GameObserver(ABC):
    """
    OBSERVER INTERFACE (Observer Design Pattern):
    This Abstract Base Class defines the contract for any class that wishes to
    be notified of state changes in the Game (Subject).

    LOOSE COUPLING:
    The Subject (Game) only needs to know that an Observer has an 'update' method;
    it doesn't need to know how the Scoreboard or any other observer handles the event.
    """

    @abstractmethod
    def update(self, game):
        # The update method is the mechanism for the Subject to notify the Observer.
        # It passes the game object (the Subject) so the Observer can query its final state.
        pass
