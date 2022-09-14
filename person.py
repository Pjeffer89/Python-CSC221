# Patrick Jeffers   Lab 11-3   3/18/2022
# This is the first part of exercise 11-3 in the book.

# Create Superclass Person.
class Person:
    def __init__(self, name, address, phoneNumber):     # Initialize attributes.
        self.__name = name
        self.__address = address
        self.__phoneNumber = phoneNumber
        
    def set_name(self, name):                                         # Setters.
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
        
    def set_phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber
             
    def get_name(self):                                               # Getters.
        return self.__name
        
    def get_address(self):
        return self.__address
        
    def get_phoneNumber(self):
        return self.__phoneNumber
    
# Create Subclass Customer.
class Customer(Person):
    def __init__(self, name, address, phoneNumber, customerNumber, mailingList):
        Person.__init__(self, name, address, phoneNumber)
        self.__customerNumber = customerNumber       # Call Person __init__ then
        self.__mailingList = mailingList           # initialize additional attr.
        
    def set_customerNumber(self, customerNumber):                     # Setters.
        self.__customerNumber = customerNumber
        
    def set_mailingList(self, mailingList):
        self.__mailingList = mailingList
        
    def get_customerNumber(self):                                     # Getters.
        return self.__customerNumber
    
    def get_mailingList(self):
        return self.__mailingList