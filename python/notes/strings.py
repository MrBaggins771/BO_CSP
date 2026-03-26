color1 = input("What is your favorite color? ").strip().upper()
color2 = input("What is your favorite color? ").strip().lower()
color3 = input("What is your favorite color? ").strip().capitalize()
color4 = input("What is your favorite color? ").strip().title()
print(color1, "is a really cool color!")

alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = "the quick brown fox jumps over the lazy dog."
print(alphabet[4:8])
word = input("What word do you want to change? ")
new = input("What will the new word be? ")
start = sentence.find(word)
print("("+sentence[start:start+len(word)]+")")
print(sentence)
sentence = sentence.replace(word,new)
print(sentence)

number = int(input("tell me a number: "))
print(number/5)

room = "Ms.LaRoss's room"
quote = 'Treyson said, "Yolo"'