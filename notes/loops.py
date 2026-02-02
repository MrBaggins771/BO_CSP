import random #always at the top

"""start = 0
while start <= 10:
    print(start)
    start += 1

count = 1
goose = random.randint(1,10)
while count != goose:
    print("Duck")
    count += 1
print("GOOSE!")"""

number = random.randint(1,25)
while True:
    guess = int(input("guess a number between 1 and 25: "))
    if guess == number:
        print(f"yes the number was {number}, you won!")
        break #break only works in loops and takes us out of the loop.
    elif guess > 25 :
        print("I asked for a number between 1 and 25. Do better.")
    elif guess < number:
        print("guess higher")
    else:
        print("guess lower")

