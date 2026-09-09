def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_format = f"{seed_type.capitalize()} seeds:"
    if unit == "packets":
        print(f"{seed_type_format} {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type_format} {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type_format} covers {quantity} square meters")
    else:
        print("Unknown unit type")
