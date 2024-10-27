def trivia_game():
    print("Welcome to the Trivia Quiz!")
    
    # Define a dictionary with questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the boiling point of water in degrees Celsius?": "100",
        "Who painted the Mona Lisa?": "Leonardo da Vinci"
    }

    # Iterate over the questions
    for question, answer in questions.items():
        user_answer = input(question + " ").strip()
        
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {answer}")
    
    print("Thanks for playing!")

# Run the trivia game
trivia_game()