from typing import Dict, Any, Optional, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Game orchestrator that combines factories and strategies.

    This class demonstrates how Abstract Factory and Strategy
    patterns work together to create a flexible game system.
    """

    def __init__(self) -> None:
        """Initialize the game engine."""
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

        # Create a sample hand of cards
        if self.factory:
            self.hand = [
                self.factory.create_creature("Fire Dragon"),
                self.factory.create_creature("Goblin Warrior"),
                self.factory.create_spell("Lightning Bolt")
            ]
            self.cards_created = len(self.hand)

    def simulate_turn(self) -> Dict[str, Any]:

        if not self.strategy:
            return {
                "error": "No strategy configured",
                "success": False
            }

        # Execute the turn using the strategy
        turn_result = self.strategy.execute_turn(
            self.hand,
            self.battlefield
        )

        # Update engine state
        self.turns_simulated += 1

        # Extract damage from turn result if available
        if "damage_dealt" in turn_result:
            self.total_damage += turn_result["damage_dealt"]

        return turn_result

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (self.strategy.get_strategy_name()
                             if self.strategy else "None"),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
            "factory_type": (type(self.factory).__name__
                            if self.factory else "None"),
            "hand_size": len(self.hand),
            "battlefield_size": len(self.battlefield)
        }
