import random, os

filename_legend = "./src/legend.txt"

base_map = "./src/map"
filename_maps = { 
                "w": os.path.join(base_map, "world_edge.txt"),
                "k": os.path.join(base_map, "world_edge.txt"),
                "o": os.path.join(base_map, "world_edge.txt"),
                "s": os.path.join(base_map, "world_edge.txt"),
                }

def select_map(str):
    with open(filename_maps[str], "r", encoding="utf-8") as f:
        lis = f.read().splitlines()
    return lis

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lis = f.read().splitlines()
    return lis

def choice_one(lis:list):
    return random.choice(lis)

def main():
    
    map_key = input("select maps [w, k, o, s] : ")
    map_data = select_map(map_key)
    print("Map : ", choice_one(map_data))
    
    fly_man = random.randint(0, 10000) % 3 
    for i in range(3):
        if fly_man == i:
            print("Number:", i, " > ", choice_one(load_data(filename_legend)), " FLYMAN")
        else:
            print("Number:", i, " > ", choice_one(load_data(filename_legend)))
main()