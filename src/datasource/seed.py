from src.domain.option import Option
from src.domain.question import Question
from src.domain.quiz import Quiz
from src.domain.py_object_id import PyObjectId

FIRST_SEEDED_QUIZ_ID = "666f6f2d6261722d71757578"
FIRST_SEEDED_QUIZ_FIRST_QUESTION_ID  = "666f6f2d6261722d71757567"
FIRST_SEEDED_QUIZ_FIRST_QUESTION_OPTION_ID  = "666f6f2d6261722d71757432"

def generate_quizzes():
    option_11 = Option(_id= PyObjectId(FIRST_SEEDED_QUIZ_FIRST_QUESTION_OPTION_ID) ,label="if")
    option_12 = Option(label="print")
    option_13 = Option(label="x=1")
    option_14 = Option(label="=")
    question_1 = Question(_id=PyObjectId(FIRST_SEEDED_QUIZ_FIRST_QUESTION_ID),label="Which one is a valid example of selection?", answer_id=option_11.id)
    question_1.options=[option_11.dict(by_alias=True),option_12.dict(by_alias=True),
                        option_13.dict(by_alias=True),option_14.dict(by_alias=True)]
    option_21 = Option(label="!=")
    option_22 = Option(label="=")
    option_23 = Option(label="==")
    option_24 = Option(label="<=")
    question_2 = Question(label="Which one is NOT a comparison operator?", answer_id=option_22.id)
    question_2.options=[option_21.dict(by_alias=True),option_22.dict(by_alias=True),
                        option_23.dict(by_alias=True),option_24.dict(by_alias=True)]

    option_31 = Option(label="We would use else if for more than two selection conditions.")
    option_32 = Option(label="We would use else if for only one selection condition.")
    option_33 = Option(label="We would use else if for calculating the modulus of a division.")
    option_34 = Option(label="We would use else if as a type of iteration")
    question_3 = Question(label="Select the relevant description for else if?", answer_id=option_31.id)
    question_3.options=[option_31.dict(by_alias=True), option_32.dict(by_alias=True),
                        option_33.dict(by_alias=True),option_34.dict(by_alias=True)]

    quiz_python = Quiz(_id=PyObjectId(FIRST_SEEDED_QUIZ_ID), label="Selection in Python")
    quiz_python.questions= [question_1.dict(by_alias=True),question_2.dict(by_alias=True),question_3.dict(by_alias=True)]

    option_111 = Option(label="Milan")
    option_122 = Option(label="Venice")
    option_133 = Option(label="Rome")
    option_144 = Option(label="Naples")
    question_11 = Question(label="In which Italian city can you find the Colosseum?",answer_id=option_133.id)
    question_11.options=[option_111.dict(by_alias=True),option_122.dict(by_alias=True),
                        option_133.dict(by_alias=True),option_144.dict(by_alias=True)]
    option_211 = Option(label="Asia")
    option_222 = Option(label="Africa")
    option_233 = Option(label="Europe")
    option_244 = Option(label="North America")
    question_22 = Question(label="What is the largest continent in size?",answer_id=option_211.id)
    question_22.options=[option_211.dict(by_alias=True),option_222.dict(by_alias=True),
                        option_233.dict(by_alias=True),option_244.dict(by_alias=True)]

    option_311 = Option(label="Amazon River")
    option_322 = Option(label="Nile")
    option_333 = Option(label="Yellow River")
    option_344 = Option(label="Congo River")
    question_33 = Question(label="What is the longest river in the world",answer_id=option_322.id)
    question_33.options=[option_311.dict(by_alias=True),option_322.dict(by_alias=True),
                         option_333.dict(by_alias=True),option_344.dict(by_alias=True)]

    quiz_general = Quiz( label="General knowladge")
    quiz_general.questions = [question_11.dict(by_alias=True),question_22.dict(by_alias=True),question_33.dict(by_alias=True)]

    quizzes = [quiz_python.dict(by_alias=True),quiz_general.dict(by_alias=True)]
    return quizzes
