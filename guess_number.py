import random

def guess_number():
    best_score = None  # Tracks fewest attempts to win
    print("Welcome to the Number Guessing Game! Type 'q' anytime to quit.\n")
    
    while True:
        max_number, attempts = choose_difficulty()
        secret_number = random.randint(1, max_number)

        guess = None
        tries = 0
        
        while attempts > 0:
            guess_input = input(f"Guess a number between 1 and {max_number}: ")
            if guess_input.lower() == 'q':
                print("Quitting the game...")
                return
            try:
                guess = int(guess_input)
            except ValueError:
                print("Invalid input! Enter an integer.\n")
                continue

            if guess < 1 or guess > max_number:
                print("Your guess is out of range. Try again.\n")
                continue  # don’t count this attempt

            attempts -= 1
            tries += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {tries} tries!\n")
                if best_score is None or tries < best_score:
                    best_score = tries
                    print(f"🏆 New best score: {best_score} attempts!\n")
                break

            # Hot & Cold hint
            difference = abs(secret_number - guess)
            if difference <= 2:
                print("🔥 Very hot!\n")
            elif difference <= 5:
                print("🌡️ Hot!\n")
            else:
                print("❄️ Cold\n")
        
        else:
            print(f"😔 Sorry! You couldn't guess the number. It was {secret_number}.\n")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

def choose_difficulty():
    
    while True:
        difficulty = input("Please enter the difficulty level for the game (easy, medium, hard): ").lower()
        if difficulty == "easy":
            max_number = 10
            attempts = 5
            return max_number, attempts
        elif difficulty == "medium":
            max_number = 20
            attempts = 4
            return max_number, attempts
        elif difficulty == "hard":
            max_number = 50
            attempts = 3
            return max_number, attempts
        else:
            print("Invalid difficulty. Please choose easy, medium, or hard.\n")
            continue

# Start the game
guess_number()
