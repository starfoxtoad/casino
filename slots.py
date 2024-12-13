# Slot Machine
import random
def slots():
    list = ["🔔","🍒","7️⃣","BAR"]
    slotOne = random.choice(list)
    slotTwo = random.choice(list)
    slotThree = random.choice(list)
    defaultCredits = 1000
    win = slotOne == slotTwo == slotThree
    lost = slotOne != slotTwo or slotThree
    print ("Welcome to slots! Take a seat.")
    print ("How much would you like to bet on this spin?")
    bet = input ("Enter your bet amount:")
    if bet > defaultCredits:
        breakpoint()
        print ("Invalid Input.")
        exit()
    print ("You have chosen to bet:", bet)
    print ("The slots read:",slotOne,slotTwo,slotThree)
    if win == True:
        defaultCredits + bet
        print ("Your new total is:",defaultCredits + bet)
    if lost== True:
        defaultCredits - bet
        print ("Your new total is:",defaultCredits-bet)
    if defaultCredits > 0:
        print ("You ran out of credits.")
        exit()
slots()

    