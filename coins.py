coins = 0 
print("You have %d coins" % coins)

coin_offer = True

while coin_offer == True:
    coin_offer = input("Do you want a coin? ").lower()
    if coin_offer == "yes":
        coins = coins + 1
        print("You have %d coins" % coins)
        coin_offer = True
    else:
        print("Bye")

