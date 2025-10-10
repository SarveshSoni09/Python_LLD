# Import necessary classes from other modules
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from fee_strategy import FeeStrategy, FlatRateFeeStrategy
from parking_strategy import ParkingStrategy, NearestFirstStrategy
from vehicle import Vehicle
from typing import List, Dict, Optional
import threading


class ParkingLot:
    """
    A Singleton class representing the entire parking lot.
    It manages floors, active tickets, and strategies for parking and fees.
    """

    # Private class variable to hold the single instance
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        """
        Private constructor. Initializes the parking lot's state.
        Raises an exception if an instance already exists.
        """
        if ParkingLot._instance is not None:
            raise Exception(
                "This class is a Singleton. Use get_instance() to get the object."
            )
        self.floors: List[ParkingFloor] = []  # A list to hold all the parking floors
        self.activeTickets: Dict[str, ParkingTicket] = (
            {}
        )  # A dictionary to track active tickets by license number
        self.fee_strategy: FeeStrategy = (
            FlatRateFeeStrategy()
        )  # Default fee calculation strategy
        self.parking_strategy: ParkingStrategy = (
            NearestFirstStrategy()
        )  # Default spot-finding strategy
        self._main_lock = threading.Lock()

    @staticmethod
    def get_instance():
        """
        Static method to access the singleton instance.
        Creates the instance if it doesn't exist yet.
        """
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def add_floor(self, floor: ParkingFloor):
        """Adds a new parking floor to the lot."""
        self.floors.append(floor)

    def set_fee_strategy(self, fee_strategy: FeeStrategy):
        """Allows changing the fee calculation strategy at runtime."""
        self.fee_strategy = fee_strategy

    def set_parking_strategy(self, parking_strategy: ParkingStrategy):
        """Allows changing the spot-finding strategy at runtime."""
        self.parking_strategy = parking_strategy

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        """
        Finds a spot for a vehicle using the current parking strategy,
        parks the vehicle, and issues a ticket.
        Returns the ticket on success, None on failure.
        """
        with self._main_lock:
            # Delegate the task of finding a spot to the current strategy object
            spot = self.parking_strategy.find_spot(self.floors, vehicle)
            if spot is not None:
                spot.park_vehicle(vehicle)  # Occupy the spot
                # Create a new ticket for this parking session
                ticket = ParkingTicket(vehicle, spot)
                self.activeTickets[vehicle.get_license_number()] = (
                    ticket  # Store the active ticket
                )
                print(
                    f"Vehicle {vehicle.get_license_number()} parked at spot {spot.get_spot_id()}"
                )
                return ticket
            else:
                print(f"No available spot for vehicle {vehicle.get_license_number()}")
                return None

    def unpark_vehicle(self, license_number: str) -> Optional[float]:
        """
        Unparks a vehicle using its license number, calculates the fee,
        and frees the spot.
        Returns the calculated fee on success, None if the ticket is not found.
        """
        with self._main_lock:
            # Remove the ticket from active tickets; returns None if not found
            ticket = self.activeTickets.pop(license_number, None)
            if ticket is None:
                print(f"Ticket not found for vehicle {license_number}")
                return None

            ticket.get_spot().unpark_vehicle()  # Free up the parking spot
            ticket.set_exit_timestamp()  # Record the exit time

            # Delegate fee calculation to the current fee strategy object
            fee = self.fee_strategy.calculate_fee(ticket)
            print(
                f"Vehicle {license_number} unparked from spot {ticket.get_spot().get_spot_id()}"
            )
            return fee
