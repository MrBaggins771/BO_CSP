# BO & GC 3 team python game

kingdom = "The Silent Kingdom"
nothing = "Nothing in INV yet"
inventory = [nothing]
playing_value = 0
playing = input("Do you wish to play? ").strip().lower()
if playing == "yes":
    playing_value += 1

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
    return choice

def castle():
    print("You have made it to the castle")
    print("To your left is the king's tower, to your right is the princess' tower, and behind you is the exit")
    castle_answ = question()
    return castle_answ

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
            s_value += 2
            inventory.append("Sword")
            print("Have a good day.")
            return s_value
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
    global inventory
    b_value = 0
    print(f"Welcome to Silentvilles' Barbershop!")
    print("What are you looking for today?")
    cut = input("You tryna look fly? ").strip().lower()
    if cut == "yes":
        b_value += 2
        print("Here's your cut yo.")
        inventory.append("A fresh cut")
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
    print("You can go deeper into the dungeon or leave.")
    choice = question()
    return choice

def d_room2():
    print("You travel deeper into the dungeon and find a large ogre standing in front of a door.")
    choice = question()
    return choice

def d_room_3a():
    print("You walk into a bright room, with gold all around.")
    print("Your greed takes over.")
    print("YOU WIN!")

def d_room_3b():
   print("You see the queen alive and well")
   print("You grab the queen and return to the castle.")
   print("The king and the princess praise you.")
   print("YOU WIN!")

def d_room_3c():
    print("You enter the room, it reeks of rot.")
    print("You see the queen's dead body infront of you.")
    print("YOU LOSE! :(")

def king():
    talked_to_king = 0
    print("You enter the king's tower")
    print("You see the King sitting on a chair crying.")
    print("King: Hello, I-I-I've lost my queen, can you find her?")
    choice = input("Do you help the king find the queen? Yes or No: ").strip().lower()
    if choice == "yes":
        print("Your journey has truly begun, head to the dungeon to find the queen.")
        talked_to_king += 1
    elif choice == "no":
        print("King: THEN GET OUT!")
    else:
        print("It's a yes or no question.")
    return talked_to_king    

#GAGE!!!!! it worksssssssssssssssssss im so happy

def princess():
    talked_to_princess = 0
    print("You enter the princess' tower.") 
    print("The princess is sitting on her bed.")
    print("Princess: Hello, please please come in")
    answer = input("Princess: What brings you in these parts? ")
    print(f"Princess: Ooh {answer} is awesome")
    print("Princess: Im so very sorry to kill the mood, but my mother has gone missing. Will you find her.")
    answer2 = input("Will you go find the queen? ")
    if answer2 == "no":
        print("Princess: That's fine.")
    elif answer2 == "yes":
        print("Princess: Thank you.")
        talked_to_princess += 1
    return talked_to_princess

def inv_check(thing):
    global inventory
    remove = inventory.index(thing)
    if thing in inventory:
        inventory.pop(remove)

def game():
    name = input("What is your name? ").strip().title()
    print(f"Hello {name} welcome to {kingdom}.")
    controls()
    global inventory
    global nothing
    global playing_value
    in_area1 = 1
    in_area2 = 0
    in_dungeon = 0
    in_castle = 0
    king_status = 0
    princess_status = 0
    while playing_value == 1:
        if in_area1 == 1:
            while in_area1 == 1 :
                area1_answ = area1()
                if area1_answ == "backwards":
                    d1_answ = d_room1()
                    if d1_answ == "forwards":
                        in_area1 -= 1
                        in_dungeon += 1
                        break
                    elif d1_answ == "backwards":
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
                        print("You leave the Barbershop.")
                    elif b_value == 2:
                        print("You leave the Barbershop with a new cut.")
                        inv_check(nothing)
                elif area1_answ == "forwards":
                    print("You go fowards.")
                    in_area1 -= 1
                    in_area2 += 1
                    break
                elif area1_answ == "inv":
                    print(inventory)
                elif area1_answ == "help":
                    controls()
                else:
                    print("You cannot do that now.")
        if in_dungeon == 1:
            while in_dungeon == 1:
                d2_answ = d_room2()
                if d2_answ == "sword" and "Sword" in inventory:
                    print("You slay the ogre.")
                    if king_answ != 1 and princess_answ != 1:
                        d_room_3a()
                        playing_value -= 1
                        break
                    elif king_answ != 1 and princess_answ == 1:
                        d_room_3b()
                        playing_value -= 1
                        break
                    elif king_answ == 1 and princess_answ != 1:
                        d_room_3c()
                        playing_value -= 1
                        break
                    elif king_answ == 1 and princess_answ == 1:
                        d_room_3c()
                        playing_value -= 1
                        break
                elif d2_answ == "a fresh cut" and "A fresh cut" in inventory:
                    print("The ogre sees your fresh cut.")
                    print("You have successfuly rizzed up the ogre, YOU WIN!")
                    playing_value -= 1
                    break
                elif d2_answ == "backwards":
                    print("You exit the dungeon.")
                    in_dungeon -= 1
                    in_area1 += 1
                elif d2_answ == "forwards":
                    print("You walk forwards but the ogre stops you.")
                elif d2_answ == "inv":
                    print(inventory)
                elif d2_answ == "help":
                    controls()
        if in_area2 == 1:
            while in_area2 == 1:
                area2_answ = area2()
                if area2_answ == "backwards":
                    print ("You turn back")
                    in_area2 -= 1
                    in_area1 += 1
                elif area2_answ == "forwards":
                    in_area2 -= 1
                    in_castle += 1
                elif area2_answ == "inv":
                    print(inventory)
                elif area2_answ == "help":
                    controls()
        if in_castle == 1:
            while in_castle == 1:
                c_answ  = castle()
                if c_answ == "forwards":
                    print("You cannot do that here.")
                elif c_answ == "backwards":
                    print("You leave the castle.")
                    in_castle -= 1
                    in_area2 += 1
                elif c_answ == "left":
                    king_answ = king()
                    if king_answ == 1:
                        king_status += 1
                elif c_answ == "right":
                    princess_answ = princess()
                    if princess_answ == 1:
                        princess_status += 1
                elif c_answ == "inv":
                    print(inventory)
                elif c_answ == "help":
                    controls()

game()