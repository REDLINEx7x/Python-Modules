from typing import Any, Dict, List, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator combining factory and strategy patterns."""

    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.hand: List[Any] = []
        self.battlefield: List[Any] = []
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        if self.factory:
            self.hand = [
                factory.create_creature("Fire Dragon"),
                factory.create_creature("Goblin Warrior"),
                factory.create_spell("Lightning Bolt")
            ]
            self.cards_created = len(self.hand)

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.strategy:
            return {"error": "No strategy configured", "success": False}
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)  # ← fixed
        return result

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (self.strategy.get_strategy_name()
                              if self.strategy else "None"),  # ← fixed
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
