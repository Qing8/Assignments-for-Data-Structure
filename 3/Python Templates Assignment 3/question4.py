def pascal(n):
    '''
    @n: number of levels in pascal triangle

    # Don't print anything if you want to submit on gradescope!


    @return: list of sublists. Each sublist contain a level's values
    '''
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    
    else:
        last_level = pascal(n-1)
        this_level = last_level[:]
        this_level.append([1])
        
        for i in range(len(last_level)-1):
            this_level[-1].append(last_level[-1][i] + last_level[-1][i+1])
            
        this_level[-1].append(1)
        
        return this_level


#print(pascal(8))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]