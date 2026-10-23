import random


def main() -> None:
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    capitalized_players = [player.capitalize() for player in players]
    originally_capitalized = [
        player for player in players if player[0].isupper()
    ]
    score_dict = {
        player: random.randint(0, 1000) for player in capitalized_players
    }
    average_score = sum(score_dict.values()) / len(score_dict)
    high_scores = {
        player: score
        for player, score in score_dict.items()
        if score > average_score
    }

    print("=== Game Data Alchemist ===\n")
    print("Initial list of players:", players)
    print("New list with all names capitalized:", capitalized_players)
    print("New list of capitalized names only:", originally_capitalized)
    print("\nScore dict:", score_dict)
    print(f"Score average is {round(average_score, 2)}")
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
