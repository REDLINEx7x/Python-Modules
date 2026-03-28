from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    # Create factory and strategy
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {type(strategy).__name__}")

    # Show supported types
    supported_types = factory.get_supported_types()
    print(f"Available types: {supported_types}")

    # Configure engine
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    # Print hand like subject format
    hand_descriptions = []
    for card in engine.hand:
        info = card.get_card_info()
        hand_descriptions.append(f"{info['name']} ({info['cost']})")

    print(f"Hand: [{', '.join(hand_descriptions)}]\n")

    print("Turn execution:")
    turn_result = engine.simulate_turn()

    print(f"Strategy: {turn_result.get('strategy', 'Unknown')}")

    # IMPORTANT: actions are inside "actions"
    actions = {
    "cards_played":     turn_result.get("cards_played", []),
    "mana_used":        turn_result.get("mana_used", 0),
    "targets_attacked": turn_result.get("targets_attacked", []),
    "damage_dealt":     turn_result.get("damage_dealt", 0)
}
    print(f"Actions: {actions}")

    print("\nGame Report:")
    status = engine.get_engine_status()

    report = {
        "turns_simulated": status.get("turns_simulated", 0),
        "strategy_used": status.get("strategy_used", "Unknown"),
        "total_damage": status.get("total_damage", 0),
        "cards_created": status.get("cards_created", 0)
    }

    print(report)

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
