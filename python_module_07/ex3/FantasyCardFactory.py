from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Union


class FantasyCardFactory(CardFactory):
    """Factory producing fantasy-themed cards."""

    CREATURES = {
        'dragon': ('Fire Dragon', 5, 'Legendary', 7, 5),
        'goblin': ('Goblin Warrior', 2, 'Common', 3, 2),
        'elf': ('Forest Elf', 3, 'Uncommon', 3, 4),
        'wizard': ('Ice Wizard', 4, 'Rare', 4, 3),
    }

    SPELLS = {
        'fireball': ('Fireball', 4, 'Rare', 'damage'),
        'lightning': ('Lightning Bolt', 3, 'Rare', 'damage'),
        'heal': ('Holy Light', 2, 'Common', 'heal'),
        'buff': ('Power Surge', 3, 'Uncommon', 'buff'),
    }

    ARTIFACTS = {
        'mana_ring': ('Mana Ring', 2, 'Uncommon', 5, '+1 mana per turn'),
        'staff': ('Arcane Staff', 4, 'Rare', 3, '+2 spell damage'),
        'crystal': (
            'Power Crystal', 3, 'Common', 4, '+1 attack to all creatures'
        ),
    }

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Create a fantasy creature card."""
        key = str(name_or_power).lower() if name_or_power else 'dragon'
        data = self.CREATURES.get(key, self.CREATURES['dragon'])
        return CreatureCard(*data)

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Create a fantasy spell card."""
        key = str(name_or_power).lower() if name_or_power else 'fireball'
        data = self.SPELLS.get(key, self.SPELLS['fireball'])
        return SpellCard(*data)

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Create a fantasy artifact card."""
        key = str(name_or_power).lower() if name_or_power else 'mana_ring'
        data = self.ARTIFACTS.get(key, self.ARTIFACTS['mana_ring'])
        return ArtifactCard(*data)

    def create_themed_deck(self, size: int) -> dict:
        """Create a balanced fantasy deck."""
        deck = []
        keys_creature = list(self.CREATURES.keys())
        keys_spell = list(self.SPELLS.keys())
        keys_arti = list(self.ARTIFACTS.keys())

        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature(keys_creature[i % len(keys_creature)]))
            elif i % 3 == 1:
                deck.append(self.create_spell(keys_spell[i % len(keys_spell)]))
            else:
                deck.append(self.create_artifact(keys_arti[i % len(keys_arti)]))

        return {'theme': 'Fantasy', 'cards': deck, 'size': len(deck)}

    def get_supported_types(self) -> dict:
        """Return supported card types."""
        return {
            'creatures': list(self.CREATURES.keys()),
            'spells': list(self.SPELLS.keys()),
            'artifacts': list(self.ARTIFACTS.keys())
        }
