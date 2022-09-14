# Patrick Jeffers   Lab 8-5   1/29/2022
# Based on chapter 8 exercise 5 in the book. This program takes a phone number
# entered by the user which may contain alphabetic characters. The program then
# converts the number to its numeric equivalent as dialed and returns that
# number back to the user.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    heading()                                                 # Display heading.
    userNumber = getUserNum()                           # Get user input number.
    newNum = convertNum(userNumber)                            # Convert number.
    output(newNum)              # Output newly converted number with formatting.

# This function displays a heading and explains the program to the user.
def heading():
    print('Below, enter a 10 character phone number in the format '\
          '999-999-9999.')
    print('Alphabetic characters are allowed, the program '\
          'will convert the number to numeric form.')    
    print('-------------------------------------------------------'\
          '--------------------------------')    

# This function gets the users entered number.
def getUserNum():
    userNumber = input('Enter a phone number: ').lower() # Convert to lowercase.
    return userNumber

# This function converts the previously entered number to numeric form.
def convertNum(userNumber):
    splitNum = userNumber.split('-')                            # Remove dashes.
    newNum = ''                             # Create empty string to build upon.
    for i in splitNum:       # Iterates through segments of the split up number.
        for j in range(len(i)):   # Iterates through each index of each segment.
            if i[j] in 'abc':        # This structure categorizes each digit and 
                newNum += '2'        # builds onto the new string with the 
            elif i[j] in 'def':      # appropriate number.
                newNum += '3'
            elif i[j] in 'ghi':
                newNum += '4' 
            elif i[j] in 'jkl':
                newNum += '5' 
            elif i[j] in 'mno':
                newNum += '6' 
            elif i[j] in 'pqrs':
                newNum += '7' 
            elif i[j] in 'tuv':
                newNum += '8' 
            elif i[j] in 'wxyz':
                newNum += '9'
            else:              # If digit doesn't match above it is added as is.
                newNum += i[j]
    return newNum

# This function formats the converted number as requested and displays it back 
# to the user.
def output(newNum):
    finalNum = newNum[:3] + '-' + newNum[3:6] + '-' + newNum[6:]
    print(f'Here is the numeric form: {finalNum}')

# Calls main to start program.
if __name__ == '__main__':
    main()