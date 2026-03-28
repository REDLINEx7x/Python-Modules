from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract interface for tournament ranking capabilities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return current rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update win count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """Return ranking information."""
        pass

