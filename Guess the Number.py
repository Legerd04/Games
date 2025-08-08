import random
while True:
    a = random.randint(1, 100)
    attempt = 0 
    print ("I'm thinking of a random number between 1-100. You have 10 guesses to find it.")
    while True:
        if attempt == 10:
            print (f"You failed. The number was {a}")
            break
        while True:
                try:
                        guess = int(input("Enter your guess: "))
                        attempt = attempt+1
                        print ("attempts left: "+str(10-attempt))
                        break
                except ValueError:
                        print("Invalid input! Please enter a number.")
                        continue
        if guess < a:
                print("Too low! Try again.")
        elif guess > a:
                print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number: {a}")
            break
    if input("Do you want to continue? (yes/no): ").strip().lower() != "yes":
        print("Thanks for playing!")
        break
    else:
        print("Let's do it")
        continue
# End of the game
# This is the end of the code 
