from alchemy.transmutation import recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print("Testing lead to gold:", recipes.lead_to_gold())


if __name__ == "__main__":
    main()
