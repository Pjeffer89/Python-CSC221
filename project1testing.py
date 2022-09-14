def main():
    sumOfZip = int(input('Enter Sum: '))
    
    sumModulo = sumOfZip % 10
    checkDigit = 10 - sumModulo
    
    if checkDigit > 9:
        checkDigit = sumOfZip % 10
    
    print(checkDigit)
    
main()

itemWeight = 0.0
postageType = 0
mailingQuantity = 0
postage = 0.0
zipCode = ''
name = ''
address = ''
city = ''
state = ''
postageCost = 0.0
checkDigit = 0
barcode = ''