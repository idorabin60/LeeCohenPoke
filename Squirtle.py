from Water import Water
from Wartortle import Wartortle


class Squirtle(Water):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):
        super().__init__(name, catch_rate, pokemon_type)
        if not isinstance(level, int):
            raise TypeError("Level must be an integer")
        if not (1 <= level <= 15):
            raise ValueError("Level must be between 1 and 15")
        if not isinstance(hit_points, int):
            raise TypeError("Hit points must be an integer")
        if not (44 <= hit_points <= 58):
            raise ValueError("Hit points must be between 44 and 58")
        if not isinstance(attack_power, int):
            raise TypeError("Attack power must be an integer")
        if not (48 <= attack_power <= 62):
            raise ValueError("Attack power must be between 48 and 62")
        if not isinstance(defense_power, int):
            raise TypeError("Defense power must be an integer")
        if not (65 <= defense_power <= 79):
            raise ValueError("Defence power must be between 65 and 79")
        self.__level = level
        self.__hit_points = hit_points
        self.__attack_power = attack_power
        self.__defense_power = defense_power
        self.__first_hit_points = hit_points

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
        damage = int(((self.__level * 2) / 5) + 2) * ((self.__attack_power) / other.get_defense_power() * eff)
        return int(damage)

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int(self.__first_hit_points * 0.1)
            damage = self.get_damage(other)
            other.absorb(damage)

    def absorb(self, damage):
        self.__hit_points -= damage


    def __repr__(self):
        return f"The Squirtle {self.get_name()} of level: {self.__level} with {self.__hit_points} HP"

    def level_up(self, level_gain):
        if 1 <= level_gain <= 16:
            self.__level += level_gain
            if self.__level > 15:
                return self.evolve()
        return None

    def evolve(self):
        self.__hit_points += 15
        if self.__hit_points in range(59, 79):
            return Wartortle(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.__level,
                              self.__hit_points, self.__attack_power + 15, self.__defense_power + 15)
        else:
            return Wartortle(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.__level, 59,
                              self.__attack_power + 15, self.__defense_power + 15)
