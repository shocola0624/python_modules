#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    try:
        print("alchemy.elements.create_fire():",
              alchemy.elements.create_fire())
        print("alchemy.elements.create_water():",
              alchemy.elements.create_water())
        print("alchemy.elements.create_earth():",
              alchemy.elements.create_earth())
        print("alchemy.elements.create_air():",
              alchemy.elements.create_air())
    except AttributeError:
        print("Failed direct module access test.")
    print()

    print("Testing package-level access (controlled by __init__.py):")

    try:
        print("alchemy.create_fire(): ", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_water(): ", end="")
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")
    print()

    print("Package metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
