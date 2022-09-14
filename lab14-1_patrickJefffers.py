# Patrick Jeffers   Lab 14-1   5/2/2022

import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    choice = 0
    while choice != 0:
        display_menu()
        choice = get_menu_choice()
        
        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()
            
def display_menu():
    print('\n----- Phonebook Menu -----')
    print('1. Add a contact.')
    print('2. Lookup a cantact.')
    print('3. Edit a contact.')
    print('4. Delete a contact.')
    print('5. Exit.')
    
def get_menu_choice():
    choice = int(input('Enter your choice: '))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        choice = int(input('Enter your choice: '))
    return choice

def create():
    print('Add a contact.')
    name = input('Enter name: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    phoneNumber = input('Enter Phone Number: ')
    insert_row(name, city, state, phoneNumber)
    
def read():
    name = input('Enter a name to search for: ')
    num_found = display_contact(name)
    print(f'{num_found} row(s) found.')
    
def update():
    pass

def delete():
    pass

# Calls main to start program.
if __name__ == "__main__":
    main()