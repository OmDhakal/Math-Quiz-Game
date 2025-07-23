import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])

    # Ensure clean division (no zero, no decimals)
    if operation == '/':
        num1 = num1 * num2  # Makes result an integer

    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    return question, correct_answer

def math_quiz():
    print("🔢 Welcome to the Math Quiz Game!")
    score = 0

    for i in range(1, 6):  # 5 questions
        question, correct_answer = generate_question()
        print(f"\nQuestion {i}: {question} = ?")

        # Loop until valid number is entered
        while True:
            user_input = input("Your answer: ")
            try:
                user_answer = float(user_input)
                break  # Valid input, exit loop
            except ValueError:
                print("⚠️ Please enter a valid number.")

        # Check if user's answer is correct
        if abs(user_answer - correct_answer) < 0.001:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {correct_answer}")

    # Show final score
    print(f"\n🎉 Quiz finished! Your score: {score}/5")

# Run the game
math_quiz()




