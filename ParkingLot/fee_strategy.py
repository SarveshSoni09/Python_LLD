# Import necessary classes and type hints
from abc import ABC, abstractmethod
from parking_ticket import ParkingTicket
from vehicle_size import VehicleSize


class FeeStrategy(ABC):
    """
    Abstract Base Class for defining different fee calculation strategies.
    This follows the Strategy Design Pattern, allowing the fee logic to be
    changed at runtime in the ParkingLot.
    """

    @abstractmethod
    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        """Calculates the parking fee based on the ticket details."""
        pass


class FlatRateFeeStrategy(FeeStrategy):
    """A concrete strategy that charges a single flat rate per hour for all vehicles."""

    # Class constant for the hourly rate
    RATE_PER_HOUR = 10.0

    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        """
        Calculates fee based on total hours parked, rounded up.
        Assumes timestamps are in milliseconds.
        """
        # Calculate duration in milliseconds
        duration_ms = (
            parking_ticket.get_exit_timestamp() - parking_ticket.get_entry_timestamp()
        )
        # Convert duration to hours, always rounding up to the next hour
        hours = (duration_ms // (1000 * 60 * 60)) + 1
        return hours * self.RATE_PER_HOUR


class VehicleBasedFeeStrategy(FeeStrategy):
    """A concrete strategy that charges different hourly rates based on vehicle size."""

    # A dictionary mapping each vehicle size to its specific hourly rate
    HOURLY_RATES = {
        VehicleSize.SMALL: 10.0,
        VehicleSize.MEDIUM: 20.0,
        VehicleSize.LARGE: 30.0,
    }

    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        """
        Calculates fee based on hours parked and the vehicle's size.
        Assumes timestamps are in milliseconds.
        """
        # Calculate duration in milliseconds
        duration_ms = (
            parking_ticket.get_exit_timestamp() - parking_ticket.get_entry_timestamp()
        )
        # Convert duration to hours, always rounding up
        hours = (duration_ms // (1000 * 60 * 60)) + 1

        # Get the vehicle from the ticket, then its size, and use it to look up the correct rate
        vehicle_size = parking_ticket.get_vehicle().get_size()
        return hours * self.HOURLY_RATES[vehicle_size]
