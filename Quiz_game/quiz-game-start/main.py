from data import question_data # Importing the question_data from data.py
from question_model import Question
from quiz_brain import QuizBrain # Importing the Question class from question_model.py

question_bank = [] # Creating an empty list to store the questions

for question in question_data: # Looping through the question_data
    text = question["text"] # Extracting the text from the question_data
    answer = question["answer"] # Extracting the answer from the question_data
    new_question = Question(text, answer) # Creating a new Question object
    question_bank.append(new_question) # Adding the new question to the question_bank



quiz=QuizBrain(question_bank) 
while quiz.still_has_questions():
    quiz.next_question()
