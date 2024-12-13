# Slot Machine
import random
def slots():
    list = ["🔔","🍒","7️⃣","BAR"]
    slotOne = random.choice(list)
    slotTwo = random.choice(list)
    slotThree = random.choice(list)
    defaultCredits = 1000
    winCredits = int(defaultCredits) + int(bet)
    loseCredits = int(defaultCredits) - int(bet)
    currentCredits = 
    bet = input ("Enter your bet amount between the amounts of: 1 and", currentCredits)
    playAgain = input ("Would you like to play again?")
    win = slotOne == slotTwo == slotThree
    lost = slotOne != slotTwo or slotThree
    print ("Welcome to slots! Take a seat.")
    print ("How much would you like to bet on this spin?")
    if bet > defaultCredits:
        breakpoint()
        print ("Invalid Input.")
        exit()
    print ("You have chosen to bet:", bet)
    breakpoint()
    print ("The slots read:",slotOne,slotTwo,slotThree)
    breakpoint()
    if win == True:
        breakpoint()
        defaultCredits + bet
        print ("Your new total is:", defaultCredits + bet)
        playAgain()
    
    if lost == True:
        breakpoint()
        defaultCredits - bet
        print ("Your new total is:", defaultCredits - bet)
        playAgain()
    if defaultCredits > 0:
        print ("You ran out of credits.")
        breakpoint()
        exit()
slots()

    