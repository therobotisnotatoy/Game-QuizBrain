from lib import data_generator


# Question-answer class
class Question:

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


# listed data with mechanic to check user answers
class QuizBrain:

    def __init__(self, question_list: list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.game_size = len(self.question_list)
        self.goes_on = True

    # game mechanic
    def next_question(self, answer: str) -> tuple:
        this_question = self.question_list[self.question_number]

        if answer == this_question.answer:
            self.question_number += 1

            if self.question_number == self.game_size:
                self.goes_on = False
                return 2, "You Win!"
            else:
                next_question = self.question_list[self.question_number]
                return 1, next_question
        else:
            self.goes_on = False
            return 3, f"You finished the game with {self.question_number} right answers"


# Create current game data and put it into QuizBrain class
def build_new_game() -> QuizBrain:

    question_bank = data_generator.quiz_data()
    my_list = []
    for element in question_bank:
        my_list.append(Question(element["text"], element["answer"]))

    return QuizBrain(my_list)
