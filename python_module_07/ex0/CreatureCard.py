from ex0.Card import Card, CardRarity
from typing import Dict , Any


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: CardRarity, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("Attack must be positive")
        if health <= 0:
            raise ValueError("Health must be positive")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        #    "stats": {"attack": self.attack, "health": self.health}
        }

    def attack_target(self, target: Any) -> Dict[str, Any]:

        target_name = getattr(target, 'name', str(target))

        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info
