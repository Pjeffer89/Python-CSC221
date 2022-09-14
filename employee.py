# Patrick Jeffers   Lab 11-1   3/15/2022
# This is the first part of exercise 11-1 in the book.

# Create Superclass
class Employee:
    def __init__(self, employeeName, employeeNumber):   # Initialize attributes. 
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber
        
    def set_employeeName(self, employeeName):                         # Setters.
        self.__employeeName = employeeName
        
    def set_employeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber
        
    def get_employeeName(self):                                       # Getters.
        return self.__employeeName
        
    def get_employeeNumber(self):
        return self.__employeeNumber
        
# Create Subclass
class ProductionWorker(Employee):
    def __init__(self, employeeName, employeeNumber, shiftNumber, payRate):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__shiftNumber = shiftNumber           # Call Employee __init__ then 
        self.__payRate = payRate                   # initialize additional attr.
        
    def set_shiftNumber(self, shiftNumber):                           # Setters.
        self.__shiftNumber = shiftNumber
        
    def set_payRate(self, payRate):
        self.__payRate = payRate
        
    def get_shiftNumber(self):                                        # Getters.
        return self.__shiftNumber
    
    def get_payRate(self):
        return self.__payRate