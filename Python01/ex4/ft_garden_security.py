class Plant:

    def __init__(self, name: str, _height: float, _plant_age: int) -> None:
        self.name = name
        self._height = _height
        self._plant_age = _plant_age
        print("Plant created: ", end="")
        self.show()

    def set_height(self, _height: float) -> None:
        if (_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = _height
        print(f"Height updated: {self.get_height()}cm")

    def set_age(self, _plant_age: int) -> None:
        if (_plant_age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._plant_age = _plant_age
        print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def show(self) -> None:
        print(f'{self.name}: {round(self.get_height(), 1)}cm,',
              f'{self.get_age()} days old\n')

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._plant_age += 1


def main():
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-1)
    print("\nCurrent stats: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
