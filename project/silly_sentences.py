# BO Silly Sentences

size = input("Give me a size: ").strip().lower()
place = input("Give me a place: ").strip().title()
verb = input("give me a past tense action verb: ").strip().lower()
name = input("Give me a name: ").strip().capitalize()
color = input("give me a color: ").strip().lower()
animal = input("Give me an animal: ").strip().upper()
full_animal =  size+" "+color+" "+animal

print("At the local " + place + ", " + name + " found a " + full_animal + "! " + name + " " + verb + " away.")