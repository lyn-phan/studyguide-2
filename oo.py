# Create your classes here
"""Part 1: Classes and Init Methods"""


class Student(object):
    """Student info"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Questions and answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

class Exam(object):
    """Exam & questions"""

    def __init__(self, name, questions):
        self.name = name
        self.questions = []

#################################################################
"""Part 2: Methods"""

#1 - #2

class Student(object):
    """Student info"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Questions and answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
    
    def ask_and_evaluate(self):
        """asks question & prompts user for answer. It should return True or False, depending on answer"""

        answer = input(self.question + " > ")
        return self.correct_answer == answer

class Exam(object):
    """Exam & questions"""

    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)
    
    def administer(self):
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        
        return 100 * (float(score) / len(self.questions))

#########################################################################################
#part 3

class Student(object):
    """Student info"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Questions and answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
    
    def ask_and_evaluate(self):
        """asks question & prompts user for answer. It should return True or False, depending on answer"""

        answer = input(self.question + " > ")
        return self.correct_answer == answer

class Exam(object):
    """Exam & questions"""

    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)
    
    def administer(self):
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        
        return 100 * (float(score) / len(self.questions))

class StudentExam(object):
    """stores a student, an exam, and student's score"""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None 

    def take_test(self):
    """administers the exame and assigns score to student exam instance"""
        self.score = self.exam.administer()

        print(f'Your exam score is {self.score}')
    
def example():
    """creates an exam, adds a few questions to the exam, creates a student & instantiates a StudentExam & administers the test"""

    exam = Exam("Final Exam")

    q1 = Question("What's the best Pokemon in PokemonGo?")
    exam.add_question(q1)

    q2 = Question("Which Pokemon is closest to your personality?")
    exam.add_question(q2)

    student = Student(
        "Lynda"
        "Phan"
        "100 Disneyland Drive"
    )

    Lynda_FinalExam = StudentExam(student, exam)

    Lynda_FinalExam.take_test()




