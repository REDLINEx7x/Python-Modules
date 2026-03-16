import alchemy.elements

from alchemy.elements import create_water
from alchemy.elements import create_fire, create_earth
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion


def main() -> None:

    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(alchemy.elements.create_fire())

    print("\nMethod 2 - Specific import:")
    print(create_water())

    print("\nMethod 3 - Aliased import:")
    print(heal())

    print("\nMethod 4 - Multiple imports:")
    print(create_earth())
    print(create_fire())
    print(strength_potion())

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
