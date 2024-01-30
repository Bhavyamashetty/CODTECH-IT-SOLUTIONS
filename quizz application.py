import random

def run_quiz():
    categories = ["General Knowledge", "Science", "History", "Geography"]
    
    questions = {
        "General Knowledge": [
            {
                "question": "What is the capital of France?",
                "choices": ["Berlin", "Paris", "London", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "choices": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                "answer": "William Shakespeare"
            }
        ],
        "Science": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Mars"
            }
        ],
        "History": [
            {
                "question": "Who was the first President of the United States?",
                "choices": ["Thomas Jefferson", "George Washington", "John Adams", "Abraham Lincoln"],
                "answer": "George Washington"
            },
            {
                "question": "In which year did World War II end?",
                "choices": ["1943", "1945", "1947", "1950"],
                "answer": "1945"
            }
        ],
        "Geography": [
            {
                "question": "Which river is the longest in the world?",
                "choices": ["Amazon", "Nile", "Yangtze", "Mississippi"],
                "answer": "Nile"
            },
            {
                "question": "What is the capital of Australia?",
                "choices": ["Sydney", "Melbourne", "Canberra", "Perth"],
                "answer": "Canberra"
            }
        ]
    }

    score = 0

    print("Welcome to the Quiz Application!")
    print("Categories: ", ", ".join(categories))

    for category in categories:
        print("\nCategory: ", category)
        category_questions = questions[category]
        random.shuffle(category_questions)

        for q in category_questions:
            print("\nQuestion: ", q["question"])
            for i, choice in enumerate(q["choices"], start=1):
                print(f"{i}. {choice}")

            user_answer = input("Your answer (Enter the number): ")
            user_answer = int(user_answer) - 1

            if q["choices"][user_answer] == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['answer']}\n")

    print("Quiz complete!")
    print(f"Your score: {score}/{len(categories) * len(category_questions)}")

if __name__ == "__main__":
    run_quiz()
