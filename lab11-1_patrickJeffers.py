# Patrick Jeffers   Lab 11-1   3/15/2022
# Based on chapter 11-1 in the book. This program demonstrates super and sub 
# class concepts. The program uses classes stored in another module.  This 
# program allows the user to create an object of the ProductionWorker class and
# then retrieve the information via accessor methods for display again.

# This imports the employee module for the program to use.
import employee

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    print('Please enter information for a production worker below.')  # Heading.
    print('-------------------------------------------------------')
    employeeName = input('Enter the employees name: ')     # Get info from user.
    employeeNumber = input('Enter the employees number: ')
    print('Current Shifts')                                              # Menu.
    print('\t1 - Day Shift')
    print('\t2 - Night Shift')
    shiftNumber = int(input('Enter the employees shift number: '))
    payRate = float(input('Enter the employees hourly pay rate: '))
    
# Create object with user entered information stored in variables.    
    newProductionWorker = employee.ProductionWorker(employeeName,employeeNumber,
                                                    shiftNumber,payRate)
# Display.    
    print()
    print('This is the employees information entered above.')         # Heading.
    print('-----------------------------------------------')
    print(f'Name: {newProductionWorker.get_employeeName()}')    # Using accessor
    print(f'Number: {newProductionWorker.get_employeeNumber()}')   # methods for
    print(f'Shift Number: {newProductionWorker.get_shiftNumber()}')   # display.
    print(f'Hourly Pay Rate: ${newProductionWorker.get_payRate():,.2f}')
    
# Calls main to start program.
if __name__ == "__main__":
    main()