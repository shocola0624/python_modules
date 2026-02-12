def lead_to_gold() -> str:
    try:
        from alchemy.elements import create_fire
        return f"Lead transmuted to gold using {create_fire()}"
    except ImportError as e:
        return e


def stone_to_gem() -> str:
    try:
        from alchemy.elements import create_earth
        return f"Stone transmuted to gem using {create_earth()}"
    except ImportError as e:
        return e
