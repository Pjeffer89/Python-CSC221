# Patrick Jeffers   Lab 6-9   1/13/2022
# This program reads a list of integers from a given file. The program then 
# calculates the total and the average of the numbers in the file and displays 
# the numbers from the file as well as the calculated total and average.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    try:                                         # Exception handling structure.
        readFile("numbers.txt")
    except IOError:         # Exception when there is an issue opening the file.
        print("There was an error when attempting to read this file.")
    except ValueError:                   # Exception for non numeric data found.
        print()
        print("Non numeric value found.")
    
# This function accesses the file, processes file and results and displays back
# to the user when called by main.
def readFile(file):
    theFile = open(file, "r")                                      # Opens file.
    sumOfNums = 0                  # Declaring and initializing local variables.
    numberOfNums = 0
    avgOfNums = 0
    listOfNums = []
    print("Numbers")                         # Prints heading for output.
    print("-------")
    line = theFile.readline()                # Reads the first line in the file.
    while line != '':           # Used to read each line that contains a number.
        eachNum = int(line) #Converts to int, and assigns the line to a variable
        listOfNums.append(eachNum)    # Creates list and adds each number to it.
        sumOfNums += eachNum         # Accumulator to total all numbers in file.
        numberOfNums += 1              # Counts the quantity of numbers in file.
        avgOfNums = avgNums(sumOfNums,numberOfNums)   # Call to get avg of nums.
        print(eachNum)                # Prints each number as the loop iterates.
        line = theFile.readline()    # Reads the next line for the while loop to 
                                     # interpret.
    print()     # Below outputs the total and average below the list of numbers.
    print('Total: ' + f'{sumOfNums:,.0f}')
    print('Average: ' + f'{avgOfNums:,.2f}')


# This function takes a total and quantity then calculates and returns the
# average.
def avgNums(total,numOfNumbers):
    avgOfNums = (total / numOfNumbers)
    return avgOfNums

# Calls main to start program.
if __name__ == '__main__':
    main()