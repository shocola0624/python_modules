#!/usr/bin/env python3

import sys
import math


def to_tuple(arg: str) -> tuple:
    """Converts the string of coordinate to tuple.

    Note: This function can cause errors.
    """
    a = arg.split(",", 2)
    _ = a[2]
    x = [int(n) for n in a]
    c = tuple(x)
    return c


def coord(arg: str) -> tuple | None:
    """Returns a 3D coordinate."""
    try:
        c = to_tuple(arg)
        print(f"Position created: {c}")
        distance((0, 0, 0), c)
    except ValueError as e:
        print(f"Error creating coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\")")
        return None
    except IndexError as e:
        print(f"Error creating coordinates: {e}")
        print(f"Error details - Type: IndexError, Args: (\"{e}\")")
        return None
    return c


def distance(c1: tuple, c2: tuple) -> None:
    """Prints the distance between c1 and c2."""
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {c1} and {c2}: {d:.2f}")


def parse(pos: tuple, arg: str) -> tuple:
    """Parses coordinate string.

    Return:
        (tuple) Returns new position. If errors occur, it returns previous
        position.
    """
    try:
        c = to_tuple(arg)
        print(f"Parsing coordinates: \"{arg}\"")
        print(f"Parsed position: {c}")
        distance((0, 0, 0), c)
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{arg}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\")")
        return pos
    except IndexError as e:
        print(f"Parsing invalid coordinates: \"{arg}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: IndexError, Args: (\"{e}\")")
        return pos
    return c


def coordinate_system() -> None:
    """
    Usage:
        python3 ft_coordinate_system.py <coord1> <coord2> ...

    Example:
        python3 ft_coordinate_system.py "10,20,5" "3,4,0" "abc,def,ghi"
    """
    print("=== Game Coordinate Sysrtem ===\n")

    av = sys.argv
    coordinates = av[1:]
    pos = None

    if not coordinates:
        coordinates = ["10,20,5", "3,4,0", "abc,def,ghi"]

    for arg in coordinates:
        if not pos:
            pos = coord(arg)
        else:
            pos = parse(pos, arg)
        print()

    print("Unpacking demonstration:")
    if not pos:
        print("No position was created!")
    else:
        x, y, z = pos
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system()
