from .abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic
class AttackerPokemon(AbstractPokemon):
    def __init__(
        self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None):
        super().__init__(
            stat_max=stat_max,stat_current=stat_current, level=level, name=name,
            type_pk="Attacker")
    def get_pokemon_attack_coef(self) -> float:
        return  1 + (self.speed_current + self.attack_current) / 200
