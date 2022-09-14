# Patrick Jeffers   Lab 12-2   3/24/2022
# Based on chapter 12 exercise 2 in the book. This program is a simple 
# multiplication program to demonstrate a recursive function.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    print('Multiplication program.')                                  # Heading.
    print('Please enter 2 positive numbers to multiply.')
    print('--------------------------------------------')
    x = int(input('Number 1: '))                 # Get user numbers to multiply.
    y = int(input('Number 2: '))
    
    result = multiply(x,y)   # Call the recursive function passing user numbers.
    
    print(f'Result: {result}')                             # Display the result.
    
# Recursive multiplication function.
def multiply(x,y):
    if x == 0 or y == 0:             # Returns 0 if a number is multiplied by 0.
        return 0
    else:
        return x + multiply(x,y-1)
            
# Calls main to start program.
if __name__ == "__main__":
    main()