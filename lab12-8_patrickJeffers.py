# Patrick Jeffers   Lab 12-8   3/24/2022
# Based on chapter 12 exercise 8 from the book. This program is a demonstration
# of Ackermann's function, a recursive mathematical algorithm used to test how 
# well a system optimizes its performance of recursion.

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    print("Solving Ackermann's function.")                            # Heading.
    print('-----------------------------')
    m = int(input('Enter a value for m: '))           # Get user values for m/n.
    n = int(input('Enter a value for n: '))
    
    output = ackermann(m,n)      # Call Ackermann's function using user numbers.
    
    print(output)                                              # Display result.
    
# Ackermann's function.
def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1, ackermann(m,n-1))

# Calls main to start program.
if __name__ == "__main__":
    main()