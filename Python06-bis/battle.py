from ex3.factories import CreatureFactory, FlameFactory
from ex3.factories import TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    first = first_factory.create_base()
    second = second_factory.create_base()
    print(first.describe())
    print("vs.")
    print(second.describe())
    print("fight!")
    print(first.attack())
    print(second.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(FlameFactory())
    print()
    print("Testing factory")
    test_factory(TransformCreatureFactory())
    print()
    print("Testing battle")
    battle(FlameFactory(), TransformCreatureFactory())