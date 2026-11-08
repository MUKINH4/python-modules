def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    return f"Testing record light spell: Spell recorded: {spell_name} " \
           f"({validation})"
