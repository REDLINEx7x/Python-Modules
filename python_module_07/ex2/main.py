from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    arcane_warrior = EliteCard(
        name='Arcane Warrior',
        cost=6,
        rarity='Legendary',
        attack_power=5,
        defense_power=3,
        mana_pool=4
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior.play({})

    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("Magic phase:")
    print(
        f"Spell cast: "
        f"{arcane_warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == '__main__':
    main()
