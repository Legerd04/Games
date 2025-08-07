import random
while True:
        stone = "stone"
        paper = "paper"
        scissors = "scissors"
        print ("You will play Stone, Paper, Scissors against the computer.")
        valid_choices = ['stone', 'paper', 'scissors']
        while True:
                answer = input("Enter your choice (stone/paper/scissors): ").strip().lower()
                if answer in valid_choices:
                        print(f"You chose: {answer}")
                        break  # Exit loop if input is valid
                else:
                        print("Don't try to play fool with me Nigesh! No it's very bad!!")
        
        pc_choice = random.choice(valid_choices)
        print(f"Computer chose: {pc_choice}")
        if answer == pc_choice:
                print("It's a tie!")
        elif (answer == stone and pc_choice == scissors) or \
                (answer == paper and pc_choice == stone) or \
                (answer == scissors and pc_choice == paper):
                print("You win! Lesgooooo!")
        else:
                print("You lose! Lol loser XD!")

        play_again=input ("Do you wanna play again (yes/no): ").strip().lower() 
        if play_again == "yes":
                continue
        else:
                print("Thanks for playing")
                break
    





    