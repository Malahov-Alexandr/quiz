# TODO : asking a question

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list


    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number += 1
        input(f'{self.question_number}: {current_question.q_text} (True/False)')

# TODO: checking is the answer was correct



# TODO: checking if we are the end of the quiz