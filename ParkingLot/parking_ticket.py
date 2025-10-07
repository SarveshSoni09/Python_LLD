import uuid
import time
from vehicle import Vehicle
from parking_spot import ParkingSpot


class ParkingTicket:
    """Represents a ticket issued to a vehicle upon entering the parking lot."""

    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        """Initializes a new ticket with a unique ID, vehicle/spot info, and entry time."""
        self.ticket_id = str(uuid.uuid4())  # Generate a unique ID for the ticket
        self.vehicle = vehicle  # The vehicle associated with this ticket
        self.spot = spot  # The spot where the vehicle is parked
        self.entry_timestamp = int(time.time())  # Store entry time as a Unix timestamp
        self.exit_timestamp = 0  # Exit time is 0 until the vehicle unparks

    # Getter methods for ticket attributes
    def get_ticket_id(self) -> str:
        return self.ticket_id

    def get_vehicle(self) -> Vehicle:
        return self.vehicle

    def get_spot(self) -> ParkingSpot:
        return self.spot

    def get_entry_timestamp(self) -> int:
        return self.entry_timestamp

    def get_exit_timestamp(self) -> int:
        return self.exit_timestamp

    def set_exit_timestamp(self):
        """Sets the exit timestamp to the current time."""
        self.exit_timestamp = int(time.time())
