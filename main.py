from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# question_data is a list of dictionaries, each dictionary has a "text" key and an "answer" key
# for each dictionary in question_data, create a new Question object and add it to question_bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0])

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

