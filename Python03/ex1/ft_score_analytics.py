from sys import argv


def usage() -> None:
    print("No scores provided.",
          "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    return


def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def calculate_range(scores: list[int]) -> float:
    return max(scores) - min(scores)


def get_valid_arg(argv: str, argc: int) -> list[int]:
    new_list: list[int] = []
    i = 1
    while i < argc:
        try:
            new_list.append(int(argv[i]))
        except Exception:
            print(f"Invalid parameter: '{argv[i]}'")
        i += 1
    return new_list


def print_stats(scores: list[int]) -> None:
    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", calculate_average(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", calculate_range(scores))


def main():
    print("=== Player Score Analytics ===")
    argc = len(argv)
    new_list = get_valid_arg(argv, argc)
    if len(new_list) < 2:
        usage()
        return
    print_stats(new_list)


if __name__ == "__main__":
    main()
