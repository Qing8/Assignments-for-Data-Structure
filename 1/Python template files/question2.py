def palindrome(string):
    '''
    ##Comment out print functions if you submit on gradescope.
    @string: The string being tested

    @return True if string is a palindrome
            False otherwise
    '''
    # To do
    string = string.lower()
    return string == string[::-1]

#print(palindrome("WASITACARORACATISAW"))