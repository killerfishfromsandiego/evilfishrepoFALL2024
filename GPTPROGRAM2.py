import random

def generate_powerball_numbers():
    print("Welcome to the PowerBall Number Generator!")
    print("This program will generate six numbers for your PowerBall ticket.")
    
    # Generate five white ball numbers (1-69)
    white_balls = random.sample(range(1, 70), 5)
    # Sort the numbers for easier reading
    white_balls.sort()
    
    # Generate one red ball number (1-26)
    red_ball = random.randint(1, 27)

    # Format the output
    print("Your PowerBall numbers are:")
    print(" ".join(map(str, white_balls)) + "   " + str(red_ball))

    print("Good luck, and may the odds be in your favor!")

# Run the PowerBall number generator
generate_powerball_numbers()
