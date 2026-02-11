# BO & GC 3 team python game

kingdom = "The Silent Kingdom"
nothing = "Nothing in INV yet"
inventory = [nothing]
def controls(): 
    print("To open your inventory type: 'INV' to see the items you've obtained.")
    print('To use an item, type: item name.')
    print("Type back in INV to return.")
    print('To move around type: "Forwards, Backwards, Left, Right". ')
    print('If preseneted with a choice, type: "A" or "B".')
    print('If forgetful, type: "Help" to see the commands again.')

def question():
    answ = input("What do you do? ").lower().strip()
    return answ

def area1():
    print(f"You have made it to Silentville.")
    print(f"There are 3 buildings, a Shop to your left, a Dungeon behind you, and a Barbershop to your right.")
    choice = question()
    return choice

def area2():
    print("You're heading to the castle, you can turn back or go forwards")
    choice = question()

def shop():
    global inventory
    shop_inv = ["Sword"]
    s_value = 0
    buy_value = 0
    print(f"Welcome to Silentvilles' local shop")
    stuff = input("Are you looking to buy anything? ").strip().lower()
    if stuff == "yes":
        print("Ok, here is what we have to offer.")
        print(shop_inv)
        purchase = input("Do you buy it? ").strip().lower()
        if purchase == "yes":
            buy_value += 2
            inventory.append("Sword")
            print("Have a good day.")
            return buy_value
        elif purchase == "no":
            s_value +=1
            print("What are you doing here then?")
            return s_value
    elif stuff == "no":
        s_value += 1
        print("What are you doing here then?")
        return s_value
    else:
        s_value +=1
        print("What are you doing here then?")
        return s_value
    
def b_shop():
    b_value = 0
    print(f"Welcome to Silentvilles' Barbershop!")
    print("What are you looking for today?")
    cut = input("You tryna look fly? ").strip().lower()
    if cut == "yes":
        b_value += 1
        print("Here's your cut yo.")
        print("You leave the Barbershop.")
    elif cut == "no":
        b_value += 1
        print("Leave my shop, pooron.")
        print("You leave the Barbershop.")
    else:
        b_value += 1
        print("What you talking about yo?")
        print("You leave the Barbershop.")
    return b_value

def d_room1():
    print("You enter the dungeon.")
    print("The dungeon's ceiling and floor are both waterlogged.")
    choice = question()
    return choice

def d_room2():
    print("You travel deeper into the dungeon and find a large ogre standing in front of the door.")
    choice = question()
    return choice

def d_room_3a():
    winval = 0
    print("You walk into a bright room, with gold all around.")
    print("Your greed takes over")
    print("You've won the game")
    winval += 1
    return winval

def d_room_3b():
   winval = 0
   print("You see the queen alive and well")
   print("You grab the queen and return to the castle.")
   winval +=1
   return winval

def d_room_3c():
    loseval = 0
    print("You enter the room, it reeks of rot.")
    print("You see the queens dead body infront of you.")
    print("You have lost the game.")
    loseval +=1
    return loseval


def inv_check(thing):
    global inventory
    if nothing in inventory:
        inventory.pop(thing)


def game():
    name = input("What is your name? ").strip().title()
    print(f"Hello {name} welcome to {kingdom}.")
    controls()
    global inventory
    global nothing
    in_area1 = 1
    in_area2 = 0
    in_dungeon = 0
    in_castle = 0
    while in_area1 == 1:
        area1_answ = area1()
        if area1_answ == "backwards":
            d_answ = d_room1()
            if d_answ == "forwards":
                in_area1 -= 1
                break
            elif d_answ == "backwards":
                print("You left the dungeon.")
        elif area1_answ == "left":
            print("You go to the shop.")
            s_value = shop()
            if s_value == 1:
                print("You leave the shop.")
            elif s_value == 2:
                print("You leave the shop with your new sword.")
                inv_check(nothing)
        elif area1_answ == "right":
            print("You go to the Barbershop.")
            b_value = b_shop()
            if b_value == 1:
                print("You left the Barbershop.")
        elif area1_answ == "forwards":
            print("You go fowards.")
            in_area1 -= 1
            in_area2 += 1
            break
        elif area1_answ == "inv":
            print(inventory)
        elif area1_answ == "help":
            controls()
    if in_area1 != 1 and in_area2 != 1:
        in_dungeon +=1
    while in_dungeon == 1:
        d2_answ = d_room2()
    if in_area1 != 1 and in_dungeon != 1:
        while in_area2 == 1:
            area2_answ = area2()
            if area2_answ == "backwards":
                print ("You turn back")
                in_area2 -= 1
                in_area1 += 1
                break
            elif area2_answ == "forwards":
                print("You begin to walk to the castle")
            else:
                print("You can not do that here")
        
    

game()