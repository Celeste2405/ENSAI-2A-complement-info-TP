from unittest import TestCase

from business_object.pokemon.all_rounder import AllRounderPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        drago = AllRounderPokemon(stat_current=Statistic(sp_atk=100, sp_def=100))

        # WHEN
        multiplier = drago.get_pokemon_attack_coef()

        # THEN
        self.assertEqual(multiplier, 2)