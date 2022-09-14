# Patrick Jeffers   Final Exam   5/9/2022
# This program is for my final exam in CSC221.  After opening and creating a
# database with the provided file.  This program will use that database to 
# select and display various data and sorted tables.  As requested, all columns
# will be displayed for each menu selection.

# Import the sqlite3 module.
import sqlite3

# Valid menu options for input validation.
VALIDMENU = [1,2,3,4,5,99]

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    # Initialize loop variable.
    choice = 0
    # Call sqlite3 connect function to establish a connection to the database.
    conn = sqlite3.connect('cities.db')
    # Call cursor method to get a cursor.
    cur = conn.cursor()
    # Loop while user hasn't selected EXIT.
    while choice != 99:
        display_menu()                                   # Call to display menu.
        choice = get_menu_choice()             # Get validated user menu choice.
        if choice == 1:        # Call appropiate function based on user request.
            menu1(cur)
        elif choice == 2:
            menu2(cur)
        elif choice == 3:
            menu3(cur)
        elif choice == 4:
            menu4(cur)
        elif choice == 5:
            menu5(cur)
    # Close the connection with the database once user selects EXIT.
    conn.close()

# Function to display main menu.
def display_menu():
    print('----- Cities Menu -----')
    print('1 - Display cities sorted by population, ascending order.')
    print('2 - Display population density by city '\
          '(population divided by area).')
    print('3 - Display total population of all the cities.')
    print('4 - Display average population of all the cities.')
    print('5 - Display city with the highest population.')
    print('99 - EXIT')
    
# Function to get and validate users menu choice.
def get_menu_choice():
    choice = int(input('\nEnter your menu choice: '))         # Get user choice.
    print()
    while choice not in VALIDMENU:                                   # Validate.
        print('Please enter a valid menu choice.')
        choice = int(input('\nEnter your menu choice: '))
        print()
    return choice                                     # Return validated choice.

# Function to display output for menu option 1.
def menu1(cur):
    # Select all from cities in ascendiong order.
    cur.execute('''SELECT * FROM Cities ORDER BY Population''')
    # Fetch Results.
    results = cur.fetchall()
    # Output.
    print('Cities by population in ascending order.')
    print('----------------------------------------')
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    for row in results:
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    print()

# Function to display output for menu option 2.
def menu2(cur):
    # Select all from cities.
    cur.execute('''SELECT * FROM Cities''')
    # Fetch Results.
    results = cur.fetchall()
    # Output.
    print('All cities including population density by city.')
    print('------------------------------------------------')
    print('CityID  CityName            Country             Population   '\
          'Area       Population Density')
    print('------  --------            -------             ----------   '\
          '--------   ------------------')
    for row in results:
        # Calculate pop density of each and assign to variable for output.
        density = ((row[3])/(row[4]))               
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}'\
              f'{row[4]:11,.1f}{density:17,.2f}')
    print()   

# Function to display output for menu option 3.
def menu3(cur):
    # Select all from cities.
    cur.execute('''SELECT * FROM Cities''')
    # Fetch Results.
    results = cur.fetchall()
    # Output.
    print('All Cities plus total population of all cities at bottom.')
    print('---------------------------------------------------------')
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    for row in results:
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    # Use SUM aggregate function to select total population from all Cities.
    cur.execute('''SELECT SUM(Population) FROM Cities''')
    # Fetch Results.
    results = cur.fetchone()
    # Output.
    print('-----------------------------')
    print(f'Total Population: {results[0]:,.0f}')
    print('-----------------------------')
    print()   

# Function to display output for menu option 4.
def menu4(cur):
    # Select all from cities.
    cur.execute('''SELECT * FROM Cities''')
    # Fetch Results.
    results = cur.fetchall()
    # Output.
    print('All Cities plus average population of all cities at bottom.')
    print('-----------------------------------------------------------')
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    for row in results:
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    # Use AVG aggregate function to select average population from all Cities.
    cur.execute('''SELECT AVG(Population) FROM Cities''')
    # Fetch Results.
    results = cur.fetchone()
    # Output.
    print('---------------------------------')
    print(f'Average Population: {results[0]:,.2f}')
    print('---------------------------------')
    print()  

# Function to display output for menu option 5.
def menu5(cur):
    # Select all from cities in descending order.
    cur.execute('''SELECT * FROM Cities ORDER BY Population DESC''')
    # Fetch first result, which is the City with the highest population.
    row = cur.fetchone()
    # Output.
    print('City with the highest population.')
    print('---------------------------------')    
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    print()   

# Calls main to start program.
if __name__ == "__main__":
    main()