import copy
class Trainer:
    def __init__(self, name, age, exp_modifier, pokemons_lst=None):
        if not isinstance(name, str):
            raise TypeError("the Trainer's name must be a string")
        if not isinstance(age, int):
            raise TypeError("the Trainer's age must be an integer")
        if not (16 <= age <= 120):
            raise ValueError("the Trainer's age must be between 16 and 120")
        if not isinstance(exp_modifier, float):
            raise TypeError("the Trainer's experience modifier must be a float")
        if not (1.5 <= exp_modifier <= 12.5):
            raise ValueError("the Trainer's experience modifier must be between 1.5 and 12.5")
        self.__name= name
        self.__age= age
        self.__exp_modifier= exp_modifier
        self.__pokemons_lst= []
        if pokemons_lst:
            for i in range(0,len(pokemons_lst)):
                self.__pokemons_lst.append(copy.copy(pokemons_lst[i]))

    def __len__(self):
        return len(self.__pokemons_lst)

    def __repr__(self):
        trainer_att= "The Trainer " + self.__name + " is " + str(self.__age) + " years old and has the following pokemons (" + str(len(self.__pokemons_lst)) + " in total):\n"
        for i in range(0, self.__len__()):
            trainer_att+= str(self.get_pokemon_lst()[i])
        return trainer_att


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_exp_modifier(self):
        return self.__exp_modifier

    def get_pokemon_lst(self):
        return copy.deepcopy(self.__pokemons_lst)

    def change_pokemon_lst(self, pokemon, pokemon_id):
        self.__pokemons_lst[pokemon_id]=(pokemon)

    def catch_pokemon(self, pokemon):
        capture_chances= ((pokemon.get_catch_rate()* self.__exp_modifier*(100-pokemon.get_hit_points())/100))
        if capture_chances>50:
            self.__pokemons_lst.append(copy.copy(pokemon))
            return self.__name+ " caught "+ pokemon.get_name()
        else:
            return self.__name + " couldn't catch " + pokemon.get_name()

    def __eq__(self, other):
        total_hit_points_self= 0
        total_hit_points_other= 0
        for i in range(0, self.__len__()):
            total_hit_points_self+= self.__pokemons_lst[i].get_hit_points()
        for i in range(0, other.__len__()):
            total_hit_points_other += other.__pokemons_lst[i].get_hit_points()
        return total_hit_points_self==total_hit_points_other

    def __gt__(self, other):
        total_hit_points_self = 0
        total_hit_points_other = 0
        for i in range(0, self.__len__()):
            total_hit_points_self += self.__pokemons_lst[i].get_hit_points()
        for i in range(0, other.__len__()):
            total_hit_points_other += other.__pokemons_lst[i].get_hit_points()
        return total_hit_points_self > total_hit_points_other


    def __ge__(self, other):
        total_hit_points_self = 0
        total_hit_points_other = 0
        for i in range(0, self.__len__()):
            total_hit_points_self += self.__pokemons_lst[i].get_hit_points()
        for i in range(0, other.__len__()):
            total_hit_points_other += other.__pokemons_lst[i].get_hit_points()
        return total_hit_points_self >= total_hit_points_other

    def __le__(self, other):
        total_hit_points_self = 0
        total_hit_points_other = 0
        for i in range(self.__len__()):
            total_hit_points_self += self.__pokemons_lst[i].get_hit_points()
        for i in range(other.__len__()):
            total_hit_points_other += other.__pokemons_lst[i].get_hit_points()
        return total_hit_points_self <= total_hit_points_other

    def __lt__(self, other):
        total_hit_points_self = 0
        total_hit_points_other = 0
        for i in range(self.__len__()):
            total_hit_points_self += self.__pokemons_lst[i].get_hit_points()
        for i in range(other.__len__()):
            total_hit_points_other += other.__pokemons_lst[i].get_hit_points()

        return total_hit_points_self < total_hit_points_other

    def __add__(self, other):
        if self> other:
            new_name= self.__name  +"-"+ other.__name
            new_pokemon_list = self.__pokemons_lst + other.__pokemons_lst
        else:
            new_name=  other.__name + "-" + self.__name
            new_pokemon_list = other.__pokemons_lst+ self.__pokemons_lst
        new_age= int((self.__age+ other.__age)/2)
        new_exp_modifier= ((self.__exp_modifier + other.__exp_modifier)/2)
        combined= Trainer(new_name, new_age, new_exp_modifier, new_pokemon_list)
        return combined


    def __str__(self): #to print the combined trainers
        result ="The Trainer "+ self.__name+ " is " + str(self.__age) + " years old " + "and has the following pokemons (" + str(len(self.__pokemons_lst)) + " in total):"
        for pokemon in self.__pokemons_lst:
            result += "\n" +str(pokemon)
        return result



