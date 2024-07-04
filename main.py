# test_battle.py

from Pikachu import Pikachu
from Charmander import Charmander
from Charizard import Charizard
from Wartortle import Wartortle
from Trainer import Trainer
from Battle import Battle

# Create Pokémon instances
charzy = Charizard("charzy", 45, "fire", 37, 93, 93, 82)
pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)
warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)

# Create Trainer instances
ash = Trainer("ash", 18, 6.0, [charzy, pika])
misty = Trainer("misty", 18, 5.5, [warty, charmy])

# Print initial trainer information
print(ash)
print(misty)

# Create Battle instance

battle = Battle(ash, misty)
battle.total_battle()
result = Battle.total_battle(ash,misty)
print(result)

# Print trainer information after battle
print(misty)
print(ash)

# Create new instances for another battle scenario
ash = Trainer("ash", 18, 6.0, [pika, charzy])
misty = Trainer("misty", 18, 5.5, [charmy, warty])

# Print initial trainer information
print(misty)
print(ash)

# Create new Battle instance for the new scenario
battle = Battle(ash, misty)

# Simulate the battle
result = battle.total_battle()
print(result)

# Print trainer information after battle
print(misty)
print(ash)




