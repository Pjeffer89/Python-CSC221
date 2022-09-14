# Patrick Jeffers   Lab 11-3   3/16/2022
# Based on chapter 11-3 in the book. This program demonstrates super and sub 
# class concepts. The program uses classes stored in another module.  This 
# simple program allows the user to create an instance of the Customer class and
# then retrieve the information via accessor methods for display again.

# This imports the person module for the program to use.
import person

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    print('Please enter information for a Customer below.')           # Heading.
    print('----------------------------------------------')
    customerName = input('Enter the customers name: ')     # Get info from user.
    customerAddress = input('Enter the customers address: ')
    customerPhone = input('Enter the customers telephone number: ')
    customerNumber = input('Enter the customers ID number: ')
    mailList = input('Does the customer wish to join the mailing list (Y/N): ')
    
    if mailList.lower() == 'y':      # Create boolean value based on user entry.
        mailingList = True
    else: mailingList = False

# Create object with user entered information stored in variables.   
    newCustomer = person.Customer(customerName, customerAddress, customerPhone,
                                  customerNumber, mailingList)
    
# Display.     
    print()
    print('This is the Customers information entered above.')         # Heading.
    print('------------------------------------------------')    
    print(f'Name: {newCustomer.get_name()}')            # Using accessor methods
    print(f'Address: {newCustomer.get_address()}')                # for display.
    print(f'Phone Number: {newCustomer.get_phoneNumber()}')
    print(f'Customer ID Number: {newCustomer.get_customerNumber()}')
    print(f'Customer joined mailing list: {newCustomer.get_mailingList()}')
    
# Calls main to start program.
if __name__ == "__main__":
    main()