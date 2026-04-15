from typing import Callable
from collections.abc import Callable

def spell(target: str, power: int) -> str:
    ...

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable
    def combination(target: str, power: int):
        return tuple(return (spell1(target, power), spell2(target, power)))
    return combination

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable
def conditional_caster(condition: Callable, spell: Callable) -> Callable
def spell_sequence(spells: list[Callable]) -> Callable
