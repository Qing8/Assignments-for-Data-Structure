def power(x,n):
    '''
    @x: the base, integer
    @n: the exponent, integer

    x, n can be negative integer.
    # Don't print anything if you want to submit on gradescope!

    @return: x^n
    '''
    if 0 <= n <= 1:
        return x**n
    else:
        if n > 1:
            return x*power(x,n-1)
        elif n < 0:
            return 1/(power(x,-n))

#print(power(-2, -3))    # -0.125
#print(power(4, 3))      # 64