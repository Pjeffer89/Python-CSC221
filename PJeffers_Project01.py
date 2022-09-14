# Patrick Jeffers   Postal Barcode Project01   1/30/2022
# This program creates mailing labels from either user input or from a file of 
# address information.

# This function displays the main menu.
def displayMenu():
    print('1 – Single Mailing')
    print('2 – Multiple Mailings')
    print('3 -- Quit')
    
# This function accepts the user’s choice for type of postage and the weight of 
# the item as arguments and calculates and returns the postage.
def calcPostage(postageType, itemWeight):
    import math
    if postageType == 1:
        if itemWeight <= 1.0:
            totalCost = 0.49
        elif itemWeight > 1.0:
            totalCost = ((math.ceil(itemWeight) - 1) * (0.22)) + 0.49
            totalCost = round(totalCost, 2)
    elif postageType == 2:
        if itemWeight <= 1.0:
            totalCost = 0.98
        elif itemWeight > 1.0:
            totalCost = ((math.ceil(itemWeight) - 1) * (0.22)) + 0.98
            totalCost = round(totalCost, 2)
    else:
        if itemWeight <= 3:
            totalCost = 2.54
        elif itemWeight > 3:
            totalCost = ((math.ceil(itemWeight) - 3) * (0.20)) + 2.54
            totalCost = round(totalCost, 2)
    return totalCost
            
# This function accepts the five individual zip code digits as arguments and 
# calculates and returns the check digit.
def calcCheckDigit(zip1,zip2,zip3,zip4,zip5):
    zipArray = [zip1,zip2,zip3,zip4,zip5]
    sumOfZip = 0
    for i in zipArray:
        i = int(i)
        sumOfZip += i
    sumModulo = sumOfZip % 10
    checkDigit = 10 - sumModulo
    if checkDigit > 9:
        checkDigit = sumOfZip % 10
    return str(checkDigit)
    
# This function accepts the five individual zip code digits and the check digit 
# as arguments and returns the barcode string.
def createBarcode(zip1,zip2,zip3,zip4,zip5,checkDigit):
    barcode = ''                             # Creates empty string to build on.
    BARCODES = [':::||','::|:|','::||:',':|::|',':|:|:',':||::','|:::|','|::|:',
                '|:|::','||:::']                            # Barcode constants.
    fullZipArray = [zip1,zip2,zip3,zip4,zip5,checkDigit] 
    for i in fullZipArray:                     
        if i == '1':
            barcode+=(BARCODES[0])
        elif i == '2':
            barcode+=(BARCODES[1])
        elif i == '3':
            barcode+=(BARCODES[2])         # Transposes each digit to the
        elif i == '4':                     # corresponding barcode segment then
            barcode+=(BARCODES[3])         # returns the final barcode.
        elif i == '5':
            barcode+=(BARCODES[4])
        elif i == '6':
            barcode+=(BARCODES[5])
        elif i == '7':
            barcode+=(BARCODES[6])
        elif i == '8':
            barcode+=(BARCODES[7])
        elif i == '9':
            barcode+=(BARCODES[8])
        elif i == '0':
            barcode+=(BARCODES[9])
    return ('|' + barcode + '|')

# This function accepts the customer’s name, street address, city, state, 
# zipcode, postage and barcode and displays a mailing label.
def displayMailingLabel(name,address,city,state,zipCode,postageCost,barcode):
    print()
    print('**************************$' + str(postageCost))
    print(name)
    print(address)
    print(city + ' ' + state + ' ' + zipCode)
    print(barcode)
    print()

# This function reads the specified text file and displays mailing labels for 
# each record in the file. This function accepts no arguments (all needed 
# information is read from file) and calls functions 2 – 5 to complete the task 
# of displaying mailing labels.
def processDataFile():
    inFile = open('postalBarcodeData.txt', 'r')  # Open file and read into list.
    rawMailingList = inFile.readlines()
    inFile.close()
    mailingList = [i.strip() for i in rawMailingList]           # Strip newline.
    nameList = mailingList[0::8]        # Creates individual lists of each type.
    addressList = mailingList[1::8]
    cityList = mailingList[2::8]
    stateList = mailingList[3::8]
    zipList = mailingList[4::8]
    parcelTypeList = mailingList[5::8]
    weightList = mailingList[6::8]
    for i in range(len(nameList)):       # Gets calculated values for each entry
        name = nameList[i]               # and displays output the same as main.
        address = addressList[i]
        city = cityList[i]
        state = stateList[i]
        zipCode = zipList[i]
        postageType = int(parcelTypeList[i])
        itemWeight = float(weightList[i])
        postageCost = calcPostage(postageType, itemWeight)
        checkDigit = calcCheckDigit(zipCode[0],zipCode[1],zipCode[2],zipCode[3],
                            zipCode[4])
        barcode = createBarcode(zipCode[0],zipCode[1],zipCode[2],zipCode[3],
                        zipCode[4],checkDigit)        
        displayMailingLabel(name,address,city,state,zipCode,postageCost,barcode)
    
# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    loop = 1                                                 # For loop control.
    print('Welcome to the Mailing Label Printing System' + '\n')      # Heading.
    while loop == 1:
        displayMenu()                                           # Displays menu.
        print()
        mailingQuantity = int(input('Enter your choice:  '))    # Get user info.
        if mailingQuantity == 1:                # For individual label creation.
            name = input('Enter name: ')
            address = input('Enter street address: ')
            city = input('Enter city: ')
            state = input('Enter state: ')
            zipCode = input('Enter zip code: ')
            postageType = int(input('Enter 1 for letter, 2 for large '\
                                    'envelope, 3 for parcel: '))
            itemWeight = float(input('Enter weight in ounces: '))
            # Calculates cost.
            postageCost = calcPostage(postageType, itemWeight)
            # Gets check digit.
            checkDigit = calcCheckDigit(zipCode[0],zipCode[1],zipCode[2],
                                        zipCode[3],zipCode[4])
            # Gets barcode.
            barcode = createBarcode(zipCode[0],zipCode[1],zipCode[2],zipCode[3],
                                    zipCode[4],checkDigit)
            # Display.
            displayMailingLabel(name,address,city,state,zipCode,postageCost,
                                barcode)
            print()
        if mailingQuantity == 2:      # Processes and displays file information.
            processDataFile()
            print()
        if mailingQuantity == 3:                                 # Ends program.
            print()
            print('Thank you')
            loop = 0

# Calls main to start program.
if __name__ == "__main__":
    main()