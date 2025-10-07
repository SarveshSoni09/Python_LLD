# Import necessary classes and type hints
from abc import ABC
from vehicle_size import VehicleSize


class Vehicle(ABC):
    """
    Abstract Base Class representing a generic vehicle.
    It defines the common properties and methods that all specific vehicle types will have.
    """

    def __init__(self, license_number: str, size: VehicleSize):
        """Initializes a vehicle with its license number and size."""
        self.license_number = license_number
        self.size = size

    def get_license_number(self) -> str:
        """Returns the vehicle's license number."""
        return self.license_number

    def get_size(self) -> VehicleSize:
        """Returns the vehicle's size (SMALL, MEDIUM, or LARGE)."""
        return self.size
