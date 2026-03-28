from ex0.Card import CardRarity
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity=CardRarity.LEGENDARY,
        attack=7,
        health=5
    )

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    available_mana = 6
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
    playable = fire_dragon.is_playable(available_mana)
    print(f"Playable: {playable}")

    if playable:
        result = fire_dragon.play({"mana": available_mana})
        print(f"Play result: {result}")

    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target("Goblin Warrior")
    print(f"Attack result: {attack_result}")

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
