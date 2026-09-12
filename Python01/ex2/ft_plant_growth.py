class Plant:

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.centimeters_growth: float = 0.0
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f'{self.name}: {round(self.height, 1)}cm,',
              f'{self.plant_age} days old')

    def grow(self) -> None:
        self.height += 0.8
        self.centimeters_growth += 0.8

    def age(self) -> None:
        self.plant_age += 1


def main() -> None:
    print('=== Garden Plant Growth ===')
    plant = Plant('Rose', 25, 30)
    plant.show()
    for day in range(1, 8):
        print(f'=== Day {day} ===')
        plant.grow()
        plant.age()
        plant.show()
    print(f'Grow this week: {plant.centimeters_growth}cm')


if __name__ == '__main__':
    main()
