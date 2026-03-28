from ex0.Card import CardRarity
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """Concrete factory creating fantasy-themed cards."""

    CREATURES = {
        "dragon": ("Fire Dragon", 5, CardRarity.LEGENDARY, 8, 5),
        "goblin": ("Goblin Warrior", 2, CardRarity.COMMON, 2, 1),
    }
    SPELLS = {
        "fireball": ("Fireball", 4, CardRarity.RARE, "damage"),
        "lightning": ("Lightning Bolt", 3, CardRarity.COMMON, "damage"),
    }
    ARTIFACTS = {
        "mana_ring": ("Mana Ring", 2, CardRarity.UNCOMMON, 3, "mana boost"),
    }

    def create_creature(self, name_or_power=None) -> CreatureCard:
        name = name_or_power if isinstance(name_or_power, str) else "dragon"
        key_map = {
            "fire dragon": "dragon",
            "goblin warrior": "goblin"
        }
        key = key_map.get(name.lower(), "dragon")
        return CreatureCard(*self.CREATURES[key])

    def create_spell(self, name_or_power=None) -> SpellCard:
        name = name_or_power if isinstance(name_or_power, str) else "fireball"
        key_map = {
            "fireball": "fireball",
            "lightning bolt": "lightning"
        }
        key = key_map.get(name.lower(), "fireball")
        return SpellCard(*self.SPELLS[key])

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        return ArtifactCard(*self.ARTIFACTS["mana_ring"])

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature("fire dragon"))
            elif i % 3 == 1:
                deck.append(self.create_spell("fireball"))
            else:
                deck.append(self.create_artifact())
        return {
            "deck": deck,
            "size": len(deck),
            "theme": "fantasy"
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
