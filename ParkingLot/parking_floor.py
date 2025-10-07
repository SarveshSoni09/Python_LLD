# Import necessary classes and type hints
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_size import VehicleSize
from typing import Dict, Optional, List
from collections import defaultdict


class ParkingFloor:
    """Represents a single floor in the parking lot, containing multiple parking spots."""

    def __init__(self, floor_number: int):
        """Initializes a floor with its number and an empty dictionary of spots."""
        self.floor_number = floor_number
        self.spots: Dict[str, ParkingSpot] = (
            {}
        )  # A dictionary to hold spots, keyed by spot ID

    def add_spot(self, spot: ParkingSpot):
        """Adds a parking spot to this floor."""
        self.spots[spot.get_spot_id()] = spot

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        """
        Finds the best-fitting available spot for a vehicle on this floor.
        It prioritizes the smallest possible spot that the vehicle can fit in.
        """
        # Filter for spots that are not occupied and can fit the vehicle
        available_spots = [
            spot
            for spot in self.spots.values()
            if not spot.is_occupied_spot() and spot.can_fit_vehicle(vehicle)
        ]

        if available_spots:
            # Sort the fitting spots by size (SMALL -> MEDIUM -> LARGE) to find the "best fit"
            available_spots.sort(key=lambda x: x.get_spot_size().value)
            return available_spots[0]  # Return the smallest fitting spot

        return None  # Return None if no suitable spot is found on this floor

    def display_availability(self):
        """Prints a summary of available spots on this floor, grouped by size."""
        print(f"--- Floor {self.floor_number} Availability ---")
        # Use defaultdict to easily count available spots of each size
        available_counts = defaultdict(int)

        for spot in self.spots.values():
            if not spot.is_occupied_spot():
                available_counts[spot.get_spot_size()] += 1

        # Print the count for each vehicle size
        for size in VehicleSize:
            print(f"  {size.name} spots: {available_counts[size]}")
