from question_model import Question
from data import question_data as quest
from quiz_brain import QuizBrain


question = []

for c in range(0, len(quest)):
    text = quest[c]["text"]
    answer = quest[c]["answer"]
    new_question = Question(text= text,
                            answer= answer)
    question.append(new_question)


# for c in range(0, len(question)):
#     answer = str(input(f"{question[c].text} True/False:")).upper()[0]
#     if answer == question[c].answer:
#         print("You got it!")
#     else:
#         print("Wrong !")
# quiz = QuizBrain(question[0].text)
# print(quiz)


quiz = QuizBrain(question)

while quiz.still_has_questions():
    for c in range(0, len(question)):
        quiz.next_question()
        
    
print("You've complete the quiz")
print(f"You final score is: {quiz.score}")
