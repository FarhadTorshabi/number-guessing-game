import random

def guess_number():
    best_score = None  # Tracks fewest attempts to win
    print("Welcome to the Number Guessing Game! Type 'q' anytime to quit.\n")
    
    while True:
        # Get range from user
        try:
            first_input = input("Enter the start of the range (or 'q' to quit): ")
            if first_input.lower() == 'q':
                break
            first = int(first_input)
            
            end_input = input("Enter the end of the range (or 'q' to quit): ")
            if end_input.lower() == 'q':
                break
            end = int(end_input)
            
        except ValueError:
            print("Invalid input! Please enter an integer.\n")
            continue

        if first >= end:
            print("Start number must be less than end number.\n")
            continue

        secret_number = random.randint(first, end)
        attempts = 0
        max_attempts = 5
        guess = None

        while attempts < max_attempts:
            guess_input = input(f"Guess a number between {first} and {end}: ")
            if guess_input.lower() == 'q':
                print("Quitting the game...")
                return
            try:
                guess = int(guess_input)
            except ValueError:
                print("Invalid input! Enter an integer.\n")
                continue

            if guess < first or guess > end:
                print("Your guess is out of range. Try again.\n")
                continue  # don’t count this attempt

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} tries!\n")
                if best_score is None or attempts < best_score:
                    best_score = attempts
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

# Start the game
guess_number()