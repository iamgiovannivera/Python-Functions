# 4. The Quiz Game

# Task 1: 
    
# questions = [
#     "What is the capital of France?",
#     "What is the largest planet in our solar system?",
#     "Who wrote 'To Kill a Mockingbird'?",
#     "What is the chemical symbol for water?",
#     "How many continents are there on Earth?"
# ]

# answers = [
#     "Paris",
#     "Jupiter",
#     "Harper Lee",
#     "H2O",
#     "7"
# ]

# # Task 2: 
    
# def quiz_user(questions, answers):
#     user_answers = []
#     for question in questions:
#         user_answer = input(question + " ")
#         user_answers.append(user_answer)
#     return user_answers

# # Task 3: 
    


# def score_quiz(questions, answers, user_answers):
#     score = 0
#     for correct_answer, user_answer in zip(answers, user_answers):
#         if correct_answer.lower() == user_answer.lower():
#             score += 1
#     return score

# def main():
#     print("Welcome to the Quiz Game!")
#     user_answers = quiz_user(questions, answers)
#     score = score_quiz(questions, answers, user_answers)
#     print(f"\nYou scored {score} out of {len(questions)}.")

# if __name__ == "__main__":
#     main()