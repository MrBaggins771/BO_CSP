ages = [22,23,25,28,34,36,38,39]
names = ["alex","katie","andrew","vienna","tia"]
print(names[4])
print(len(names))
print(names)
names[0] = "eric"
names.append("jayshree") #adds to list
index = names.index("vienna")
names.pop(index) #removes rom list
print(names)

for name in names:
    print(f"hello {name}")

for number in ages:
    print(f"{number} squared is {number ** 2}")

for i in range(20):
    print(f"it is the {i} iteration of this loop")