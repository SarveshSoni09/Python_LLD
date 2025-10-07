# Import the Enum class
from enum import Enum


class VehicleSize(Enum):
    """
    An Enumeration to represent the different sizes of vehicles.
    Using an Enum provides type safety and prevents errors from using simple strings.
    """

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
