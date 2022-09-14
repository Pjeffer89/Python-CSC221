# Patrick Jeffers   Lab 8-14   1/30/2022
# Based on chapter 8 exercise 14 in the book.  This program reads from a file of
# gas prices from 1993 to 2013 and returns various calculations based on the 
# contents. Specifically, it returns the average price per year, the average 
# price per month, and the lowest and highest prices for each year.

# Constants.
STARTYEAR = 1993
ENDYEAR = 2013
STARTMONTH = 1
ENDMONTH = 12
MONTHS = ['January','February','March','April','May','June','July','August',
          'September','October','November','December']

# This function takes input from the gasList and splits/returns only the price
# portion.
def getPrice(listItem):
    items = listItem.split(':')
    return float(items[1])

# This function takes input from the gasList and splits/returns only the year 
# portion.
def getYear(listItem):
    items = listItem.split(':')
    dateItems = items[0].split('-')
    return int(dateItems[2])     

# This function takes input from the gasList and splits/returns only the month 
# portion.
def getMonth(listItems):
    items = listItems.split(':')
    dateItems = items[0].split('-')
    return int(dateItems[0])  

# This function returns the average price per year from the gasFile.
def getYearlyAvg(gasList, year):
    total = 0
    count = 0                               # Initialze accumulator and counter.

# Iterates through the gasList, gets the sum of all the prices for specified 
# year in total and increments counter.
    for each in gasList:
        if getYear(each) == year:
            total += getPrice(each)
            count += 1
    average = total / count                # Calculates and returns the average.
    return average

# This function is to display the average price per year.
def yearlyAvgOutput(gasList):
    print('Average price per year.')
    print('-----------------------')
    for year in range(STARTYEAR, ENDYEAR + 1):  
        print(f'The average price in {year} was $' 
              f'{getYearlyAvg(gasList, year):.2f}.') 
    print('------------------------------------')

# This function returns the average price per month from the gasFile.
def getMonthlyAvg(gasList, monthNum):
    total = 0
    count = 0                               # Initialze accumulator and counter.
    
# Iterates through the gasList, gets the sum of all the prices for specified 
# month in total and increments counter.
    for each in gasList:
        if getMonth(each) == monthNum:
            total += getPrice(each)
            count += 1
    average = total / count                # Calculates and returns the average.
    return average    
    
# This function is to display the average price per month.
def monthlyAvgOutput(gasList):
    print('Average price per month.')
    print('------------------------')
    for monthNum in range(STARTMONTH, ENDMONTH + 1):  
        print(f'The average price in {MONTHS[monthNum-1]} was $' 
              f'{getMonthlyAvg(gasList, monthNum):.2f}.') 
    print('----------------------------------------')

# This function returns the highest price per year from the gasFile.
def getHighestPerYear(gasList, year):
    priceList = []
    for each in gasList:
        if getYear(each) == year:
            priceList.append(getPrice(each))
    maxPrice = max(priceList)
    return maxPrice

# This function is to display the highest price per year.
def highestPerYearOutput(gasList):
    print('The highest price per year.')
    print('---------------------------')
    for year in range(STARTYEAR, ENDYEAR + 1):  
        print(f'The highest price in {year} was $' 
              f'{getHighestPerYear(gasList, year):.2f}.') 
    print('------------------------------------')
    
# This function returns the lowest price per year from the gasFile.
def getLowestPerYear(gasList, year):
    priceList = []
    for each in gasList:
        if getYear(each) == year:
            priceList.append(getPrice(each))
    minPrice = min(priceList)
    return minPrice

# This function is to display the lowest price per year.
def lowestPerYearOutput(gasList):
    print('The lowest price per year.')
    print('--------------------------')
    for year in range(STARTYEAR, ENDYEAR + 1):  
        print(f'The lowest price in {year} was $' 
              f'{getLowestPerYear(gasList, year):.2f}.') 
    print('-----------------------------------')
    
# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    inFile = open('GasPrices.txt', 'r')                             # Open file.
    gasList = inFile.readlines()                          # Read file to a list.
    inFile.close()                                                 # Close file.
    yearlyAvgOutput(gasList)      # Call function to display the yearly average.
    monthlyAvgOutput(gasList)    # Call function to display the monthly average.
    highestPerYearOutput(gasList)  # Call to display the highest price per year.
    lowestPerYearOutput(gasList)    # Call to display the lowest price per year.
    
# Calls main to start program.
if __name__ == "__main__":
    main()