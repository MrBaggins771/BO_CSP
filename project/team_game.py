# BO 3 team python game

kingdom = "The Silent Kingdom"
name = input("What is thy name: ").strip().title()
inventory = []

def game():
    print(f"You made it to {kingdom}, y")

def tutorial():
    print(f"Hello {name}. Welcome to {kingdom}.")
    print("This is the tutorial, you will learn what to do and how to do it.")
    print("If you are met with a choice the answers will be next to the question. EX: You are met with a fork in the road (LEFT/RIGHT).")
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

start()