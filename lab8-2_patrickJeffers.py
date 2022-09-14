# Patrick Jeffers   Lab 8-2   1/26/2022
# This program asks the user to input a series of single-digit numbers with no 
# spaces or anything separating the numbers.  The program then processes this 
# so that it will return to the user the sum of the single sigit numbers 
# entered.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    stringAsList = []            # Create list to store numbers from user input.
    
# Heading and explanation for the user.
    print('Below, enter a series of single-digit numbers with nothing'\
          ' separating the numbers.  The program will find the sum of the'\
          ' numbers.')
    print('----------------------------------------------------------'\
          '--------------------------------------------------------------'\
          '---------')
    string = input('Enter a series of numbers: ')           # Get number string.
    for ch in string:                         # Puts each character into a list.
        stringAsList.append(ch)

    for i in range(len(stringAsList)):              # Converts list to integers.
        stringAsList[i] = int(stringAsList[i])

    total = sum(stringAsList)                                # Gets sum of list.

    print(f'The sum is {total}.')                         # Display the results.

# Calls main to start program.
if __name__ == '__main__':
    main()