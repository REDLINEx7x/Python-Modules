from ex0.Card import CardRarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()

    # create two tournament cards with different base ratings
    dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity=CardRarity.LEGENDARY,
        attack_power=8,
        health=5,
        base_rating=1200
    )

    wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity=CardRarity.RARE,
        attack_power=6,
        health=7,
        base_rating=1150
    )

    # register cards and get their IDs
    platform = TournamentPlatform()
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    # print registration info for each card
    for card, card_id in [(dragon, dragon_id), (wizard, wizard_id)]:
        rank_info = card.get_rank_info()
        print(f"{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {rank_info['rating']}")
        print(f"- Record: {rank_info['record']}")
        print()

    # create a match
    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")
    print()

    # print leaderboard
    print("Tournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} "
            f"- Rating: {entry['rating']} "
            f"({entry['record']})"
        )
    print()

    # print platform report
    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()


### Verify the Rating Math
#```
#Fire Dragon:  base=1200, wins=1, losses=0
#→ 1200 + (1×16) - (0×16) = 1216 ✅

#Ice Wizard:   base=1150, wins=0, losses=1
#→ 1150 + (0×16) - (1×16) = 1134 ✅

#avg_rating = (1216 + 1134) // 2 = 2350 // 2 = 1175 ✅
#```

#---

### Verify the IDs
#```
#"Fire Dragon" → split()[-1] = "Dragon" → .lower() = "dragon"
#→ card_id = "dragon_001" ✅

#"Ice Wizard"  → split()[-1] = "Wizard" → .lower() = "wizard"
#→ card_id = "wizard_001" ✅
