# Patrick Jeffers   Lab 9-9   2/20/2022
# Based on chapter 9 exercise 9 in the book.  This program is a modified version
# of card_dealer.py.  It is a blackjack game that simulates a game between two
# players.  The program deals to each player until one hand is greater than 21.
# The winner is then determined depending on if either or both exceed 21.  The
# program repeats until all cards have been dealt from a standard shuffled deck.

# Import random to use for shuffling the deck.
import random

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    # Create a deck of cards.
    deck = create_deck()
    
    print('Blackjack Simulation')                                     # Heading.
    print('--------------------'+'\n')
    
    # Deal the cards.
    deal_cards(deck)

# The create_deck function returns a dictionary
# representing a shuffled deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    DECK = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    shuffledDeck = {}                                 # For new version of deck.
    deckList = list(DECK)                             # Create list and shuffle.
    random.shuffle(deckList)
    for i in deckList:                         # Back into dictionary, shuffled.
        shuffledDeck[i] = DECK[i]

    # Return the deck.
    return shuffledDeck

# The deal_cards function deals cards until the deck is empty.  It is 
# effectively a virtual blackjack dealer. The function deals the cards, and 
# displays the results of each game.
def deal_cards(deck):
    while deck != {}:                           # Continues until deck is empty.
        try:
            playerOneScore = 0   # Initialize an accumulator for the hand value.
            playerTwoScore = 0   # Initialize an accumulator for the hand value.
            winner = ''
            
            print(f'{"Player 1":20}{"Player 2":20}')        # Each game heading.
            print(f'{"--------":20}{"--------":20}')    
            
            while playerOneScore <= 21 and playerTwoScore <= 21: # Deal to each.
                playerOneCard, playerOneValue = deck.popitem()
                playerTwoCard, playerTwoValue = deck.popitem()
                
                if 'Ace' in playerOneCard:    # Handles ace card logic depending
                    if playerOneScore > 10:                # each players score.
                        playerOneScore += 1
                    else: playerOneScore += 11
                else: playerOneScore += playerOneValue
                
                if 'Ace' in playerTwoCard:
                    if playerTwoScore > 10:
                        playerTwoScore += 1
                    else: playerTwoScore += 11
                else: playerTwoScore += playerTwoValue
                
                # Display each card and then final total.
                print(f'{playerOneCard:20}{playerTwoCard:20}')
            print(f'{"Total":20}{"Total":20}')
            print(f'{"-----":20}{"-----":20}')
            print(f'{playerOneScore:<20}{playerTwoScore}')
            
            # Determines and displays the winner of each game.
            if playerOneScore > 21 and playerTwoScore > 21:
                winner = 'Neither player won. Both players busted.'
            elif playerOneScore > 21:
                winner = 'Player 2 wins!'
            else:
                winner = 'Player 1 wins!'
            
            print('---------------------------------------')
            print(winner)
            print('---------------------------------------')
            print()
        except KeyError:        # Handles KeyErrors when deck runs out of cards.
            print('--------------------------')
            print('Game Incomplete.')
            print('The deck ran out of cards.')
            print('--------------------------')

# Call the main function.
if __name__ == '__main__':
    main()