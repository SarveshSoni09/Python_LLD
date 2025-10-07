from abc import ABC, abstractmethod
from parking_floor import ParkingFloor
from vehicle import Vehicle
from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from typing import List, Optional


class ParkingStrategy(ABC):
    """
    Abstract Base Class for defining different strategies to find a parking spot.
    This is an implementation of the Strategy Design Pattern.
    """

    @abstractmethod
    def find_spot(
        self, floors: List[ParkingFloor], vehicle: Vehicle
    ) -> Optional[ParkingSpot]:
        """The method that each concrete strategy must implement."""
        pass


class NearestFirstStrategy(ParkingStrategy):
    """A concrete strategy that finds a spot on the lowest possible floor."""

    def find_spot(
        self, floors: List[ParkingFloor], vehicle: Vehicle
    ) -> Optional[ParkingSpot]:
        # Iterate through floors from the first to the last
        for floor in floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot  # Return the first spot found
        return None


class FarthestFirstStrategy(ParkingStrategy):
    """A concrete strategy that finds a spot on the highest possible floor."""

    def find_spot(
        self, floors: List[ParkingFloor], vehicle: Vehicle
    ) -> Optional[ParkingSpot]:
        # Iterate through floors from the last to the first by reversing the list
        for floor in reversed(floors):
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot  # Return the first spot found from the top
        return None


class BestFitStrategy(ParkingStrategy):
    """
    A concrete strategy that searches all floors to find the most size-appropriate
    (i.e., smallest possible) spot in the entire lot.
    """

    def find_spot(
        self, floors: List[ParkingFloor], vehicle: Vehicle
    ) -> Optional[ParkingSpot]:
        best_spot: Optional[ParkingSpot] = None

        # Iterate through every floor to find all potential spots
        for floor in floors:
            spot_on_this_floor = floor.find_available_spot(vehicle)

            if spot_on_this_floor is not None:
                # If this is the first spot we've found, it's the best so far
                if best_spot is None:
                    best_spot = spot_on_this_floor
                else:
                    # If the new spot is a tighter fit than the current best spot, update it
                    if (
                        spot_on_this_floor.get_spot_size().value
                        < best_spot.get_spot_size().value
                    ):
                        best_spot = spot_on_this_floor
        return best_spot
