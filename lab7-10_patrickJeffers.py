# Patrick Jeffers   Lab 7-10   1/17/2022
# Based on chapter 7 exercise 10 in the book. This program utilizes a file of
# all World Series winners from 1903-2020. The program allows the user to enter
# a team name and will return the number of times that team has won from that 
# time period in total.  The program continues to take team names until stopped
# by the user.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    count = 0                             # Accumulator to count number of wins.
    cont = True                                         # Used for loop control.
    infile = open('WorldSeriesWinners.txt', 'r') # Open and get content of file.
    allWinners = infile.readlines()
    infile.close()

# Strips newline character from newly created list.    
    for i in range(len(allWinners)):
        allWinners[i] = allWinners[i].rstrip('\n')

# Heading for program.    
    print('This program will tell you how many times a team has won'\
          ' the World Series from 1903-2020.')
    print('--------------------------------------------------------'\
          '---------------------------------')
    while cont == True:                                     # Main control loop.
        inputTeam = input('Enter a team name or "stop" to end: ')
        if inputTeam == 'stop':    # Gets team name from user or allows to stop.
            cont = False
            break
    
# This process iterates through the list of all team names and each time it
# matches the user input it increases the count by 1.
        for i in allWinners:
            if i == inputTeam:
                count += 1

# Output results back to user, then reset counter for next entry.        
        print(f'Your team won {count} times.')
        print()
        count = 0

# Calls main to start program.   
main()