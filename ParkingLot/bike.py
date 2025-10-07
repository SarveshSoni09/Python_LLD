# Import the parent Vehicle class and the VehicleSize enum
from vehicle import Vehicle
from vehicle_size import VehicleSize


class Bike(Vehicle):
    """A concrete implementation of a Vehicle, representing a bike."""

    def __init__(self, license_number: str):
        """
        Initializes a Bike.
        Calls the parent constructor with a hardcoded size of SMALL.
        """
        super().__init__(license_number, VehicleSize.SMALL)
