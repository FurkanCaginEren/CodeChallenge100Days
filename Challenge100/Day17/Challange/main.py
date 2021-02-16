from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

brain = QuizBrain(0, question_bank)

for i in question_data:
    new_q = Question(i["text"], i["answer"])
    question_bank.append(new_q)


while brain.still_has_question():
    brain.next_question()

print("You've completed the quiz")
print(f"Your final score {brain.score}/{len(question_bank)}")
