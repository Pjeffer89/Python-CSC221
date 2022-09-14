# Patrick Jeffers, 14 April 2022 PJeffers_project2.py
# This program serves as Project 2 for CSC221.  This is a program to take in a 
# CSV file of Covid-19 data then sort and display charts of data based on user
# choices of what and how they would like to view the data.

# Currently the only main menu option fully built out to completion is option 3.

# Function to manage menu option 3 and plot based on user requests.
def plotMenuItem3(casesOrDeaths3, year3, lineOrBar3):
    import pandas as pd                                         # Import pandas.
    import matplotlib.pyplot as plt                         # Import matplotlib.
    df = pd.read_csv('covid19data.csv')                # Open file to dataframe.
    df['submissionDate'] = pd.to_datetime(df['submissionDate'])  # To date type.
    df.set_index('submissionDate', inplace = True)          # Set date as index.
    df.sort_values('submissionDate', inplace = True)                     # Sort.
    
    # Setup charts if user selects 2020.
    if year3 == 2020:
        plt.xlabel('Year 2020')                                   # Set X label.
        # Setup charts based on cases or deaths.
        if casesOrDeaths3 == 1:
            plt.title('New Cases')                                  # Set title.
            plt.ylabel('New cases x 1,000,000')                   # Set Y label.
            # Modified new specific dataframe for chart output.
            ndf = df.loc['2020-01-01':'2020-12-31'].resample('M').sum()/1000000
            y = ndf['newCases']                                    # Set Y axis.
        else:
            plt.title('New Deaths')                                 # Set title.
            plt.ylabel('New deaths x 10,000')                     # Set Y label.
            # Modified new specific dataframe for chart output.
            ndf = df.loc['2020-01-01':'2020-12-31'].resample('M').sum()/10000
            y = ndf['newDeaths']                                   # Set Y axis.
    # Setup charts if user selects 2021.
    elif year3 == 2021:
        plt.xlabel('Year 2021')                                   # Set X label.
        # Setup charts based on cases or deaths.
        if casesOrDeaths3 == 1:
            plt.title('New Cases')                                  # Set title.
            plt.ylabel('New cases x 1,000,000')                   # Set Y label.
            # Modified new specific dataframe for chart output.
            ndf = df.loc['2021-01-01':'2021-12-31'].resample('M').sum()/1000000
            y = ndf['newCases']                                    # Set Y axis.
        else:
            plt.title('New Deaths')                                 # Set title.
            plt.ylabel('New deaths x 10,000')                     # Set Y label.
            # Modified new specific dataframe for chart output.
            ndf = df.loc['2021-01-01':'2021-12-31'].resample('M').sum()/10000
            y = ndf['newDeaths']                                   # Set Y axis.
    # Setup charts if user selects 2022.
    elif year3 == 2022:
        plt.xlabel('Year 2022')                                   # Set X label.
        # Setup charts based on cases or deaths.
        if casesOrDeaths3 == 1:
            plt.title('New Cases')                                  # Set title.
            plt.ylabel('New cases x 1,000,000')                   # Set Y label.
            # Modified new specific dataframe for chart output.
            ndf = df.loc['2022-01-01':'2022-12-31'].resample('M').sum()/1000000
            y = ndf['newCases']                                    # Set Y axis.
        else:
            plt.title('New Deaths')                                 # Set title.
            plt.ylabel('New deaths x 10,000')                     # Set Y label.
            # Modified new specific dataframe for chart output.
            ndf = df.loc['2022-01-01':'2022-12-31'].resample('M').sum()/10000
            y = ndf['newDeaths']                                   # Set Y axis.
    x = ndf.index                                                  # Set X axis.
     
    # Plot output based on user choice of line or bar chart.
    if lineOrBar3 == 1:                                         # If line chart.
        plt.plot(x,y)                                            # Plot X and Y.
        plt.grid(True)                                            # Enable grid.
        plt.ylim(ymin = 0, ymax = 22)                  # Set Y axis min and max.
        plt.show()                                                    # Display.
    else:                                                        # If bar chart.
        plt.bar(x,y,15)                           # Plot X and Y. Set bar width.
        plt.ylim(ymin = 0, ymax = 22)                  # Set Y axis min and max.
        plt.show()                                                    # Display.
        
# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    # Program constants.  Lists of possible entries for user input validation.
    # All possible states.
    ALLSTATES = ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI',
                 'IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN',
                 'MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH',
                 'OK','OR','PA','PR','RI','SC','SD','TN','TX','UT','VA','VT', 
                 'WA','WI','WV','WY']
    # All possible months.
    ALLMONTHS = ['01','02','03','04','05','06','07','08','09','10','11','12']
    # All possible years.
    ALLYEARS = [2020,2021,2022]
    # Only possible main menu choices.
    MAINMENUOPTIONS = [1,2,3,4,5]
    # Only possible sub-menu choices.
    SUBMENUOPTIONS = [1,2]

    # Setup program to loop until exit is chosen by the user.
    mainMenuChoice = 1
    # Heading for the program, followed by menu.
    print('Welcome to the Covid 19 data plotting program.')
    print('-------------------------------------------------')    
    while mainMenuChoice != 5:
        print('Please choose which data you would like to view.')
        print('-------------------------------------------------')
        print('\t1: Daily cases or deaths.')
        print('\t2: Monthly chart for one state for a year.')
        print('\t3: Totals for all states by year.')
        print('\t4: Monthly data for multiple years.')
        print('\t5: Exit.')
        # Get and validate the users main menu choice.
        mainMenuChoice = int(input('Choose from the menu above: '))
        while mainMenuChoice not in MAINMENUOPTIONS:
            print('Please enter a valid menu option.')
            mainMenuChoice = int(input('Choose from the menu above: '))
    
        # If the user chooses option 1.
        if mainMenuChoice == 1:
            print('-------------------------------------------------')
            # Get and validate a state from user.
            state1 = input('Enter a 2 letter state abbreviation '\
                           'such as "NC": ').upper()
            while state1 not in ALLSTATES:
                print('Please enter a valid state abbreviation.')
                state1 = input('Enter a 2 letter state abbreviation '\
                               'such as "NC": ').upper()
            # Get and validate user choice of cases or deaths.
            casesOrDeaths1 = int(input('Enter "1" for cases or "2" '\
                                       'for deaths: '))
            while casesOrDeaths1 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                casesOrDeaths1 = int(input('Enter "1" for cases or "2" '\
                                           'for deaths: '))
            # Allow user to choose between a single month or range of months.
            monthOrRange1 = int(input('Enter "1" for a single month or "2" '\
                                      'for a range of months: '))
            while monthOrRange1 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                monthOrRange1 = int(input('Enter "1" for a single month or '\
                                          '"2" for a range of months: '))            
            # If a single month is chosen, get and validate the month.
            if monthOrRange1 == 1:
                month1 = (input('Enter the 2 digit month number: '))
                while month1 not in ALLMONTHS:
                    print('Please enter a vaid month number, "01-12".')
                    month1 = (input('Enter the 2 digit month number: '))
            # If a range of months is chosen, get and validate the starting and
            # ending months.
            elif monthOrRange1 == 2:
                startMonth1 = (input('Enter the 2 digit month number of '\
                                        'the starting month: '))
                while startMonth1 not in ALLMONTHS:
                    print('Please enter a vaid month number, "01-12".')
                    startMonth1 = (input('Enter the 2 digit month number '\
                                            'of the starting month: '))            
                endMonth1 = (input('Enter the 2 digit month number of the '\
                                      'ending month: ')) 
                while endMonth1 not in ALLMONTHS:
                    print('Please enter a vaid month number, "01-12".')
                    endMonth1 = (input('Enter the 2 digit month number '\
                                          'of the ending month: '))            
            # Get and validate user choice of line or bar chart.
            lineOrBar1 = int(input('Enter "1" for a line chart or "2" for '\
                                       'a bar chart: '))
            while lineOrBar1 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                lineOrBar1 = int(input('Enter "1" for a line chart or "2" '\
                                           'for a bar chart: '))        

        # If the user chooses option 2.
        elif mainMenuChoice == 2:
            print('-------------------------------------------------')
            # Get and validate a state from user.
            state2 = input('Enter a 2 letter state abbreviation such '\
                           'as "NC": ').upper()
            while state2 not in ALLSTATES:
                print('Please enter a valid state abbreviation.')
                state2 = input('Enter a 2 letter state abbreviation '\
                               'such as "NC": ').upper()
            # Get and validate a year from user.
            year2 = int(input('Enter the year, 2020, 2021, or 2022: '))
            while year2 not in ALLYEARS:
                print('Please enter a valid year.')
                year2 = int(input('Enter the year, 2020, 2021, or 2022: '))
            # Get and validate user choice of cases or deaths.
            casesOrDeaths2 = int(input('Enter "1" for cases or "2" '\
                                       'for deaths: '))
            while casesOrDeaths2 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                casesOrDeaths2 = int(input('Enter "1" for cases or "2" '\
                                           'for deaths: '))
            # Get and validate user choice of line or bar chart.
            lineOrBar2 = int(input('Enter "1" for a line chart or "2" for a'\
                                   ' bar chart: '))
            while lineOrBar2 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                lineOrBar2 = int(input('Enter "1" for a line chart or "2" for '\
                                       'a bar chart: '))            

        # If the user chooses option 3.
        elif mainMenuChoice == 3:
            print('-------------------------------------------------')
            # Get and validate user choice of cases or deaths.
            casesOrDeaths3 = int(input('Enter "1" for cases or "2" '\
                                       'for deaths: '))
            while casesOrDeaths3 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                casesOrDeaths3 = int(input('Enter "1" for cases or "2" '\
                                           'for deaths: '))
            # Get and validate a year from user.
            year3 = int(input('Enter the year, 2020, 2021, or 2022: '))
            while year3 not in ALLYEARS:
                print('Please enter a valid year.')
                year3 = int(input('Enter the year, 2020, 2021, or 2022: '))
            # Get and validate user choice of line or bar chart.
            lineOrBar3 = int(input('Enter "1" for a line chart or "2" for a'\
                                   ' bar chart: '))
            while lineOrBar3 not in SUBMENUOPTIONS:
                print('Please enter a valid menu option.')
                lineOrBar3 = int(input('Enter "1" for a line chart or "2" for '\
                                       'a bar chart: '))
            # Call function to create output plotting.
            plotMenuItem3(casesOrDeaths3, year3, lineOrBar3)
   
        # If the user chooses option 4.
        elif mainMenuChoice == 4:
            print('-------------------------------------------------')
            # No idea what I am supposed to ask for here yet.
            # What is "Monthly data for multiple years"?
        
        print()
            
# Calls main to start program.
if __name__ == "__main__":
    main()