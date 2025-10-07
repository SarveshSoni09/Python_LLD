# Import the parent Vehicle class and the VehicleSize enum
from vehicle import Vehicle
from vehicle_size import VehicleSize


class Truck(Vehicle):
    """A concrete implementation of a Vehicle, representing a truck."""

    def __init__(self, license_number: str):
        """
        Initializes a Truck.
        Calls the parent constructor with a hardcoded size of LARGE.
        """
        super().__init__(license_number, VehicleSize.LARGE)
