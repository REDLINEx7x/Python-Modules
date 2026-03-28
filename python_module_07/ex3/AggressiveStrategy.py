from typing import List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Aggressive strategy: attack hard and fast."""

    def get_strategy_name(self) -> str:
        """Return strategy name."""
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize enemy player first, then creatures."""
        enemies = [t for t in available_targets if 'Enemy' in str(t)]
        others = [t for t in available_targets if 'Enemy' not in str(t)]
        return enemies + others

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute aggressive turn: play cheap cards, deal damage."""
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        mana_budget = 5
        mana_used = 0
        cards_played = []

        for card in sorted_hand:
            if mana_used + card.cost <= mana_budget:
                cards_played.append(card.name)
                mana_used += card.cost

        targets = self.prioritize_targets(['Enemy Player', 'Enemy Creature'])
        damage_dealt = mana_used + 3
        return {
            'strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets[:1],
            'damage_dealt': damage_dealt
        }
