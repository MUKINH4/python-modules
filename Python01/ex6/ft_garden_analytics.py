class Plant:

    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_count(self, func_name: str):
            if func_name == 'grow':
                self._grow_count += 1
            elif func_name == 'age':
                self._age_count += 1
            elif func_name == 'show':
                self._show_count += 1
            else:
                return

        def show_stats(self) -> None:
            print(f"{self._grow_count} grow, {self._age_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self._height = height
        self._plant_age = plant_age
        self.stats = self.Stats()

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
        self.stats.increment_count('show')

    def grow(self) -> None:
        self._height += 0.8
        self.stats.increment_count('grow')

    def age(self) -> None:
        self._plant_age += 1
        self.stats.increment_count('age')

    @staticmethod
    def more_than_year(days: int):
        print(f"Is {days} more than a year? -> {days > 365}")

    @classmethod
    def create_anonymous_plant(cls):
        return cls("Unknown plant", 0.0, 0)

class Flower(Plant):

    def __init__(self, name: str, height: float, plant_age: int,
                 color: str) -> None:
        super().__init__(name, height, plant_age)
        self._color = color
        self._bloomed = False
        print("\n=== Flower")

    def get_color(self) -> str:
        return self._color

    def grow(self):
        print(f"[asking the {self.name.lower()} to grow and bloom]")
        self.set_height(self.get_height + 8)
        self.bloom()

    def bloom(self) -> None:
        if not self._bloomed:
            self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        if not self._bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, plant_age: int, trunk_diameter: float):
        super().__init__(name, height, plant_age)
        self._trunk_diameter = trunk_diameter
        print("\n=== Tree")

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.get_height()}cm long and {self._trunk_diameter}cm wide.")

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


class Seed(Flower):

    def __init__(self, name: str, height: float, plant_age: str, color: str, seeds: int = 0):
        super().__init__(name, height, plant_age, color)
        self._seeds = seeds


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.more_than_year(30)
    Plant.more_than_year(400)

    flower: Flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    flower.stats.show_stats()

    anonymous = Plant.create_anonymous_plant()
    anonymous.show()


if __name__ == "__main__":
    main()

