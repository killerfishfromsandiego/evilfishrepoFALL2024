import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    play = input("Do you want to play? (yes/no): ").strip().lower()

    if play != "yes":
        print("Maybe next time!")
        return

    secret_number = random.randint(1, 10)
    guess = None

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You've guessed the number {secret_number}!")

# Run the number guessing game
number_guessing_game()
