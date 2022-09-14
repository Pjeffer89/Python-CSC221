# Patrick Jeffers   Final Exam   5/9/2022

import sqlite3

VALIDMENU = [1,2,3,4,5,99]

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    choice = 0
    while choice != 99:
        display_menu()
        choice = get_menu_choice()
        if choice == 1:
            menu1()
        elif choice == 2:
            menu2()
        elif choice == 3:
            menu3()
        elif choice == 4:
            menu4()
        elif choice == 5:
            menu5()

def display_menu():
    print('----- Cities Menu -----')
    print('1 - Display cities sorted by population, ascending order.')
    print('2 - Display population density by city '\
          '(population divided by area).')
    print('3 - Display total population of all the cities.')
    print('4 - Display average population of all the cities.')
    print('5 - Display city with the highest population.')
    print('99 - EXIT')
    
def get_menu_choice():
    choice = int(input('\nEnter your menu choice: '))
    print()
    while choice not in VALIDMENU:
        print('Please enter a valid menu choice.')
        choice = int(input('\nEnter your menu choice: '))    
    return choice

def menu1():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities ORDER BY Population''')
    results = cur.fetchall()
    print('Cities by population in ascending order.')
    print('----------------------------------------')
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    for row in results:
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    print()
    conn.close()

def menu2():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities''')
    results = cur.fetchall()
    print('All cities including population denstiy by city.')
    print('------------------------------------------------')
    print('CityID  CityName            Country             Population   '\
          'Area       Population Density')
    print('------  --------            -------             ----------   '\
          '--------   ------------------')
    for row in results:
        density = ((row[3])/(row[4]))
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}'\
              f'{row[4]:11,.1f}{density:17,.2f}')
    print()
    conn.close()    

def menu3():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities''')
    results = cur.fetchall()
    print('All Cities plus total population of all cities at bottom.')
    print('---------------------------------------------------------')
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    for row in results:
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    cur.execute('''SELECT SUM(Population) FROM Cities''')
    results = cur.fetchone()
    print('-----------------------------')
    print(f'Total Population: {results[0]:,.0f}')
    print('-----------------------------')
    print()
    conn.close()    

def menu4():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities''')
    results = cur.fetchall()
    print('All Cities plus average population of all cities at bottom.')
    print('-----------------------------------------------------------')
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    for row in results:
        print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    cur.execute('''SELECT AVG(Population) FROM Cities''')
    results = cur.fetchone()
    print('---------------------------------')
    print(f'Average Population: {results[0]:,.2f}')
    print('---------------------------------')
    print()
    conn.close()    

def menu5():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Cities ORDER BY Population DESC''')
    row = cur.fetchone()
    print('City with the highest population.')
    print('---------------------------------')    
    print('CityID  CityName            Country             Population   Area')
    print('------  --------            -------             ----------   ----'\
          '----')
    print(f'{row[0]:<8}{row[1]:20}{row[2]:20}{row[3]:,.0f}{row[4]:11,.1f}')
    print()
    conn.close()    

# Calls main to start program.
if __name__ == "__main__":
    main()
