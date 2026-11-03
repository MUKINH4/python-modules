from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing healing_potion:", potions.healing_potion())
    print("Testing strength_potion:", potions.strength_potion())


if __name__ == "__main__":
    main()
