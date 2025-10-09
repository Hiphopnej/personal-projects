#List of bosses with set spawn orders
boss_list = ["dino king", "grim", "jolly roger", "anomaly", "anonymous", "lord of luck", "spade harbringer", "lord of luck", "remnant dino king", "remnant jolly roger", "remnant anonymous"]

#Used for for loops
number = 0

#List of bosses spawn locations
dino_king_spawn_locations = ["scrapyard", "desert", "beach"]

#functions
def boss_calculator(spawn_locations, number):
    last_spawn = input(f"What was the latest spawn location?{spawn_locations} ")
    for spawn in spawn_locations:
        if last_spawn == spawn:
            if spawn == spawn_locations[-1]:
                print(f"The next spawn location is {spawn_locations[0]}")
            else:
                print(f"The next spawn location is {spawn_locations[number + 1]}")
        number += 1

What_to_calculate = input("What do you want to calculate?(boss, gems, luck) ")
if What_to_calculate.lower() == "boss":
    what_boss = input(f"What boss do you want to find?{boss_list} ")
    if what_boss.lower() == "dino king":
        boss_calculator(dino_king_spawn_locations, number)