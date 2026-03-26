from ex0.Card import Card
from typing import Dict, List


class SpellCard(Card):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.consumed = False

    def get_card_info(self) -> Dict:
        """Return spell card information."""
        info = super().get_card_info()
        info['type'] = 'Spell'
        info['effect_type'] = self.effect_type
        return info

    def play(self, game_state: dict) -> dict:
        self.consumed = True
        effect_map = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Restore {self.cost} health to target',
            'buff': f'Grant +{self.cost} power to target',
            'debuff': f'Reduce target power by {self.cost}'
        }
        effect = effect_map.get(
            self.effect_type, f'Apply {self.effect_type} effect'
        )
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect
        }

    def resolve_effect(self, targets: List) -> dict:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True
        }
