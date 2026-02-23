"""Garden security demo: SecurePlant with validated private fields."""


class SecurePlant:
    """Plant with private height/age and simple validation."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant (height/age start at 0)."""
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, current_height: int) -> None:
        """Set height if non-negative."""
        if current_height >= 0:
            self.__height = current_height
            print(f"Height updated: {current_height}cm [OK]")
        else:
            print(
                "Invalid operation attempted: height "
                f"{current_height}cm [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Get height (cm)."""
        return self.__height

    def set_age(self, current_age: int) -> None:
        """Set age if non-negative."""
        if current_age >= 0:
            self.__age = current_age
            print(f"Age updated: {current_age} days [OK]")
        else:
            print(
                "Invalid operation attempted: age "
                f"{current_age}days [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        """Get age (days)."""
        return self.__age


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 25, 30)
print("Plant created:", plant.name)

plant.set_height(25)
plant.set_age(30)

print()
plant.set_height(-3)

print()
print(
    f"Current plant: {plant.name} ({plant.get_height()}cm, "
    f"{plant.get_age()} days)"
)
