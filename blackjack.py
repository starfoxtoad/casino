import random
def blackjack():
    print ("Welcome to Blackjack. In this game, you need to get as close to 21 as possible without going over. You face an AI dealer, which has some tricks up his sleeve.")
    # H means Hard, N Means Normal, E means easy.
    nList = ["11","5","6","7","8","9","10","10","10","10","11","5","6","7","8","9","10","10","10","10","11","5","6","7","8","9","10","10","10","10","11","5","6","7","8","9","10","10","10","10"]
    eList = ["11","1","2","3","4","5","6","7","8","9","10","10","10","10","11","1","2","3","4","5","6","7","8","9","10","10","10","10","11","1","2","3","4","5","6","7","8","9","10","10","10","10","11","1","2","3","4","5","6","7","8","9","10","10","10","10"]
    print ("Select Dealer Difficulty:")
    print ("1. Hard")
    print ("2. Normal")
    print ("3. Easy")
dealerDifficulty = input ("Input desired difficulty.")
if dealerDifficulty == "1":
    print ("You have chosen: Hard Difficulty.")
    print ("The deck has been chosen. Cards are being dealt.")
    hList = ["11","8","9","10","10","10","King","11","8","9","10","10","10","King","11","8","9","10","10","10","10","11","8","9","10","10","10","10"]
    hdealerHand = random.choice(hList) + "" + random.choice(hList)
    cards = ["11","1","2","3","4","5","6","7","8","9","10","10","10","10","11","1","2","3","4","5","6","7","8","9","10","10","10","10","11","1","2","3","4","5","6","7","8","9","10","10","10","10","11","1","2","3","4","5","6","7","8","9","10","10","10","10"]
    playerHand = random.choice (cards) + random.choice (cards)
    print ("Your hand is:", playerHand)
    print ("With this knowledge, would you like to hit or stand? (h/s):")
    if input != "s":
        hit = print (random.choice(cards))
        print ("Your new hand sum total is:", playerHand + hit)
        print ("With this knowledge, would you like to hit or stand? (h/s):")
    if input == "s":
        print ("You have chosen to stand. Your current total is:", playerHand)
        print (hdealerHand)
    if input != "s" or "h":
        print ("Invalid Input. Banned for life.")
        exit()
if hdealerHand > playerHand:
    print ("You lose. Dealer had:", hdealerHand, "you had:",playerHand)
if hdealerHand < playerHand:
    print ("You win! You had:", playerHand, "Dealer had:", hdealerHand)

if dealerDifficulty == "2":
    print ("No balls.")
    exit()
if dealerDifficulty == "3":
    print ("You have literally no balls.")
    exit()
if input != "1" or "2" or "3":
    print ("Invalid. KYS.")
    exit()