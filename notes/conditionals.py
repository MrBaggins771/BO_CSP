"""number = -34

if abs(number) < 10:
    print(f"{number} is a single digit number.")
elif abs(number) < 100:
    print(f"{number} is a 2 digit number.")
else:
    print("your number is too big")"""

name = input("what is your name? ").strip().capitalize()
if name == "Xavier" or name == "Jake":
    print("I love your hair! How often do you dye it?")
    often = input("In months please! ")
    if int(often) < 3:
        print("Thats very often")
    else:
        print("cool")
else:
    print(f"Sup {name}")