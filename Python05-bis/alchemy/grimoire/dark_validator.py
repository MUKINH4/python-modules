from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = {
        ingredient.lower() for ingredient in dark_spell_allowed_ingredients()
    }
    ingredients_list = [
        ingredient.strip(" ,").lower() for ingredient in ingredients.split()
    ]
    if any(ingredient in allowed_ingredients
           for ingredient in ingredients_list):
        result = f"{ingredients}- VALID"
    else:
        result = f"{ingredients}- INVALID"

    return result
