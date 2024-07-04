from Fire import Fire

class Charizard(Fire):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power,defense_power):
        super().__init__(name, catch_rate, pokemon_type)
        if not isinstance(level, int):
            raise TypeError("level must be an integer")
        if not (32<=level<=50):
            raise ValueError("level must be between 32 and 50")
        if not isinstance(hit_points, int):
            raise TypeError("hit points must be an integer")
        if not (78<=hit_points<=99):
            raise ValueError("hit points must be between 78 and 99")
        if not isinstance(attack_power, int):
            raise TypeError("attack power must be an integer")
        if not (84<=attack_power<=99):
            raise ValueError("attack power must be between 84 and 99")
        if not isinstance(defense_power, int):
            raise TypeError("defense power must be an integer")
        if not (78<=defense_power<=99):
            raise ValueError("defense power must be between 78 and 99")
        self.__level= level
        self.__hit_points= hit_points
        self.__attack_power= attack_power
        self.__defense_power= defense_power
        self.__first_hit_points= hit_points


    def get_hit_points(self):
        return self.__hit_points

    def get_defense_power(self):
        return self.__defense_power

    def can_fight(self):
        if self.__hit_points >= (self.__first_hit_points) * 0.1:
            return True
        else:
            return False

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int((self.__first_hit_points) * 0.1)
            damage = self.get_damage(other)
            other.absorb(damage)

    def absorb(self, damage):
        self.__hit_points -= damage

    def __repr__(self):
        return f"The Charizard {self.get_name()} of level: {self.__level} with {self.__hit_points} HP"

    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            eff = 2
        else:
            eff = 0.5
        damage = int((((self.__level * 2) / 5) + 2) * ((self.__attack_power) / other.get_defense_power() * eff)+4)
        return damage

    def level_up(self, level_gain):
        if level_gain>=0:
            self.__level = +level_gain
            if self.__level > 50:
                self.__level=50