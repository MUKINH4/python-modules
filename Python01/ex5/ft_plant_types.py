class Plant:

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self._height = height
        self._plant_age = plant_age

    def set_height(self, height: float):
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {round(self.get_height(), 1)}cm")

    def set_age(self, _plant_age: int):
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
              f'{self.get_age()} days old')

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._plant_age += 1


class Flower(Plant):

    def __init__(self, name: str, height: float, plant_age: int,
                 color: str) -> None:
        super().__init__(name, height, plant_age)
        self._color = color
        self._bloomed = False
        print("\n=== Flower")

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        if not self._bloomed:
            self.show()
            print(f" {self.name} has not bloomed yet")
            print("[asking the rose to bloom]")
            self._bloomed = True
        self.show()
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")


class Tree(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 trunk_diameter: float):
        super().__init__(name, height, plant_age)
        self._trunk_diameter = trunk_diameter
        print("\n=== Tree")

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of",
              f"{self.get_height()}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, plant_age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        print("\n=== Vegetable")

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def set_height(self, height):
        self._height = height

    def grow(self, grow_days):
        for _ in range(grow_days):
            self.set_height(self.get_height() + 2.1)
        print(f"[make tomato grow and age for {grow_days} days")
        self.set_age(self.get_age() + grow_days)
        self._nutritional_value += grow_days


def main():
    print("=== Garden Plant Types ===")
    flower: Flower = Flower("Rose", 15.0, 30, "red")
    flower.bloom()

    tree: Tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()

    vegetable: Vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    vegetable.grow(20)
    vegetable.show()


if __name__ == "__main__":
    main()
