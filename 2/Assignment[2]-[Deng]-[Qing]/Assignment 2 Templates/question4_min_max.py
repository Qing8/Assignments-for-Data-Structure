def min_max(l):
    '''
    @l: list of integers.

    @return: list, or tuple of two elements. 
    First element is min, second element is max.
    '''
    
    i = 0
    maxs = []
    mins = []
    while i < len(l):
        if l[i] < l [i+1]:
            b = l[i+1]
            s = l[i]
        elif l[i] > l[i+1]:
            b = l[i]
            s = l[i+1]
        elif l[i] == l[i+1]:
            b = s = l[i]
        maxs.append(b)
        mins.append(s)
        i += 2
    
    
    max_num = maxs[0]
    min_num = mins[0]
    
    for a in maxs[1:]:
        if a > max_num:
            max_num = a
            
    for m in mins[1:]:
        if m < min_num:
            min_num = m
    return [min_num,max_num]

print(min_max([6,2,5,8,1,-4,6,12,78,21,55,62,1,0]))











