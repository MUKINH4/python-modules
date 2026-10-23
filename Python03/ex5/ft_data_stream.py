import random
import typing


Event = tuple[str, str]


def gen_event() -> typing.Generator[Event, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "swim", "climb", "use", "release"]

    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(events: list[Event]) -> typing.Generator[Event, None, None]:
    while events:
        event_index = random.randrange(len(events))
        yield events.pop(event_index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()
    for event_index in range(1000):
        player, action = next(event_generator)
        print(f"Event {event_index}: Player {player} did action {action}")

    events = [next(event_generator) for _ in range(10)]
    print("Built list of 10 events:", events)

    for event in consume_event(events):
        print("Got event from list:", event)
        print("Remains in list:", events)


if __name__ == "__main__":
    main()
