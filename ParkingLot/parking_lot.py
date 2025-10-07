from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from fee_strategy import FeeStrategy, FlatRateFeeStrategy
from parking_strategy import ParkingStrategy, NearestFirstStrategy
from vehicle import Vehicle
from typing import List, Dict, Optional


class ParkingLot:

    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a Singleton")
        self.floors: List[ParkingFloor] = []
        self.activeTickets: Dict[str, ParkingTicket] = {}
        self.fee_strategy = FlatRateFeeStrategy()
        self.parking_strategy = NearestFirstStrategy()

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def set_fee_strategy(self, fee_strategy: FeeStrategy):
        self.fee_strategy = fee_strategy

    def set_parking_strategy(self, parking_strategy: ParkingStrategy):
        self.parking_strategy = parking_strategy

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        spot = self.parking_strategy.find_spot(self.floors, vehicle)
        if spot is not None:
            spot.park_vehicle(vehicle)
            ticket = ParkingTicket(vehicle, spot)
            self.activeTickets[vehicle.get_license_number()] = ticket
            print(
                f"Vehicle {vehicle.get_license_number()} parked at spot {spot.get_spot_id()}"
            )
            return ticket
        else:
            print(f"No available spot for vehicle {vehicle.get_license_number()}")
            return None

    def unpark_vehicle(self, license_number: str) -> Optional[float]:
        ticket = self.activeTickets.pop(license_number, None)
        if ticket is None:
            print(f"Ticket not found for vehicle {license_number}")
            return None
        ticket.get_spot().unpark_vehicle()
        ticket.set_exit_timestamp()
        fee = self.fee_strategy.calculate_fee(ticket)
        print(
            f"Vehicle {license_number} unparked from spot {ticket.get_spot().get_spot_id()}"
        )
        return fee
