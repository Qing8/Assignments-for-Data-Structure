def anagram(string1, string2):
    '''
    ##Comment out print functions if you submit on gradescope.
    @string1: The first string
    @string2: The second string

    @return True if string1 is anagram of string2
            False otherwise
    '''
    # To do
    string1 = string1.lower()
    string2 = string2.lower()
    string = string1+string2
    new_long_string = ""
    
    for i in string:
        if i.isalpha():
            new_long_string += i
        
    marker = 0
    for i in new_long_string:
        marker = marker^ord(i)

    if marker == 0 :
        return True
    else:
        return False


string1 = "1 23"
string2 = "3 2 1"
#print(anagram(string1, string2))      
        
