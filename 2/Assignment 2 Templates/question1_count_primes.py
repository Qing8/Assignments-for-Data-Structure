import math
def count_primes(n):
    '''
    @n: count the number of prime numbers less than n.

    @return: number of prime numbers less than n.
    '''

############################# Solution 1 ######################################
    counter = 0
    for i in range(2,n+1):
        result = True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                result = False
        if result:
            counter += 1
    return counter
     #Run Time O(n^(3/2))

############## Solution 2  (reference from  LEETCODE solution) ################
     
############## much much more concise than Solution1 :\ #####################
    
#     #index 0,1,'2',3,'4',5,'6'...
#     #list [1,2,'3',4,'5',6,'7'...]
#    
#    result = [1] * n
#    result[0],result[1] = 0,0
#    search_end = int(math.sqrt(n))+1
#    
#    for i in range(2,search_end):
#        
#        if result[i] == 1:
#            result[i*i:n:i] = [0] * len(result[i*i:n:i])
#            
#    return sum(result)
#    # Run Time O(n)
    
    
print(count_primes(111)) # Should prints 4.





















