# BO time of day

time = int(input("What is time in military time? (hhmm): "))

if time >= 2100 and time < 2400:
    print("Good night, fine sir and or mad'am. Rest well for tomorrow shall be a fine day.")
elif time >= 0 and time <500:
    print("Good sir and or mad'am! You need your rest. Please go to sleep.")
elif time >= 500 and time < 900:
    print("Good morning fine sir and or mad'am. The day is quite fond of you.")
elif time >= 900 and time <1200:
    print("Good day fine sir and or mad'am. It is quite the nice day for a stroll don't you think?")
elif time >= 1200 and time < 1600:
    print("Good afternoon fine sir and or mad'am. It is a great time for a picnic.")
elif time >= 1600 and time < 2100:
    print("Good evening fine sir and or mad'am. What would you like for dinner?")