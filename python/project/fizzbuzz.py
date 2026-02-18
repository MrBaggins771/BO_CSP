# BO fizz buzz

num = 0
while num < 50:
    num += 1
    if num % 3 == 0 and num % 5 == 0: 
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0: 
        print("Fizz")
    else:
        print(num)