# Patrick Jeffers   Lab 10-2   3/3/2022
# This is the first part of exercise 10-2 in the book.  It will be imported and 
# used by the main lab program.  This module stores the class Car.

class Car:
    def __init__(self, year, make):            # Init method for Car attributes.
        self.__year_model = year
        self.__make = make
        self.__speed = 0
        
    def accelerate(self):                                   # Accelerate method.
        self.__speed += 5
            
    def brake(self):                                             # Brake method.
        self.__speed -= 5
            
    def get_speed(self):                                     # Get Speed method.
        return self.__speed                             # Returns current speed.