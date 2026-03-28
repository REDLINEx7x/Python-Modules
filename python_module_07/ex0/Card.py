from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    """Enumeration of valid card rarities."""

    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

    def __str__(self) -> str:
        return self.value


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: CardRarity) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
