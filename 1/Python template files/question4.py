def addOne(digits):
    '''
    ##Comment out print functions if you submit on gradescope.
    @digits: a list of digits
    
    @return a list of digits, which is @digits added 1 to it.
    '''
    # To do
    
    def check(l):

        position = -1
        while l[position] == 9:
            position -= 1
        print(position+1)
        return position+1
    
    
    
    if len(digits) == digits.count(9):
        return [1] + [0]*len(digits)
    elif digits[-1] == 9 :
        position = check(digits)
        return digits[:position-1] + [digits[position-1]+1] + [0]*abs(position)
    else:
        return digits[:-1] + [digits[-1]+1]
              
    
#print(addOne([1,2,3]))
#print(addOne([1,9,9,9,8]))
#print(addOne([9]))