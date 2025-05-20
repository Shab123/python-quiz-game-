import random

quiz_data = {
    "Technology": [
        {
            "question": "What does HTML stand for?",
            "options": ["A. HighText Machine Language", "B. HyperText and links Markup Language", "C. HyperText Markup Language", "D. None of these"],
            "answer": "C",
            "explanation": "HTML stands for HyperText Markup Language and is used to create web pages."
        },
        {
            "question": "Which company developed the Java programming language?",
            "options": ["A. Microsoft", "B. Sun Microsystems", "C. Google", "D. IBM"],
            "answer": "B",
            "explanation": "Java was developed by Sun Microsystems in 1995."
        }
    ],
    "Geography": [
        {
            "question": "Which is the largest desert in the world?",
            "options": ["A. Sahara", "B. Gobi", "C. Antarctica", "D. Arctic"],
            "answer": "C",
            "explanation": "Although cold, Antarctica is classified as a desert and is the largest."
        },
        {
            "question": "Which river is the longest in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
            "answer": "B",
            "explanation": "The Nile is traditionally considered the longest river in the world."
        }
    ]
}

print("🎓 Welcome to the Advanced Quiz Game with Explanations!")
print("Choose a category:\n")

for i, category in enumerate(quiz_data, 1):
    print(f"{i}. {category}")

while True:
    try:
        selection = int(input("Enter the number of your chosen category: "))
        if 1 <= selection <= len(quiz_data):
            category = list(quiz_data.keys())[selection - 1]
            break
        else:
            print("Invalid category number.")
    except ValueError:
        print("Please enter a valid number.")

print(f"🧭 Starting Quiz in '{category}' Category\n")
questions = quiz_data[category]
random.shuffle(questions)

score = 0

for i, q in enumerate(questions, 1):
    print(f"Q{i}. {q['question']}")
    for opt in q['options']:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was {q['answer']}")
    print(f"💡 Explanation: {q['explanation']}")
    print("-" * 50)

print(f"\n🎉 You've completed the quiz! Final Score: {score}/{len(questions)}")
if score == len(questions):
    print("🏆 Perfect Score! You're a genius!")
elif score >= len(questions) // 2:
    print("👍 Good job!")
else:
    print("📘 Keep learning and try again!")
