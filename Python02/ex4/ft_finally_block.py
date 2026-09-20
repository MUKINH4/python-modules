class PlantError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)
        self.message = message


def water_plant(plant_name: str):
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    print("Testing valid plants...")
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
    print("Closing watering system\n")

    print("Opening watering system")
    print("Testing invalid plants...")
    water_plant("Tomato")
    water_plant("lettuce")


def main():
    print("=== Garden Watering System ===\n")
    try:
        test_watering_system()
    except PlantError as error:
        print(f"Caught {error.__class__.__name__}: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
