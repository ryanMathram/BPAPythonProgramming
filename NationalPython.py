'''
00191602
'''

import random
import datetime

'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


Character save exists. Override (O), Make a new save (N), or Quit (Q)?
Invalid input. Please enter 'O', 'N', or 'Q'.
No save found. Make a new save (N) or Quit (Q)?
Invalid input. Please enter 'N' or 'Q'.
Save Successful!
Would you like to adventure again? (Y/N):
Invalid input. Please enter 'Y' or 'N'.
See you on the next adventure!
'''


def valueError(): pass


'''''''''''''''''''''''''''''
 Write your new function here
'''''''''''''''''''''''''''''

#SC3
def save_game(char):
    # Try to see if try catch needed
    #SC4/SC5
    char.timestamp = datetime.datetime.now()
    dict = load_characters("GameSaves.txt")
    found = False

    for i in range(len(dict)):
        #SC6
        if dict.get(i) == char:
            found = True
            try:
                val = input("Character save exists. Override (O), Make a new save (N), or Quit(Q)? ").lower()
                #SC7
                if val == "o":
                    dict[i] = char
                elif val == "n":
                    dict[len(dict) + 1] = char
                elif val == "q":
                    break
                else:
                    raise ValueError()
            except valueError():
                val = input("Invalid input. Please enter 'O', 'N', or 'Q': ")
                if val == "o":
                    dict[i] = char
                elif val == "n":
                    dict[len(dict) + 1] = char
                elif val == "q":
                    break

    if not found:
        try:
            save = input("No save found. Make a new save(N) or Quit(Q)? ").lower()
            if save == "n":
                dict[len(dict) + 1] = char
            elif save == "q":
                exit()
            else:
                raise ValueError
        except valueError:
            save = input("Invalid input. Please enter 'N' or 'Q'. ")
            if save == "n":
                dict[len(dict) + 1] = char
            elif save == "q":
                exit()

    file = open("GameSaves.txt", "w")
    keys = dict.keys()
    for i in keys:
        val = (dict[i]).name + "," + (dict[i]).weapon + "," + str((dict[i]).level) + "," + str((
            dict[i]).strength) + "," + str((dict[i]).health) + "," + str((dict[i]).gold) + "," + str((
                  dict[i]).timestamp) + ","
        #SC8
        file.write("val")
    print("Save Successful")


class Character:
    def __init__(self, name, weapon, level=1, strength=random.randint(12, 17), health=random.randint(7, 10) * 10,
                 gold=0, timestamp=''):
        self.name = name
        self.weapon = weapon
        self.level = level
        self.strength = strength
        self.health = health
        self.gold = gold
        self.timestamp = timestamp

#SC1
def load_characters(filename):
    characters = {}
    with open(filename, 'r') as file:
        #SC2
        count = 1
        for line in file:
            name, weapon, level, strength, health, gold, timestamp = line.strip().split(',')
            characters[count] = Character(name, weapon, int(level), int(strength), int(health), int(gold), timestamp)
            count += 1
    return characters


def start_menu():
    while True:
        print("BPA Dungeon Adventure")
        print("---------------------")
        print("(N) New Game\n(L) Load Game")
        choice = input(
            "Enter your choice (N/L): ").upper()  # Converts the input to uppercase to handle lowercase inputs
        print()
        if choice == 'L':
            characters = load_characters('GameSaves.txt')
            load_game(characters)
            break  # Break out of the loop if a valid option is chosen
        elif choice == 'N':
            start_new_game()
            break  # Break out of the loop if a valid option is chosen
        else:
            print("Invalid choice!\n")


def start_new_game():
    print("Welcome to the dungeon!\nTreasure awaits for those brave enough to venture inside...")
    name = input("Enter your character's name: ")
    weapon = input("Choose your weapon: ")
    character = Character(name, weapon)
    start_game(character)


def load_game(characters):
    header = "There are " + str(len(characters)) + " available saves:"
    print()
    print(header)
    print("-" * len(header))
    #SC8
    keys = characters.keys()
    for key in keys:
        line = f"{key:>5}. {characters[key].name}\t{'Level ' + str(characters[key].level):>5}\t{characters[key].timestamp:>20}"
        print(line)

    while True:  # Loop to allow re-selection if user declines
        try:
            key = int(input("\nChoose a save to load: "))
            if 0 <= key < len(characters):
                selected_char = Character(characters[key].name, characters[key].weapon, characters[key].level,
                                          characters[key].strength, characters[key].health, characters[key].gold,
                                          characters[key].timestamp)
                display_character(selected_char)  # Show chosen character details
                confirm = input("Load this character? (Y/N): ").upper()
                if confirm == 'Y':
                    # Move on with that character
                    start_game(selected_char)
                    break  # Exit loop if confirmed
                elif confirm == 'N':
                    continue  # Re-display list of saves for a new choice
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.\n")
            else:
                print("Invalid selection.\nPlease choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def display_character(char):
    print(f"\nName: {char.name}\t\tLevel: {char.level}")
    print(f"Gold: {char.gold:02d}\t\tWeapon: {char.weapon}")
    print(f"Health: {char.health}\t\tStrength: {char.strength}\n\n")


def found_loot(char):
    loot = random.choice('ggggggghhh')
    if loot == 'g':
        new_gold = random.randint(25, 150)
        char.gold += new_gold
        return f"{new_gold} gold"
    else:
        bonus = random.randint(1, 3) * 10
        char.health += bonus
        return f"a health potion. You restored {bonus} health"


def encounter(char):
    print("A monster is attacking you!")
    while True:
        try:
            attack = int(input(f"Enter:\t'1' to use your {char.weapon},\n\t'2' to run away\nChoice: "))
            if attack < 1 or attack > 2:
                print("Invalid choice!")
            else:
                break
        except ValueError:
            print("Invalid Choice!")
    if attack == 1:
        monster = random.randint(10, 20)
        result = char.strength - monster
        if result >= 0:
            reward = found_loot(char)
            input(f"\nYou defeated the monster and found {reward}!\nPress Enter to continue")
        else:
            char.health -= abs(result) * 10
            print(f"\nThat was rough! You lost {abs(result) * 10} health.")
            if char.health <= 0:
                char.health = 0
            else:
                input("Luckily you managed to get past the monster!\nPress Enter to continue")
    elif attack == 2:
        save_game(char)
    return attack


def game_over(char):
    if char.health > 0 and char.level == 4:
        treasure = random.randint(500, 5000)
        char.gold += treasure
        print(f"\nYou made it to the treasure! You found {treasure} gold!")
    elif char.health > 0 and char.level < 4:
        print("\nYou didn't find the treasure, but you survived to fight again another day...")
    else:
        print("\nYou fought as best you could, but didn't make it.\nThe treasure waits for the next adventurer...")
    display_character(char)

    play = input("Would you like to play again? (Y/N)? ").lower()
    print(play)
    if play != "y" or play != "n":
        play = input("Invalid input. Please enter 'Y' or 'N'. ")
    if play == "y":
        start_menu()
    elif play == "n":
        print("See you on the next adventure!")


def start_game(character):
    display_character(character)
    # rewrite the for loop to pick up where the character left off
    for i in range(character.level, 4):
        result = encounter(character)
        if character.health <= 0 or result == 2:
            break
        else:
            character.level += 1
        display_character(character)
    game_over(character)


# Main code
characters = load_characters("GameSaves.txt")
start_menu()