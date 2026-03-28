from ex0.Card import CardRarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    fire_dragon = CreatureCard('Fire Dragon', 5, CardRarity.LEGENDARY, 7, 5)
    lightning_bolt = SpellCard('Lightning Bolt', 3, CardRarity.RARE, 'damage')
    mana_crystal = ArtifactCard(
        'Mana Crystal', 2, CardRarity.COMMON, 5, '+1 mana per turn'
    )

    deck = Deck()
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    for i in range(3):
        card = deck.draw_card()
        if card:
            type_name = card.__class__.__name__.replace('Card', '')
            print(f"Drew: {card.name} ({type_name})")
            print(f"Play result: {card.play({})}\n")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == '__main__':
    main()
