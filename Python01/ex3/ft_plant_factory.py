class Plant:

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        print('Created: ', end='')
        self.show()

    def show(self) -> None:
        print(f'{self.name}: {round(self.height, 1)}cm,',
              f'{self.plant_age} days old')

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1


def main():
    plants_dict: list[dict[str, any]] = [
        {"name": "Rose", "height": 25.0, "plant_age": 30},
        {"name": "Oak", "height": 200.0, "plant_age": 365},
        {"name": "Cactus", "height": 5.0, "plant_age": 90},
        {"name": "Sunflower", "height": 80.0, "plant_age": 45},
        {"name": "Fern", "height": 15.0, "plant_age": 120},
    ]
    print("=== Plant Factory Output ===")
    for plant in plants_dict:
        plant = Plant(plant["name"], plant["height"], plant["plant_age"])


if __name__ == "__main__":
    main()
