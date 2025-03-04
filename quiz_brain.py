class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """
        Check if there are any questions left in the question_list\n
        """
        return self.question_number < len(self.question_list)

    # self is a reference to the current instance of the class
    def next_question(self):
        """
         Get the current question from the question_list\n
         self.question_number is the index of the current question\n
         self.question_list is the list of questions
        """
        current_q = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False):\n")
            if user_answer.lower() in ["true", "false"]:
                break
            else:
                print("Please type 'True' or 'False'.")

        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right')
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


