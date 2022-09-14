# Patrick Jeffers   Lab 10-9   3/3/2022
# This is the first part of exercise 10-9 in the book.  It will be imported and 
# used by the main lab program.  This module stores the class Question.

class Question:
    def __init__(self, triviaQuestion, answer1, answer2, answer3, answer4, \
                 correctAnswer):
        self.__triviaQuestion = triviaQuestion
        self.__answer1 = answer1
        self.__answer2 = answer2               # __init__ method for attributes.
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correctAnswer = correctAnswer
    
    def set__triviaQuestion(self, triviaQuestion):                  # Accessors.
        self.__triviaQuestion = triviaQuestion
        
    def set__answer1(self, answer1):
        self.__answer1 = answer1
        
    def set__answer2(self, answer2):
        self.__answer2 = answer2
        
    def set__answer3(self, answer3):
        self.__answer3 = answer3
        
    def set__answer4(self, answer4):
        self.__answer4 = answer4
        
    def set__correctAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer
        
    def get__triviaQuestion(self):                                   # Mutators.
        return self.__triviaQuestion
    
    def get__answer1(self):
        return self.__answer1
    
    def get__answer2(self):
        return self.__answer2
    
    def get__answer3(self):
        return self.__answer3
    
    def get__answer4(self):
        return self.__answer4
    
    def get__correctAnswer(self):
        return self.__correctAnswer  
    
    def __str__(self):                            # For display in main program.
        display = self.get__triviaQuestion() + '\n' + \
            '1: ' + self.get__answer1() + '\n' + \
            '2: ' + self.get__answer2() + '\n' + \
            '3: ' + self.get__answer3() + '\n' + \
            '4: ' + self.get__answer4()
        return display
        