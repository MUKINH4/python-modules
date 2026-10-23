import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "First Steps",
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder",
    ]
    number_of_achievements = random.randint(5, 9)
    return set(random.sample(achievements, number_of_achievements))


def main() -> None:
    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements = {
        name: gen_player_achievements() for name in player_names
    }

    print("=== Achievement Tracker System ===\n")
    for name, achievements in player_achievements.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set()
    for achievements in player_achievements.values():
        all_achievements = all_achievements.union(achievements)

    common_achievements = set.intersection(*player_achievements.values())
    print(f"\nAll distinct achievements: {all_achievements}")
    print(f"\nCommon achievements: {common_achievements}\n")

    for name, achievements in player_achievements.items():
        other_achievements: set[str] = set()
        for other_name, other_player_achievements in player_achievements.items():
            if other_name != name:
                other_achievements = other_achievements.union(
                    other_player_achievements
                )
        unique_achievements = achievements.difference(other_achievements)
        print(f"Only {name} has: {unique_achievements}")

    print()
    for name, achievements in player_achievements.items():
        missing_achievements = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing_achievements}")


if __name__ == "__main__":
    main()
