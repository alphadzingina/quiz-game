class QuizBrain:

    def __init__(self, q_list):
        """constructor method"""
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        """returns True if question_number is less than no of questions, false otherwise"""
        self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
