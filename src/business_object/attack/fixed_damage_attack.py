from .abstract_attack import AbstractAttack
from business_object.statistic import Statistic
class FixedDamageAttack(AbstractAttack):
    def __init__(
        self, power=0, name=None, description=None):
        super().__init__(power= power, 
            self._name: str = name
            self._description: str = description
    def get_pokemon_attack_coef(self) -> float:
        return  1 + (self.attack_current + self.defense_current) / 200