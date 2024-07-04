from Trainer import Trainer
from Pokemon import Pokemon


class Battle:
    def __init__(self, trainer1, trainer2):
        self.__trainer1= trainer1
        self.__trainer2= trainer2


    def dual_battle(self, trainer1_pokemon_id, trainer2_pokemon_id):
        winner= 0
        print("debug that shit")
        print()
        pokemon1 = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id]
        pokemon2 = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id]
        rounds= 0
        while pokemon1.can_fight() and pokemon2.can_fight():
            rounds+=1
            pokemon1.attack(pokemon2)
            if pokemon2.can_fight():
               pokemon2.attack(pokemon1)
        if not pokemon1.can_fight() and pokemon2.can_fight():
            return rounds, 2
        elif pokemon1.can_fight() and not pokemon2.can_fight():
            return rounds, 1
        else:
            return rounds, 0

    def check_if_pokemon_can_fight(self,trainer):
        for pokemon in trainer.get_pokemon_lst():
            if pokemon.can_fight():
                return True
        return False


    def get_first_pokemon_that_can_fight(self,trainer):
        for pokemon in trainer.get_pokemon_lst():
            if pokemon.can_fight():
                return pokemon
        return None


    def get_the_index_of_the_pokemon(self,pokemon,trainer):
        for i in range(0,len(trainer.get_pokemon_lst())):
            if trainer.get_pokemon_lst()[i] == pokemon:
                return i

    @staticmethod
    def get_the_pokemon_that_can_deal_the_most_damage(self,target_pokemon,trainer):
        max_dmage = 0
        strongest_poke = None
        for attacking_pokemon in trainer.get_pokemon_lst():
            if attacking_pokemon.can_fight():
                if attacking_pokemon.get_damage(target_pokemon) > max_dmage:
                    max_dmage  = attacking_pokemon.get_damage(target_pokemon)
                    strongest_poke = attacking_pokemon
        return  strongest_poke

    def total_battle(self):
        rounds = 0
        while self.check_if_pokemon_can_fight(self.__trainer1) or self.check_if_pokemon_can_fight(self.__trainer2):
            rounds += 1
            pokemon1 = self.get_first_pokemon_that_can_fight(self.__trainer1)
            pokemon2 = self.get_first_pokemon_that_can_fight(self.__trainer2)


            if pokemon1 is None:
                if pokemon2 is None:
                    return "The battle ended in a draw"
                else:
                    return f'Trainer {self.__trainer2.get_name()} won the battle in {rounds} rounds'
            elif pokemon2 is None:
                return f'Trainer {self.__trainer1.get_name()} won the battle in {rounds} rounds'

            pokemon2 = self.get_the_pokemon_that_can_deal_the_most_damage(self,pokemon1, self.__trainer2)

            pokemon1_index = self.get_the_index_of_the_pokemon(pokemon1, self.__trainer1)
            pokemon2_index = self.get_the_index_of_the_pokemon(pokemon2, self.__trainer2)


            dual_result = self.dual_battle(pokemon1_index, pokemon2_index)

            if dual_result == 1:
                pokemon2 = self.get_the_pokemon_that_can_deal_the_most_damage(pokemon1, self.__trainer2)
            elif dual_result == 2:
                pokemon1 = self.get_the_pokemon_that_can_deal_the_most_damage(pokemon2, self.__trainer1)
            else:
                pokemon1 = self.get_first_pokemon_that_can_fight(self.__trainer1)
                pokemon2 = self.get_the_pokemon_that_can_deal_the_most_damage(pokemon1, self.__trainer2)

        return "The battle ended with a draw"
