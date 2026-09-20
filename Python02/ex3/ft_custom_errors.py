class GardenError(Exception):

    def __init__(self, message="Unknown garden error"):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)
        self.message = message


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)
        self.message = message


class Plant:

    def __init__(self, name: str, is_wilting: bool):
        self.name = name
        self.is_wilting = is_wilting

    def check_wilting(self) -> None:
        if (self.is_wilting):
            raise PlantError(f"The {self.name} plant is wilting")
        else:
            print("Not wilting")

    @staticmethod
    def check_water_tank(water_quantity: float):
        tank_minimum: float = 5.0
        if (water_quantity <= tank_minimum):
            raise WaterError("Not enough water in the tank!")
        else:
            print("Enough water in the tank!")

    def water_plant(self, water_quantity: int):
        try:
            self.check_water_tank(water_quantity)
        except WaterError as error:
            raise GardenError(error.message)

    def expose_to_sun(self):
        try:
            self.check_wilting()
        except PlantError as error:
            raise GardenError(error.message)


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    plant = Plant("Tomato", True)
    try:
        print("Testing PlantError...")
        plant.check_wilting()
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}\n")
    try:
        print("Testing WatterError...")
        Plant.check_water_tank(1.0)
    except WaterError as error:
        print(f"Caught {error.__class__.__name__}: {error}\n")
    print("Testing catching all garden errors...")
    try:
        plant.expose_to_sun()
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
    try:
        plant.water_plant(3)
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
