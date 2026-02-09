# BO & GC 3 team python game

"""kingdom = "The Silent Kingdom"
name = input("What is thy name: ").strip().title()
inventory = []

def game():
    print(f"You made it to {kingdom}, y")

def tutorial():
    print(f"Hello {name}. Welcome to {kingdom}.")
    print("This is the tutorial, you will learn what to do and how to do it.")
    print("If you are met with a choice the answers will be next to the question.") 
    print("EX: You are met with a fork in the road: A. left B. right.")
    print("If you obtain an ITEM you can see it when you type INV.")
    print("To use an item type the item's name for your coice.")
    print("You are now prepared to go on your adventure")
    game()

def start():
    answ = input("Do you wish to play? ").strip().lower()
    if answ == "yes":
        print("Good. enjoy your adventure.")
        tutorial()
    elif answ == "no":
        print("Goodbye!")
    else:
        print("That's not what I asked for.")

def question(question, answ1, answ2):
    input(f"{question}. A:{answ1} B:{answ2}")

start()"""


# GC
"""print(f"Hello {name}")
print(f"My name is Jona, welcome to {kingdom}, where would you like to go")
choice  = input(f"You can go to the princess tower or king tower, what do you choose {name} (King or princess) ").strip().capitalize()
if choice == "King":
    print("You go to the king tower.")
elif choice == "Princess":
    print("You go to the princess tower.")
homeless = input("You see a ugly stupid homeless man, do you A: Give him money or B: Ignore him ").strip().capitalize()
if homeless == "A":
    print("The homeless man tells people about your kindness, you obtain one kindness token ")
elif homeless == "B":
    print("You gain one hate token.")
print(f"You arrive at the {choice} tower.")"""

kingdom = "The Silent Kingdom"
def controls(): 
    print("To open your inventory type 'INV' to see the items you've obtained.")
    print("Type back in INV to return.")
    print('To move around type "Forwards, Backwards, Left, Right". ')
    print('To use an item, type the items name.')
    print('If preseneted with a choice, type, "A" or "B".')
    print('If forgetful, type "Help" to see the commands again.')

def question():
    answ = input("What do you do? ").lower().strip()
    return answ

def area1():
    print(f"You have made it to Silentville.")
    print(f"There are 3 buildings, a Shop, a Dungeon, and a Barbershop.")

def game():
    name = input("What is your name? ")
    print(f"Hello {name} welcome to {kingdom}.")
    controls()
    location = area1()
    area1_answ = question()
    if area1_answ == "backwards":
        print("You can't do that.")
    elif area1_answ

game()