from ex0.Card import Card
from ex0.Card import CardRarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card with combat and tournament ranking capabilities."""

    def __init__(self, name: str, cost: int, rarity: CardRarity,
                 attack_power: int, health: int,
                 base_rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.wins = 0
        self.losses = 0
        self.base_rating = base_rating    # ← never changes
        self.rating = base_rating         # ← updates after each match

    # ━━━━━━━━━━━━━━━━━━━━━━━━
    # From Card
    # ━━━━━━━━━━━━━━━━━━━━━━━━
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters battlefield"
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Tournament"
        info["attack_power"] = self.attack_power
        info["health"] = self.health
        return info

    # ━━━━━━━━━━━━━━━━━━━━━━━━
    # From Combatable
    # ━━━━━━━━━━━━━━━━━━━━━━━━
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "tournament"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(2, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    # ━━━━━━━━━━━━━━━━━━━━━━━━
    # From Rankable
    # ━━━━━━━━━━━━━━━━━━━━━━━━
    def calculate_rating(self) -> int:
        """Elo-style rating based on base_rating."""
        self.rating = self.base_rating + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}"
        }

    # ━━━━━━━━━━━━━━━━━━━━━━━━
    # Own method
    # ━━━━━━━━━━━━━━━━━━━━━━━━
    def get_tournament_stats(self) -> dict:
        return {
            "card_info": self.get_card_info(),
            "combat_stats": self.get_combat_stats(),
            "rank_info": self.get_rank_info()
        }
