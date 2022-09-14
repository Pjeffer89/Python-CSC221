# Patrick Jeffers   Lab 10-9   3/3/2022
# Based on exercise 10-9 in the book. This is a simple 2 player trivia game.
# The program takes turns asking each player 5 trivia questions.  After all 10
# questions are answered the points are displayed and a winner is declared.

# This imports the question module for the program to use.
import question

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
# Creating 10 questions.
    question1 = question.Question('What does a wire fox terrier like to '\
                                  'chase more than anything else?',\
                                  'Duck.',\
                                  'Rabbit.',\
                                  'Squirrel.',\
                                  'Their tail.', \
                                  3)
    question2 = question.Question('What is the unit of measurement for '\
                                  'resistance when referring to an electrical '\
                                  'circuit?',\
                                  'Hertz.',\
                                  'Amperage.',\
                                  'Scoville.',\
                                  'Ohms.',\
                                  4)
    question3 = question.Question('What does the yellow flag signify in the '\
                                  'context of auto racing?',\
                                  'Stop.',\
                                  'Caution.',\
                                  'Restart.',\
                                  'Pit.',\
                                  2)
    question4 = question.Question('A device used to recover otherwise wasted '\
                                  'exhaust energy to turn a compressor and '\
                                  'force air into the intake of an engine '\
                                  'thus increasing power and volumetric '\
                                  'efficiency.',\
                                  'Turbocharger.',\
                                  'Supercharger.',\
                                  'Catalytic Converter.',\
                                  'Nitrous System.',\
                                  1)
    question5 = question.Question('Who is the official 2021 Formula One World '\
                                  'Champion?',\
                                  'Sergio Perez.',\
                                  'Lewis Hamilton.',\
                                  'Lando Norris.',\
                                  'Max Verstappen.',\
                                  4)
    question6 = question.Question('What is cynophobia the fear of?',\
                                  'Cinnamon.',\
                                  'Fire.',\
                                  'Dogs.',\
                                  'Tornadoes.',\
                                  3)
    question7 = question.Question('What is the national animal of Scotland?',\
                                  'Raven.',\
                                  'Unicorn.',\
                                  'Highland Cow.',\
                                  'Sheep.',\
                                  2)
    question8 = question.Question('What is the hottest planet in our solar'\
                                  'system?',\
                                  'Venus.',\
                                  'Mars.',\
                                  'Jupiter.',\
                                  'Saturn.',\
                                  1)
    question9 = question.Question('What is the name of the Italian style of '\
                                  'coffee known for extracting concentrated '\
                                  'coffee with high pressure?',\
                                  'Affogato.',\
                                  'Mocha.',\
                                  'Prestissimo.',\
                                  'Espresso.',\
                                  4)
    question10 = question.Question('What is the fear of long words?',\
                                   'Ablutophobia.',\
                                   'Globophobia.',\
                                   'Hippopotomonstrosesquippedaliophobia.',\
                                   'Chirophobia.',\
                                   3)

# Create list with all 10 question objects.    
    triviaQuestions = [question1, question2, question3, question4, question5, \
                       question6, question7, question8, question9, question10]
      
# Create variables to store player scores.
    player1Score = 0
    player2Score = 0
    
# Heading and instructions.    
    print('----------------------------------------------------------')
    print('Player 1, answer your 5 trivia questions below, good luck!')
    print('----------------------------------------------------------')
    for i in range(5):                     # Iterates through first 5 questions.
        print()
        eachQuestion = triviaQuestions[i]
        print(eachQuestion)                             # Display each question.
        print()
        playerAnswer = int(input('Enter your answer here: ')) # Get user answer.
        if playerAnswer == eachQuestion.get__correctAnswer():
            player1Score += 1     # Increment score if player answer is correct.

# Heading and instructions.    
    print('\n' + '----------------------------------------------------------')   
    print('Player 2, answer your 5 trivia questions below, good luck!')
    print('----------------------------------------------------------')
    for i in range(5,10):                 # Iterates through second 5 questions.
        print()
        eachQuestion = triviaQuestions[i]
        print(eachQuestion)                             # Display each question.
        print()
        playerAnswer = int(input('Enter your answer here: ')) # Get user answer.
        if playerAnswer == eachQuestion.get__correctAnswer():
            player2Score += 1     # Increment score if player answer is correct.
    
# Display total points for each player.  Then determine and display who is the 
# winner or if the game was a tie.
    print('\n' + '-------------------------------------------')
    print(f'Player 1 scored {player1Score} points.')
    print(f'Player 2 scored {player2Score} points.')
    if player1Score > player2Score:
        print('Player 1 wins!')
    elif player2Score > player1Score:
        print('Player 2 wins!')
    else:
        print('It was a tie score.  Neither player wins.')
    print('-------------------------------------------')

# Calls main to start program.
if __name__ == "__main__":
    main()