"""Garden security module with a SecurePlant class and demo usage."""


class SecurePlant:
    """Represent a plant with validated, private height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with a name and secure attributes.

        Args:
            name: Plant name.
            height: Initial height in centimeters (stored securely).
            age: Initial age in days (stored securely).
        """
        self.name = name
        self.__height = 0
        self.__age = 0

    #def get_info(self) -> str:
    #        return f"{self.name} ({self.__height}cm, {self.__age} days)"

    def set_height(self, current_height: int) -> None:
        """Set the plant height if non-negative.

        Args:
            current_height: New height in centimeters.
        """
        if current_height >= 0:
            self.__height = current_height
            print(f"Height updated: {current_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {current_height}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Return the current plant height in centimeters."""
        return self.__height

    def set_age(self, current_age: int) -> None:
        """Set the plant age if non-negative.

        Args:
            current_age: New age in days.
        """
        if current_age >= 0:
            self.__age = current_age
            print(f"Age updated: {current_age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {current_age}days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        """Return the current plant age in days."""
        return self.__age


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 0, 0)

#print(f"Current plant:{plant.get_info()}")
print("Plant created:", plant.name)

plant.set_height(25)
plant.set_age(30)

print()
plant.set_height(-3)

print()
print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")
