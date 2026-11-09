from ex3.creatures import Creature, TransformCapability
from ex3.factories import TransformCreatureFactory


def demonstrate(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    print("base:")
    demonstrate(factory.create_base())
    print("evolved:")
    demonstrate(factory.create_evolved())