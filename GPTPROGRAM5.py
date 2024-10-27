def red_text(text):
    return f"\033[91m{text}\033[0m"

def green_text(text):
    return f"\033[92m{text}\033[0m"

def blue_text(text):
    return f"\033[94m{text}\033[0m"

def yellow_text(text):
    return f"\033[93m{text}\033[0m"

def brown_text(text):
    return f"\033[33m{text}\033[0m"

def main():
    print("Welcome to the Color Text Display!")
    
    # Display text in different colors
    print(red_text("This text is red!"))
    print(green_text("This text is green!"))
    print(blue_text("This text is blue!"))
    print(yellow_text("This text is yellow!"))
    print(brown_text("This text is brown!"))
    
    # User input for custom color and text
    color_choice = input("Choose a color (red, green, blue, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    if color_choice == "red":
        print(red_text(user_text))
    elif color_choice == "green":
        print(green_text(user_text))
    elif color_choice == "blue":
        print(blue_text(user_text))
    elif color_choice == "yellow":
        print(yellow_text(user_text))
    elif color_choice == "brown":
        print(brown_text(user_text))
    else:
        print("Invalid color choice!")

# Run the main program
if __name__ == "__main__":
    main()
