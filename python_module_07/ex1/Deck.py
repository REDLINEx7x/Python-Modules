import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, List, Optional


class Deck:

    def __init__(self) -> None:
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._cards:
            if card.name == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        if not self._cards:
            return None
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self._cards)
        creatures = sum(1 for card in self._cards if isinstance(card, CreatureCard))
        spells = sum(1 for card in self._cards if isinstance(card, SpellCard))
        artifacts = sum(1 for card in self._cards if isinstance(card, ArtifactCard))
        avg_cost = (
            round(sum(card.cost for card in self._cards) / total, 1)
            if total > 0 else 0.0
        )
        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
