from Fire import Fire
from Charmeleon import Charmeleon


class Charmander(Fire):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):
        super().__init__(name, catch_rate, pokemon_type)
        if not isinstance(level, int):
            raise TypeError("Level must be an integer")
        if not (1 <= level <= 15):
            raise ValueError("Level must be between 1 and 15")
        if not isinstance(hit_points, int):
            raise TypeError("Hit points must be an integer")
        if not (39 <= hit_points <= 57):
            raise ValueError("Hit points must be between 39 and 57")
        if not isinstance(attack_power, int):
            raise TypeError("Attack power must be an integer")
        if not (52 <= attack_power <= 63):
            raise ValueError("Attack power must be between 52 and 63")
        if not isinstance(defense_power, int):
            raise TypeError("Defense power must be an integer")
        if not (43 <= defense_power <= 57):
            raise ValueError("Defence power must be between 43 and 57")
        self.__level = level
        self.__hit_points = hit_points
        self.__attack_power = attack_power
        self.__defense_power = defense_power
        self.__first_hit_points = hit_points

    def __repr__(self):
        return f"The Charmander {self.get_name()} of level: {self.__level} with {self.__hit_points} HP"

    def get_hit_points(self):
        return self.__hit_points

    def get_defense_power(self):
        return self.__defense_power

    def can_fight(self):
        return self.__hit_points >= self.__first_hit_points * 0.1

    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            eff = 2
        else:
            eff = 0.5
        damage = int(((self.__level * 2) / 5) + 2) * (((self.__attack_power) / other.get_defense_power()) * eff)
        return int(damage)

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int(self.__first_hit_points * 0.1)
            damage = self.get_damage(other)
            other.absorb(damage)

    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        if 1 <= level_gain <= 16:
            self.__level += level_gain
            if self.__level > 15:
                return self.evolve()
        return None

    def evolve(self):
        self.__hit_points += 19
        if self.__hit_points in range(58, 78):
            return Charmeleon(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.__level,
                              self.__hit_points, self.__attack_power + 12, self.__defense_power + 15)
        else:
            return Charmeleon(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.__level, 58,
                              self.__attack_power + 12, self.__defense_power + 15)

