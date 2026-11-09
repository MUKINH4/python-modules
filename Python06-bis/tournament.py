from ex3.factories import CreatureFactory, FlameFactory
from ex3.factories import TransformCreatureFactory
from ex4.strategies import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for index, (first_factory, first_strategy) in enumerate(opponents):
        for second_factory, second_strategy in opponents[index + 1:]:
            first = first_factory.create_base()
            second = second_factory.create_base()
            print()
            print("* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")
            try:
                print(first_strategy.act(first))
                print(second_strategy.act(second))
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
    print()
    print("Tournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
    ])