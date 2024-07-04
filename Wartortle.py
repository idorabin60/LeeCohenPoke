from Water import Water
from Blastoise import Blastoise

class Wartortle(Water):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):
        super().__init__(name, catch_rate, pokemon_type)
        if not isinstance(level, int):
            raise TypeError("Level must be an integer")
        if not (16 <= level <= 31):
            raise ValueError("Level must be between 16 and 31")
        if not isinstance(hit_points, int):
            raise TypeError("Hit points must be an integer")
        if not (59 <= hit_points <= 78):
            raise ValueError("Hit points must be between 59 and 78")
        if not isinstance(attack_power, int):
            raise TypeError("Attack power must be an integer")
        if not (63 <= attack_power <= 82):
            raise ValueError("Attack power must be between 63 and 82")
        if not isinstance(defense_power, int):
            raise TypeError("Defense power must be an integer")
        if not (80<= defense_power <= 99):
            raise ValueError("Defence power must be between 80 and 99")
        self.__level = level
        self.__hit_points = hit_points
        self.__attack_power = attack_power
        self.__defense_power = defense_power
        self.__first_hit_points = hit_points

    def __repr__(self):
        return f"The Wartortle {self.get_name()} of level: {self.__level} with {self.__hit_points} HP"

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
        damage = int((((self.__level * 2) / 5) + 2) * ((self.__attack_power) / other.get_defense_power() * eff)-1)
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
            if self.__level > 31:
                return self.evolve()
        return None

    def evolve(self):
        self.__hit_points += 20
        if self.__hit_points in range(80, 99):
            return Blastoise(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.__level,
                              self.__hit_points, self.__attack_power + 20, self.__defense_power + 20)
        else:
            return Blastoise(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.__level, 80,
                              self.__attack_power + 20, self.__defense_power + 20)