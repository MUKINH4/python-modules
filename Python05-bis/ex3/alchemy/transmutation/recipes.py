from alchemy import elements
from ..potions import strength_potion
import elements as root_elements


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew "
        f"'{elements.create_air()}' and '{strength_potion()}' mixed with "
        f"'{root_elements.create_fire()}'"
    )
