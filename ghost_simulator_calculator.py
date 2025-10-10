#List of bosses with set spawn orders
boss_list = ["dino king", "grim", "jolly roger", "anomaly", "anonymous", "lord of luck", "spade harbringer"]

#Used for for-loops
number = 0

#List of bosses spawn locations
dino_king_spawn_locations = ["junkyard", "desert", "beach"]
grim_spawn_locations = ["board shop", "above spawn", "soul converter"]
jolly_roger_locations = ["castle bridge", "pixie island bridge", "middle bridge"]
anomaly_spawn_locations = ["swamplands behind gab3", "farm", "spaceship at the highest point", "data stream next to key fragment", "winter tundra entrance to mushroom forest", "mushroom forest under green ring", "winter tundra on top of bridge", "winter tundra on top of cliff", "data stream next to rowan", "twisting river", "twisting river", "barn above juliana", "spaceship near gum machine", "spaceship near barn entrance", "bloxbyte hq to the right", "spaceship next to billy's fork", "spaceship next to billy's fork", "twisting river", "barn on the floor in a corner", "data stream next to rowan's flashdrive", "barn in fron of julianna", "barn next to rich-ard's tie", "twisting river", "reverse city central square", "reverse city 3rd floor", "reverse city bank entrance", "bloxbyte hq left room", "spaceship below billy's pitchfork", "swamplands next to red ring", "mushroom forest log at the start of obby"]
anonymous_spawn_locations = ["data stream", "winter tundra", "farm"]
lord_of_luck_spawn_locations = ["thexz's island", "covenk's island", "makkiemon's island", "goro7's island", "didi1147's island inside pyramid", "castle right side", "castle left side"]
spade_harbringer_spawn_locations = ["castle gardens", "crystal canyon", "enchanted jungle", "underwater ruins", "fantasy courtyard", "phantom castle", "scrap city", "blue forest", "floating bridge", "hidden caverns"]

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

#Main
What_to_calculate = input("What do you want to calculate?(boss, gems, luck) ")
if What_to_calculate.lower() == "boss":
    what_boss = input(f"What boss do you want to find?{boss_list} ")
    if what_boss.lower() == "dino king":
        boss_calculator(dino_king_spawn_locations, number)
    elif what_boss.lower() == "grim":
        boss_calculator(grim_spawn_locations, number)
    elif what_boss.lower() == "jolly roger":
        boss_calculator(jolly_roger_locations, number)
    elif what_boss.lower() == "anomaly":
        print("Note that the program will always say that the next spawn location is the same if its a duplicated spawn even if its the ladder of the two")
        boss_calculator(anomaly_spawn_locations, number)
    elif what_boss.lower() == "anonymous":
        boss_calculator(anonymous_spawn_locations, number)
    elif what_boss.lower() == "lord of luck":
        boss_calculator(lord_of_luck_spawn_locations, number)
    elif what_boss.lower() == "spade harbringer":
        boss_calculator(spade_harbringer_spawn_locations, number)