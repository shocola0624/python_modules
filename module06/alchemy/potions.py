def healing_potion() -> str:
    try:
        from .elements import create_fire, create_water
        fire_result = create_fire()
        water_result = create_water()
        return f"Healing potion brewed with {fire_result} and {water_result}"
    except ImportError as e:
        return e


def strength_potion() -> str:
    try:
        from .elements import create_fire, create_earth
        fire_result = create_fire()
        earth_result = create_earth()
        return f"Strength potion brewed with {earth_result} and {fire_result}"
    except ImportError as e:
        return e


def invisiblity_potion() -> str:
    try:
        from .elements import create_air, create_water
        air_result = create_air()
        water_result = create_water()
        return (f"Invisibility potion brewed with "
                f"{air_result} and {water_result}")
    except ImportError as e:
        return e


def wisdom_potion() -> str:
    try:
        from .elements import (create_fire,     create_water,
                               create_earth,    create_air)
        return ("Wisdom potion brewed with all elements: "
                f"{create_fire()} {create_water()}"
                f"{create_earth()} {create_air()}")
    except ImportError as e:
        return e
