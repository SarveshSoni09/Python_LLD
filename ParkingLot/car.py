# Import the parent Vehicle class and the VehicleSize enum
from vehicle import Vehicle
from vehicle_size import VehicleSize


class Car(Vehicle):
    """A concrete implementation of a Vehicle, representing a car."""

    def __init__(self, license_number: str):
        """
        Initializes a Car.
        Calls the parent constructor with a hardcoded size of MEDIUM.
        """
        super().__init__(license_number, VehicleSize.MEDIUM)
