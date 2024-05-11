day = int(input('Day (0-6)? '))
if day == 0:
    print("Sleep in")
elif day == 1:
    print("Go to work")
elif day == 2:
    print("Go to work")
elif day == 3:
    print("Go to work")
elif day == 4:
    print("Go to work")
elif day == 5:
    print("Go to work") 
elif day == 6:
    print("Sleep in")

day = int(input('Day of the week? (0-6) '))

if day == 0 or 6:
    sleep = True

if sleep:
    print ("Sleep in")
else:
    print ("Go to work")
