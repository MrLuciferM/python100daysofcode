from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for each in question_data:
    question_bank.append(Question(each["question"], each["correct_answer"]))
    
print(question_bank[0].question, question_bank[0].answer)

quiz_brain = QuizBrain(question_bank)



while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz...")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")