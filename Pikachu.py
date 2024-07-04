from Electric import Electric

class Pikachu(Electric):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power,friendship):
        super().__init__(name, catch_rate, pokemon_type)
        if not isinstance(level, int):
            raise TypeError("level must be an interger")
        if not (1 <= level <= 32):
            raise ValueError("level must be between 1 and 32")
        if not isinstance(hit_points, int):
            raise TypeError("hit points must be an integer")
        if not (35 <= hit_points <= 99):
            raise ValueError("hit points must be between 35 and 99")
        if not isinstance(attack_power, int):
            raise TypeError("attack power must be an integer")
        if not (55 <= attack_power <= 99):
            raise ValueError("attack power must be between 55 and 99")
        if not isinstance(defense_power, int):
            raise TypeError("defense power must be an integer")
        if not (40 <= defense_power <= 99):
            raise ValueError("defense power must be between 40 and 99")
        if not isinstance(friendship, int):
            raise TypeError("friendship must be an integer")
        if not (1 <= friendship <= 5):
            raise ValueError("friendship must be between 1 and 5")
        self.__level = level
        self.__hit_points = hit_points
        self.__attack_power = attack_power
        self.__defense_power = defense_power
        self.__first_hit_points = hit_points
        self.__friendship= friendship

    def get_hit_points(self):
        return self.__hit_points

    def get_defense_power(self):
        return self.__defense_power

    def can_fight(self):
        return self.__hit_points >= int(self.__first_hit_points * 0.1)

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= int(self.__first_hit_points * 0.1)
            damage = self.get_damage(other)
            other.absorb(damage)

    def absorb(self, damage):
        self.__hit_points -= damage

    def __repr__(self):
        return f"The Pikachu {self.get_name()} of level: {self.__level} with {self.__hit_points} HP"

    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            eff = 2
        else:
            eff = 0.5
        damage = (int((((self.__level * 2) / 5) + 2) * ((self.__attack_power) / other.get_defense_power() * eff)) +self.__friendship)
        return damage

    def level_up(self, level_gain):
        if level_gain >= 0:
            self.__level += level_gain
            if self.__level > 50:
                self.__level =50