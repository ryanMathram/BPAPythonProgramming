import random
import DungeonCrawler
#00191602
'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


Enter your choice (N/L):
Invalid choice!
Choose a save to load:
Load this character? (Y/N):
Invalid input. Please enter 'Y' or 'N'.
Invalid selection.\nPlease choose a number from the list.
Invalid input. Please enter a number.
'''


#SC1 the object Character is intialized
class Character:
    def __init__(self, name, weapon, level = 1, strength = random.randint(12,17),
                  health = random.randint(70,100).__round__(10),
                  gold = 0, time_s = ""):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.strength = strength
        self.health = health
        self.gold = gold
        self.time_s = time_s


def start_new_game():
    print("Welcome to the dungeon!\nTreasure awaits for those brave enough to venture inside...")
    name = input("Enter your character's name: ")
    weapon = input("Choose your weapon: ")
    #SC8 Creates a new character object and calls the start_game function from DungeonCrawler
    new_c = Character(name,weapon)
    DungeonCrawler.start_game(new_c)


def start_menu():
    print("BPA Dungeon Adventure\n---------------------\n(N) New Game\n(L) Load Game")
    choice = input("Enter your choice (N/L): ")

    #SC5 utilizes a while loop in order to catch the right values
    while True:
        if choice.lower() == "n":
            #SC7 calls the state_new_game() function when the user inputs "N"
            start_new_game()
            break
        elif choice.lower() == "l":
            #SC6 when the user wants to load a choice with "L", this calls the load_characters and load_game function
            list_char = load_characters("GameSaves.txt")
            load_game(list_char)
            break
        else:
            print("Invalid Choice!")
            choice = input("Enter your choice (N/L): ")


def load_game(lis_c):
    print(f"There are {len(lis_c)} available saves:")
    print("----------------------------")
    for n in range(len(lis_c)):
        print(f"\n{n+1} {lis_c[n].name}\tLevel {lis_c[n].level}\t{lis_c[n].time_s}")

    choice = int(input("Choose a save to load: "))


    #SC10 clls the display_chcaracters function from the DungeonCrawler python file and ensures the correct statement with the if statements
    DungeonCrawler.display_character(lis_c[choice-1])
    choice_two = input("Load this character(Y/N): ").lower()
    #SC9 Uses a while loop/trycatch in order to use the correct levels
    while True:
        if choice_two == "n":
            load_game(lis_c)
            break
        elif choice_two == "y":
            #SC10 calls start_game function from DungeonCrawler
            DungeonCrawler.start_game(lis_c[choice-1])
            break
        else:
            print("Invalid Choice!")
            choice_two = input("Load this character(Y/N): ").lower()

    pass

#SC2 the parameter takes the file name
def load_characters(file):

    lis = []
    #SC3 Readds each line of the file and creates a character object
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            list_chars = line.split(",")
            c = Character(list_chars[0],list_chars[1],int(list_chars[2]),int(list_chars[3]),
                          int(list_chars[4]),int(list_chars[5]),list_chars[6])
            #SC4 Adds the character object to the list and then returns the list after the loop
            lis.append(c)
    return lis

# main code
start_menu()