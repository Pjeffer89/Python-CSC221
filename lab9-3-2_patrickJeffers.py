# Patrick Jeffers   Lab 9-3-2   2/18/2022
# Based on exercise 9-3 in the book.  This is a companion program to lab 9-3.
# This program opens, decrypts, then displays the contents of a file created in
# the other program.

# This function is passed file contents and a dictionary of encryption code 
# keys.  The function then converts and returns the decrypted version based on
# the encryption code.
def decrypt(fileContents, CODE):
    decryptedContents = ''                 # Creates empty string to build upon.
    for i in fileContents:     # Iterates through entire contents while ignoring
        if i.isspace():         # spaces. Each characters corresponding value is
            decryptedContents += i          # added to the string created above.
        else:
            decryptedContents += CODE[i]
    return decryptedContents

# Main function for the program, controls the flow and calls other functions as
# required.
def main():
    # Stores encryption codes.
    CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}
    
    inFile = open('encryptedText.txt', 'r')                   # Open input file.
    fileContents = inFile.read()                    # Read input file to a list.
    inFile.close()                                                 # Close file.
    
    decryptedContents = decrypt(fileContents, CODE)     # Get decrypted version.
    
    print(decryptedContents)                   # Display decrypted text to user.

# Calls main to start program.
if __name__ == '__main__':
    main()