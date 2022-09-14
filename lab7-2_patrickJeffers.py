# Patrick Jeffers   Lab 7-2   1/17/2022
# This program is based on chapter 7 exercise 2 in the book. The program gets a 
# number of sets from the user.  Based on this number of sets the program will 
# generate sets of 6 numbers between 1-69. The first 5 numbers are unique with
# the sixth being any number between 1-69.  The program then allows the user to 
# stop or continue generating as many sets as they choose. 

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
      import random                  # Imported for random selection capability.
      generateAgain = 'yes'                         # Variable for loop control.
      maxNumber = 69             # Sets the max range of numbers to choose from.
      fullNumberSet = []       # List created to hold number range to pull from.
      lotterySet = []                 # List created to hold each generated set.
      for num in range(1, maxNumber + 1):     # Fills list of full number range.
            fullNumberSet.append(num)      
      
      while generateAgain == 'yes':                              # Loop control.
            numberOfSets = int(input('How many sets of numbers would you'\
                                     ' like to generate? ')) # Getting number of
            print('\n' + 'Here are your generated sets.')    # sets and create
            print('-----------------------------')           # output heading.
      
# Based on the number of sets requested, the loop will create a 5 number list
# of unique random numbers. Then generate the python ball and append it to the
# end making the 6 number lottery ticket. Finally this will also display each 
# set as its created and the loop is interated through.
            for i in range(numberOfSets):
                  lotterySet = random.sample(fullNumberSet, k=5)
                  pythonBall = random.choice(fullNumberSet)
                  lotterySet.append(pythonBall)
                  print(lotterySet)

# This will allow the user to exit the program or go back and generate more sets
# of numbers.  Includes input validation for user entry.
            print('\n' + 'Would you like to generate more sets of numbers? ')
            generateAgain = input('Enter "yes" or "no": ')
            while generateAgain.lower() not in ('yes', 'no'):
                  generateAgain = input('Invalid Entry. Enter "yes" or "no": ')
            if generateAgain == 'no':
                  break
            print()     

# Calls main to start program.      
main()