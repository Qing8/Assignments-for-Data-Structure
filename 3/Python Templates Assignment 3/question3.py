def unique(s):
    '''
    @S: input list sequence.

    Use recursion, runtime should be O(n^2)
    # Don't print anything if you want to submit on gradescope!


    @return: True if all elements are unique.
             False otherwise.
    '''
    if len(s) == 1:
        return True
    elif len(s) > 1:
        return (s[0] not in s[1:] and unique(s[1:]))
    
    
#print(unique([1,7,6,5,4,3,1]))    # False
#print(unique([9,4,3,2,1,8]) )     # True