#00191602

import math
import random
name = ""
weapon = ""
choice = ""
level = 0
gold = 00
health = 0
strength = 0


#SC1 : prints all the attributes of the character
def display_character():
    global name
    global weapon
    global level
    global gold
    global strength
    global health
    global choice
    return (f"\nName: {name}\t Level: {level}\nGold: {gold}\t Weapon: {weapon}\n"
            f" Health: {health}\t Strength: {strength} \n\n")



def encounter():
    global choice
    global strength
    global weapon
    print("A monster is attacking you!")
    '''choice = input(f"Enter:\t'1' to use your {weapon},\n\t\t'2' to run away\nChoice: ")
    #SC8
    if choice != "1" or choice != "2":
        print("Invalid choice")
        choice = input(f"Enter:\t'1' to use your {weapon},\n\t\t'2' to run away")

    if choice == "1":
        #SC9
        mon_ste = random.randint(10,20)
        if(strength >= mon_ste):
            print(f"You defeated the monster and found {found_loot()}!")
            input("Press Enter when you are ready to begin... ")
        else:
            strength = (mon_ste - strength) * 10
            '''
    try:
        choice = input(f"Enter:\t'1' to use your {weapon},\n\t\t'2' to run away\nChoice: ")
        if(choice != "1" or choice != "2"):
            raise ValueError("Invalid choice")
    except ValueError as e:
        print(e)
        choice = input(f"Enter:\t'1' to use your {weapon},\n\t\t'2' to run away\nChoice: ")
    finally:
        if choice == "1":
            # SC9
            mon_ste = random.randint(10, 20)
            if (strength >= mon_ste):
                print(f"You defeated the monster and found {found_loot()}!")
                input("Press Enter when you are ready to begin... ")
            else:
                strength = (mon_ste - strength) * 10



#SC3: randomly chooses if the user gets gold(70) or health(30)
def found_loot():
    global health
    global gold
    ran = random.randint(100)
    #SC4: Adds random amount of gold or health
    if(ran <= 70):
        value = random.randint(25,150)
        gold += value
        return f"{value} gold!"
    else:
        value = random.randint(1,3) * 10
        health += value
        return f"a health potion. You restored {value} health"


def start_game():
    global name
    global weapon
    global level
    global gold
    global strength
    global health
    global choice

    name = input("What is your name, adventure? ")
    weapon = input("What is your weapon of choice? ")
    level = 1
    #SC2
    gold = 00
    health = random.randint(70,100)
    strength = random.randint(10,20)

    display_character()

    print(f"Hello, {name}!\nIn this dungeon, you will fight three "
          f"monsters. If you survive to the end, treasure awaits!\nYou have a trusty {weapon}, I see.\nGood You will need it.")
    input("Press Enter when you are ready to begin... ")
    #SC5
    for i in range(3):
        encounter()
        #SC6
        if health < 0 or choice == "2":
            break
        else:
            level += 1
    #SC7
    game_over()


def game_over():
    pass


print("Welcome to the dungeon!")

start_game()







