import random
print("Welcome to the Casino. Games are under maintenance as of current.")
print ("1. Roulette")
def roulette():
  list = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]
  print("Welcome to Roulette!")
  print("Bet on a number between 0 and 36, or a color.")
  # Asks the user if they want to bet on a number or color.
  colorBet = input("Would you like to bet on a color? (y/n): ")
  # If a user inputs a non Yes or No input, code ends.
  if colorBet != "y" and colorBet != "n":
    print("Invalid input. Please try again.")
    exit()
    # If a user inputs a Yes, they will be asked to bet on a color.
  if colorBet != "n":
    print("What color would you like to bet on?")
    print("1. Red")
    print("2. Black")
    color = input("Enter your choice: ")
    # If the users chooses to bet on Red, it will select from a list of either red or black. If it lands on red, they win. If it lands on black, they lose.
    if color == "1":
      print("You have chosen to bet on Red.")
      print("The ball is spinning...")
      color = random.choice(["Red", "Black"])
      print("The ball landed on", color)
      if color == "Red":
        print("Congratulations! You won!")
        exit()
      else:
        print("Sorry, you lost.")
        exit()
        # If the users chooses to bet on Black, it will select from a list of either red or black. If it lands on red, they lose. If it lands on black, they win.
    if color == "2":
          print("You have chosen to bet on Black.")
          print("The ball is spinning...")
          color = random.choice(["Red", "Black"])
          print("The ball landed on", color)
          if color == "Black":
            print("Congratulations! You won!")  
            exit()
          else:
            print("Sorry, you lost.")
            exit()
      # Prevents the user from selecting a color that is not available.
    elif color != "1" or "2":
      print("Invalid choice. Please try again.")
      exit()  
      # If the users chooses not to bet on a color, they will be asked to bet on a number.
  if colorBet == "n" :
    print("Okay. Input a number between 0 and 36.")
  bet = input()
  spin = random.choice(list)
  if bet == spin:
    print("You win!")
    print("That low Taper fade meme is still massive btw")
    exit()
  else:
    print("You lose!")
    print ("The wheel landed on...")
    print (spin)
  exit()
print ("2. Blackjack.")
def blackjack() :
  print ("Welcome to Blackjack. In this game, you need to get as close to 21 as possible without going over. You face an AI dealer, which has some tricks up his sleeve.")
      # H means Hard, N Means Normal, E means easy.
  print ("Select Dealer Difficulty:")
  print ("1. Hard")
  print ("2. Normal")
  print ("3. Easy")
  dealerDifficulty = input ("Input desired difficulty.")
  if dealerDifficulty == "1":
      print ("You have chosen: Hard Difficulty.")
      print ("The deck has been chosen. Cards are being dealt.")
      # Functions to use throughout code
      dcardOne = random.randint(8,11)
      dcardTwo = random.randint(8,10)
      hdealerHand = dcardOne + dcardTwo
      cardOne = random.randint(1,11)
      cardTwo = random.randint(1,11)
      cardThree = random.randint(1,11)
      cardFour = random.randint(1,11)
      cardFive = random.randint (1,11)
      baseHand = cardOne + cardTwo
      sumTotal = cardOne + cardTwo + cardThree
      newsumTotal = cardOne + cardTwo + cardThree + cardFour
      newestsumTotal = cardOne + cardTwo + cardThree + cardFour + cardFive
      print ("Your hand is:", baseHand)
      decision1 = input("With this knowledge, would you like to hit or stand? (h/s):")
    # if the input is not s, you will hit, creating the new sumTotal.
      if decision1 != "s":
        print ("You have chosen to hit. Your new total is:", sumTotal)
        decision2 = input("With this knowledge, would you like to hit or stand? (h/s):")
        if decision2 != "s":
          print ("You have chosen to hit again. Your new total is:", newsumTotal)
          decision3 = input("This is the final hit oppurtunity. Would you like to hit or stand? (h/s):")
          if decision3 != "s":
            print ("You have chosen to hit again. Your new total is:", newestsumTotal)
            print ("The dealer had:", hdealerHand)
            if hdealerHand > newestsumTotal:
                print ("You lose. Dealer had:", hdealerHand, "you had:", newestsumTotal)
            if hdealerHand < baseHand:
                print ("You win! You had:", newestsumTotal, "Dealer had:", hdealerHand)
          if decision3 == "s":
            print("You have chosen to stand. Your current total is:", newsumTotal)
            print ("The dealer had:", hdealerHand)
            if hdealerHand > newsumTotal:
                  print ("You lose. Dealer had:", hdealerHand, "you had:", newsumTotal)
            if hdealerHand < newsumTotal:
                  print ("You win! You had:", newsumTotal, "Dealer had:", hdealerHand)
        if decision2 == "s":
          print ("You have chosen to stand. Your current total is:", sumTotal)
          print ("The dealer had:", hdealerHand)
          if hdealerHand > sumTotal:
              print ("You lose. Dealer had:", hdealerHand, "you had:", sumTotal)
          if hdealerHand < sumTotal:
              print ("You win! You had:", sumTotal, "Dealer had:", hdealerHand)
      if decision1 == "s":
          print ("You have chosen to stand. Your current total is:", baseHand)
          print ("The dealer had:", hdealerHand)
          if hdealerHand > baseHand:
              print ("You lose. Dealer had:", hdealerHand, "you had:", baseHand)
          if hdealerHand < baseHand:
              print ("You win! You had:", baseHand, "Dealer had:", hdealerHand)
  if dealerDifficulty == "2":
      print ("You have chosen: Normal Difficulty.")
      print ("The deck has been chosen. Cards are being dealt.")
      # Functions to use throughout code
      dcardOne = random.randint(5,11)
      dcardTwo = random.randint(5,10)
      ndealerHand = dcardOne + dcardTwo
      cardOne = random.randint(1,11)
      cardTwo = random.randint(1,11)
      cardThree = random.randint(1,11)
      cardFour = random.randint(1,11)
      cardFive = random.randint (1,11)
      baseHand = cardOne + cardTwo
      sumTotal = cardOne + cardTwo + cardThree
      newsumTotal = cardOne + cardTwo + cardThree + cardFour
      newestsumTotal = cardOne + cardTwo + cardThree + cardFour + cardFive
      print ("Your hand is:", baseHand)
      decision1 = input("With this knowledge, would you like to hit or stand? (h/s):")
    # if the input is not s, you will hit, creating the new sumTotal.
      if decision1 != "s":
        print ("You have chosen to hit. Your new total is:", sumTotal)
        decision2 = input("With this knowledge, would you like to hit or stand? (h/s):")
        if decision2 != "s":
          print ("You have chosen to hit again. Your new total is:", newsumTotal)
          decision3 = input("This is the final hit oppurtunity. Would you like to hit or stand? (h/s):")
          if decision3 != "s":
            print ("You have chosen to hit again. Your new total is:", newestsumTotal)
            print ("The dealer had:", ndealerHand)
            if ndealerHand > newestsumTotal:
                print ("You lose. Dealer had:", ndealerHand, "you had:", newestsumTotal)
            if ndealerHand < baseHand:
                print ("You win! You had:", newestsumTotal, "Dealer had:", ndealerHand)
          if decision3 == "s":
            print("You have chosen to stand. Your current total is:", newsumTotal)
            print ("The dealer had:", ndealerHand)
            if ndealerHand > newsumTotal:
                  print ("You lose. Dealer had:", ndealerHand, "you had:", newsumTotal)
            if ndealerHand < newsumTotal:
                  print ("You win! You had:", newsumTotal, "Dealer had:", ndealerHand)
        if decision2 == "s":
          print ("You have chosen to stand. Your current total is:", sumTotal)
          print ("The dealer had:", ndealerHand)
          if ndealerHand > sumTotal:
              print ("You lose. Dealer had:", ndealerHand, "you had:", sumTotal)
          if ndealerHand < sumTotal:
              print ("You win! You had:", sumTotal, "Dealer had:", ndealerHand)
      if decision1 == "s":
          print ("You have chosen to stand. Your current total is:", baseHand)
          print ("The dealer had:", ndealerHand)
          if ndealerHand > baseHand:
              print ("You lose. Dealer had:", ndealerHand, "you had:", baseHand)
          if ndealerHand < baseHand:
              print ("You win! You had:", baseHand, "Dealer had:", ndealerHand)
  if dealerDifficulty == "3":
    print ("You have chosen: Easy Difficulty.")
    print ("The deck has been chosen. Cards are being dealt.")
    # Functions to use throughout code
    dcardOne = random.randint(1,11)
    dcardTwo = random.randint(1,10)
    edealerHand = dcardOne + dcardTwo
    cardOne = random.randint(1,11)
    cardTwo = random.randint(1,11)
    cardThree = random.randint(1,11)
    cardFour = random.randint(1,11)
    cardFive = random.randint (1,11)
    baseHand = cardOne + cardTwo
    sumTotal = cardOne + cardTwo + cardThree
    newsumTotal = cardOne + cardTwo + cardThree + cardFour
    newestsumTotal = cardOne + cardTwo + cardThree + cardFour + cardFive
    print ("Your hand is:", baseHand)
    decision1 = input("With this knowledge, would you like to hit or stand? (h/s):")
  # if the input is not s, you will hit, creating the new sumTotal.
    if decision1 != "s":
      print ("You have chosen to hit. Your new total is:", sumTotal)
      decision2 = input("With this knowledge, would you like to hit or stand? (h/s):")
      if decision2 != "s":
        print ("You have chosen to hit again. Your new total is:", newsumTotal)
        decision3 = input("This is the final hit oppurtunity. Would you like to hit or stand? (h/s):")
        if decision3 != "s":
          print ("You have chosen to hit again. Your new total is:", newestsumTotal)
          print ("The dealer had:", edealerHand)
          if edealerHand > newestsumTotal:
              print ("You lose. Dealer had:", edealerHand, "you had:", newestsumTotal)
          if edealerHand < baseHand:
              print ("You win! You had:", newestsumTotal, "Dealer had:", edealerHand)
        if decision3 == "s":
          print("You have chosen to stand. Your current total is:", newsumTotal)
          print ("The dealer had:", edealerHand)
          if edealerHand > newsumTotal:
                print ("You lose. Dealer had:", edealerHand, "you had:", newsumTotal)
          if edealerHand < newsumTotal:
                print ("You win! You had:", newsumTotal, "Dealer had:", edealerHand)
      if decision2 == "s":
        print ("You have chosen to stand. Your current total is:", sumTotal)
        print ("The dealer had:", edealerHand)
        if edealerHand > sumTotal:
            print ("You lose. Dealer had:", edealerHand, "you had:", sumTotal)
        if edealerHand < sumTotal:
            print ("You win! You had:", sumTotal, "Dealer had:", edealerHand)
    if decision1 == "s":
        print ("You have chosen to stand. Your current total is:", baseHand)
        print ("The dealer had:", edealerHand)
        if edealerHand > baseHand:
            print ("You lose. Dealer had:", edealerHand, "you had:", baseHand)
        if edealerHand < baseHand:
            print ("You win! You had:", baseHand, "Dealer had:", edealerHand)
  if dealerDifficulty != "1" or "2" or "3":
          exit()
print ("3. Poker")
selection = input("Enter your selection: ")
if selection == "1":
  roulette()
if selection == "2":
  blackjack()
if selection == "3":
  poker()