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
    answ = question()
    return answ

def area2():
    print("You're heading to the castle, you can turn back or go forwards")
    choice = question()
    if choice == "backwards":
       print ("You turn back")
    elif choice == "forwards":
       print("You begin to face the castle")
    elif choice == "left" or choice == "right":
        print("You can't do that here, try forwards or backwards.")
    else:
        print("You can't do that here")

def shop():
    s_value = 0
    print(f"Welcome to Silentvilles' local shop")
    stuff = input("Are you looking to buy anything?").strip().lower()
    if stuff == "yes":
        s_value += 1
        print("We've got a lot, but based on your apperance here pal, you're not buying anything at this establishment.")
    elif stuff == "no":
        s_value += 1
        print("No, brokie")
    else:
        s_value +=1
        print("What are you doing here then?")
        return s_value
    
def b_shop():
    b_value = 0
    print(f"Welcome to Silentvilles' Barbershop!")
    print("What are you looking for today?")
    cut = input("You tryna look fly?").strip().lower()
    if cut == "yes":
        b_value += 1
        print("Heres your cut yo")
    elif cut == "no":
        b_value += 1
        print("Leave my shop, pooron")
    else:
        b_value += 1
        print("What you talking about yo")
    return b_value

def game():
    name = input("What is your name? ")
    print(f"Hello {name} welcome to {kingdom}.")
    controls()
    in_area1 = 1
    in_area2 = 0
    while in_area1 == 1:
        area1_answ = area1()
        if area1_answ == "backwards":
            print("You can't do that here.")
        elif area1_answ == "left":
            print("You go to the shop.")
            s_value = shop()
            if s_value > 0:
                area1()
        elif area1_answ == "right":
            print("You go to the Barbershop.")
            b_value = b_shop()
            if b_value > 0:
                area1
        elif area1_answ == "forwards":
            print("You go fowards.")
        else:
            print("placement")
            break
    in_area1 -= 1
    if in_area1 != 1:
        in_area2 += 1
    if in_area2 == 1:
        area2()
    

game()