import time

# Assuming your file structure is flat, otherwise adjust imports
from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from parking_strategy import (
    NearestFirstStrategy,
    FarthestFirstStrategy,
    BestFitStrategy,
)
from bike import Bike
from car import Car
from truck import Truck


class AdvancedParkingLotDemo:

    @staticmethod
    def _display_lot_availability(parking_lot: ParkingLot):
        """Helper function to display availability for all floors."""
        print("--- Current Lot Availability ---")
        if not parking_lot.floors:
            print("No floors in the parking lot.")
            return
        for floor in parking_lot.floors:
            floor.display_availability()

    @staticmethod
    def _setup_parking_lot():
        """Creates a fresh parking lot instance with a standard layout."""
        print("--- 1. Setting up the Parking Lot ---")
        parking_lot = ParkingLot.get_instance()

        # Clear existing floors and tickets for a clean run
        parking_lot.floors.clear()
        parking_lot.activeTickets.clear()

        # Create 3 floors with a specific layout for testing strategies
        floor1 = ParkingFloor(1)
        floor1.add_spot(ParkingSpot("F1-S1", VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot("F1-M1", VehicleSize.MEDIUM))
        floor1.add_spot(ParkingSpot("F1-L1", VehicleSize.LARGE))

        floor2 = ParkingFloor(2)
        floor2.add_spot(ParkingSpot("F2-M1", VehicleSize.MEDIUM))
        floor2.add_spot(ParkingSpot("F2-M2", VehicleSize.MEDIUM))

        floor3 = ParkingFloor(3)
        floor3.add_spot(ParkingSpot("F3-S1", VehicleSize.SMALL))
        floor3.add_spot(ParkingSpot("F3-L1", VehicleSize.LARGE))

        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)
        parking_lot.add_floor(floor3)

        print("Parking Lot setup complete.\n")
        AdvancedParkingLotDemo._display_lot_availability(parking_lot)
        return parking_lot

    @staticmethod
    def run():
        """Runs the entire demonstration."""
        parking_lot = AdvancedParkingLotDemo._setup_parking_lot()

        # --- ACT 1: Demonstrate NearestFirstStrategy ---
        print("\n--- 2. DEMO: Nearest First Strategy ---")
        parking_lot.set_parking_strategy(NearestFirstStrategy())
        print("Strategy set to NearestFirst. A Car should park on Floor 1.")
        parking_lot.park_vehicle(Car("C-NEAR"))
        AdvancedParkingLotDemo._display_lot_availability(parking_lot)
        parking_lot.unpark_vehicle("C-NEAR")  # Clean up for next demo

        # --- ACT 2: Demonstrate FarthestFirstStrategy ---
        print("\n--- 3. DEMO: Farthest First Strategy ---")
        parking_lot.set_parking_strategy(FarthestFirstStrategy())
        print(
            "Strategy set to FarthestFirst. A Car should park on Floor 2 (as Floor 3 has no Medium spot)."
        )
        parking_lot.park_vehicle(Car("C-FAR"))
        AdvancedParkingLotDemo._display_lot_availability(parking_lot)
        parking_lot.unpark_vehicle("C-FAR")  # Clean up

        # --- ACT 3: Demonstrate BestFitStrategy ---
        print("\n--- 4. DEMO: Best Fit Strategy ---")
        parking_lot.set_parking_strategy(BestFitStrategy())
        print(
            "Strategy set to BestFit. A Car ('C-BESTFIT') should choose the Medium spot on F2 over the Large on F1."
        )
        # Temporarily occupy F1-M1 to create the scenario where F1's only fitting spot is Large
        parking_lot.park_vehicle(Bike("TEMP-BIKE"))
        parking_lot.park_vehicle(Car("C-BESTFIT"))
        AdvancedParkingLotDemo._display_lot_availability(parking_lot)
        parking_lot.unpark_vehicle("C-BESTFIT")
        parking_lot.unpark_vehicle("TEMP-BIKE")  # Clean up

        print("\n--- Final Lot Status (should be empty) ---")
        AdvancedParkingLotDemo._display_lot_availability(parking_lot)
        print("\n--- DEMO COMPLETE ---")


if __name__ == "__main__":
    AdvancedParkingLotDemo.run()
