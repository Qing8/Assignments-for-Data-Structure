def merge(I1, I2):  
    '''
    @I1: first iterable object. Can be a string!
    @I2: second iterable object.

    @return: alternately merged I1, I2 elements in a list.
    '''   
#########################3##### Solution 1 ##################################   
    l1 = list(I1)
    l2 = list(I2)
    
    a = len(l1)
    b = len(l2)
    
    new_l = []
    
    def combine(length):
        for i in range(length):
            new_l.append(l1[i])
            new_l.append(l2[i])        
        return new_l

    if a < b:
        new_l = combine(a)
        new_l += l2[a:]
        
    elif a > b:
        new_l = combine(b)
        new_l += l1[b:]
        
        
    elif a == b:
        new_l = combine(a)
            
    return new_l
    
#########################3##### Solution 2 ####################################
#
#    l1 = list(I1)
#    l2 = list(I2)
#    
#    if len(l1) > len(l2):
#        extra = l1[len(l2):]
#        l1 = l1[:len(l2)]
#    elif len(l2) > len(l1):
#        extra = l2[len(l1):]
#        l2 = l2[:len(l1)]
#        
#    lst = (len(l1)+len(l2)) *[0]
#    
#    lst[::2] = l1
#    lst[1::2] = l2
#    
#    lst += extra
#    return lst

    



print([i for i in merge("what",range(100,105))])
print([i for i in merge(range(5),range(100,101))])
print([i for i in merge(range(1),range(100,105))])