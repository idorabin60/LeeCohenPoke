from Pokemon import Pokemon
from abc import ABC, abstractmethod
import copy

class Electric(Pokemon, ABC):
    def __init__(self, name, catch_rate, pokemon_type):
        super().__init__(name, catch_rate)
        self.__effective_against_me= []
        self.__effective_against_others=["water"]
        if pokemon_type!= "electric":
            raise TypeError("for a Electric pokemon, type must be Electric")
        self.__pokemon_type= pokemon_type

    def get_pokemon_type(self):
        return copy.deepcopy(self.__pokemon_type)

    def get_effective_against_me(self):
        return copy.deepcopy(self.__effective_against_me)

    def get_effective_against_others(self):
        return copy.deepcopy(self.__effective_against_others)

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def absorb(self, damage):
        pass

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def can_fight(self):
        pass

    @abstractmethod
    def get_damage(self, other):
        pass

    @abstractmethod
    def get_defense_power(self):
        pass

    @abstractmethod
    def get_hit_points(self):
        pass

    @abstractmethod
    def level_up(self, level_gain):
        pass