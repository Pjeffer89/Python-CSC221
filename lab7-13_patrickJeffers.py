# Patrick Jeffers   Lab 7-13   1/23/2022
# This program simulates a magic 8 ball.  The program uses a list of responses 
# from a file for answers.  The user enters a "yes or no" question and the 
# program then generates a random answer from that list of answers.  The program
# will continue to take questions until told to stop by the user.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    import random                            # For getting random numbers later.
    numOfResponses = 15
    cont = True                                         # Used for loop control.
    infile = open('8_ball_responses.txt', 'r')   # Open and get content of file.
    allResponses = infile.readlines()
    infile.close()

# Strips newline character from newly created list.    
    for i in range(len(allResponses)):
        allResponses[i] = allResponses[i].rstrip('\n')
        
# Heading for program. Explains the program to the user.  
    print('Please enter a "yes or no" question for the magic 8 ball '\
          'program.  Or enter "stop" to end.')
    print('---------------------------------------------------------'\
          '---------------------------------')
    while cont == True:                                     # Main control loop.
        userQuestion = input('Enter your question: ')
        if userQuestion == 'stop':  # Gets question from user or allows to stop.
            cont = False
            break

# This will generate a random number up to the number of responses in the file.
# Then use that number to pick an index for a response from the response list 
# and display it.
        responseNum = random.randrange(0,numOfResponses)
        print(allResponses[responseNum] + '\n')
       
# Calls main to start program.
if __name__ == '__main__':
    main()