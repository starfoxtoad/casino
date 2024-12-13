import random
def poker ():
    cards = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    acardOne = random.choice(cards)
    acardTwo = random.choice(cards)
    bcardOne = random.choice(cards)
    bcardTwo = random.choice(cards)
    ccardOne = random.choice(cards)
    ccardTwo = random.choice(cards)
    dcardOne = random.choice(cards)
    dcardTwo = random.choice(cards)
    cardOne = random.choice(cards)
    cardTwo = random.choice(cards)
    flop = random.choice(cards)
    turn = random.choice(cards)
    river = random.choice(cards)
    startingHand = cardOne + "and" + cardTwo
    astartingHand = acardOne +"and"+ acardTwo
    bstartingHand = bcardOne +"and"+ bcardTwo
    cstartingHand = ccardOne +"and"+ ccardTwo
    dstartingHand = dcardOne +"and"+ dcardTwo
    print ("Welcome to the poker table. To start, input yes to ante up.")
    anteUp = input("Would you like to play this hand of poker? (y/n):")
    if anteUp == "y":
        print("Your starting hand is:", startingHand)
        print ("The dealer has distributed cards to all players.")
        

    if anteUp == "n":
        exit()
    if anteUp != "y" or "n":
        print ("Invalid response.")
        exit()
poker()