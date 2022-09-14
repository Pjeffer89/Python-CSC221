# Patrick Jeffers   Lab 9-5   2/18/2022
# Based on chapter 9 exercise 5 from the book.  This program opens a text file,
# read the contents of the file, then creates a dictionary.  The dictionary will
# include each word from the file as the keys with the keys value being the 
# number of times that words appears in the file.

# This function is passed the contents of the file and processes the words to 
# remove punctuation and capitalization.  Then the function splits the contents 
# before creating a set with all unique words.
def getUniqueWords(fileContents):
    fileContents = fileContents.lower()                 # Remove capitalization.
    fileContents = fileContents.replace('.','')                # Remove periods.
    fileContents = fileContents.replace(',','')                 # Remove commas.
    fileContents = fileContents.replace("'s","")                  # Remove "'s".
    wordList = fileContents.split()            # Get full list of words in file.
    wordSet = set(wordList)        # Use set to get unique set of words in file.
    return wordList, wordSet

# This function is passed the unique set of words and returns a dictionary of 
# the words with values set to 0.
def createUniqueWordDictionary(wordSet):
    uniqueWordDictionary = {}                  # Empty dictionary to build upon.
    for i in wordSet:                            # Iterates through set building 
        uniqueWordDictionary[i] = 0                # dictionary with values = 0.
    return uniqueWordDictionary

# This function is passed the full list of words and the dictionary of unique
# words. The function then iterates through the list and each time the word is
# encountered it increments the words value in the dictionary by 1. It then 
# returns the counted version of the dictionary for display later.
def countWords(wordList, uniqueWordDictionary):
    for i in wordList:
        uniqueWordDictionary[i] += 1
    return uniqueWordDictionary

# This function is passed the final counted dictionary and is used to display
# the processed information back to the user.  After formatting a heading, the
# function uses a loop to pull and remove each key and value from the dictionary
# for display and deletion until the dictionary is empty.
def displayCount(countedWordsDictionary):
    print()
    print(f'{"Word":25}{"Frequency"}')
    print(f'{"----":25}{"---------"}')
    while (len(countedWordsDictionary) > 0):
        keyValue = countedWordsDictionary.popitem()
        print(f'{keyValue[0]:25}{keyValue[1]}')
        
# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    inFile = open('text95.txt', 'r')                                # Open file.
    fileContents = inFile.read()                         # Get contents of file.
    inFile.close()                                                 # Close file.
    wordList, wordSet = getUniqueWords(fileContents)                  # Process.
    uniqueWordDictionary = createUniqueWordDictionary(wordSet)
    countedWordsDictionary = countWords(wordList, uniqueWordDictionary)
    displayCount(countedWordsDictionary)                      # Display results.
    
# Calls main to start program.
if __name__ == '__main__':
    main()