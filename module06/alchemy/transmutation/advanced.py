def philosophers_stone() -> str:
    try:
        from .basic import lead_to_gold
        from ..potions import healing_potion
        return ("Philosopher's stone created using "
                f"{lead_to_gold()} and {healing_potion()}")
    except ImportError as e:
        return e


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
