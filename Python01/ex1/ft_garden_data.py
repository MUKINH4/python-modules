class Plant:

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.plant_age} days old')


def main() -> None:
    print('=== Garden Plant Registry ===')
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == '__main__':
    main()
