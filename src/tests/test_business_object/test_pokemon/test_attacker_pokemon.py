from unittest import TestCase

from business_object.pokemon.attacker import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        pika = AttackerPokemon(stat_current=Statistic(attack=100, speed=100))

        # WHEN
        multiplier = pika.get_pokemon_attack_coef()

        # THEN
        self.assertEqual(multiplier, 2)