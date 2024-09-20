from unittest import TestCase

from business_object.pokemon.defender import DefenderPokemon
from business_object.statistic import Statistic


class TestDefenderPokemon(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = DefenderPokemon(stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        self.assertEqual(multiplier, 2)