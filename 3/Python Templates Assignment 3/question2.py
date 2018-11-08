def recur(n):
    if (n < 0):
        return recur(-n)
    elif (n < 10):
        return n
    else:
        return (n % 10 + recur(n // 10))


def iteration(n):
    '''
    iteration function. (use loops)
    Should do exactly the same task as the recursive function above.
    # Don't print anything if you want to submit on gradescope!

    '''
    n = abs(n)
    if len(str(n)) <= 2:
        return n
    elif len(str(n)) > 2:
        summ = 0
        for i in str(n):
            summ += int(i)
        return summ
    
#print(recur(-134))
#print(iteration(-134))

