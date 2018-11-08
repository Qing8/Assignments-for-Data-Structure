def gcd(a, b):
    '''
    ##Comment out print functions if you submit on gradescope.
    @a: the first integer
    @b: the second integer

    @return the greatest common divisor of integer a and b.
    '''
    # To do
    if a > b:
        larger = a
        smaller = b
    elif a < b:
        larger = b
        smaller = a
    else:
        return a
    
    remainder = larger % smaller
    if remainder == 0 :
        return smaller
    elif remainder == 1:
        return 1
    else:
        return gcd(smaller,remainder)

#print(gcd(26, 45))
#print(gcd(45, 15))
