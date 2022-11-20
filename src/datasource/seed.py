import datetime
from uuid import UUID 

from src.domain.option import Option
from src.domain.question import Question
from src.domain.quiz import Quiz
from bson import ObjectId

FIRST_SEEDED_QUIZ_ID = ObjectId('666f6f2d6261722d71757578')

def generate_quizzes():
    option_11 = Option(label="if")
    option_12 = Option(label="print")
    option_13 = Option(label="x=1")
    option_14 = Option(label="=")
    question_1 = Question(label="Which one is a valid example of selection?")
    question_1.options=[dict(option_11),dict(option_12),dict(option_13),dict(option_14)]
    question_2 = Question(label="Which one is NOT a comparison operator?")
    option_21 = Option(label="!=")
    option_22 = Option(label="=")
    option_23 = Option(label="==")
    option_24 = Option(label="<=")
    question_2.options=[dict(option_21),dict(option_22),dict(option_23),dict(option_24)]

    question_3 = Question(label="Select the relevant description for else if?")
    option_31 = Option(label="We would use else if for more than two selection conditions.")
    option_32 = Option(label="We would use else if for only one selection condition.")
    option_33 = Option(label="We would use else if for calculating the modulus of a division.")
    option_34 = Option(label="We would use else if as a type of iteration")
    question_3.options=[dict(option_31),dict(option_32),dict(option_33),dict(option_34)]

    quiz_python = Quiz(_id=FIRST_SEEDED_QUIZ_ID, label="Selection in Python")
    quiz_python.questions= [dict(question_1),dict(question_2),dict(question_3)]

    option_111 = Option(label="Milan")
    option_122 = Option(label="Venice")
    option_133 = Option(label="Rome")
    option_144 = Option(label="Naples")
    question_11 = Question(label="In which Italian city can you find the Colosseum?")
    question_11.options=[dict(option_111),dict(option_122),dict(option_133),dict(option_144)]
    question_22 = Question(label="What is the largest continent in size?")
    option_211 = Option(label="Asia")
    option_222 = Option(label="Africa")
    option_233 = Option(label="Europe")
    option_244 = Option(label="North America")
    question_22.options=[dict(option_211),dict(option_222),dict(option_233),dict(option_244)]

    question_33 = Question(label="What is the longest river in the world")
    option_311 = Option(label="Amazon River")
    option_322 = Option(label="Nile")
    option_333 = Option(label="Yellow River")
    option_344 = Option(label="Congo River")
    question_3.options=[dict(option_311),dict(option_322),dict(option_333),dict(option_344)]

    quiz_general = Quiz( label="General knowladge")
    quiz_general.questions = [dict(question_11),dict(question_22),dict(question_33)]

    quizzes = [dict(quiz_python),dict(quiz_general)]
    return quizzes

