def largest_ten(l):
    # Assuming list size greater than 10
    '''
    @l: list of integers
    
    remember to mention your runtime!

    @return: largest ten elements in list l.
    '''
    
    l2 = l[:]    
    
########################### Solution 1 (merge sort) ######################################
    def merge_sort(lst):
        length = len(lst)
        
        if length == 1:
            return lst
        
        mid = length // 2
        first_half = merge_sort(lst[:mid])
        second_half = merge_sort(lst[mid:])
        sorted_list = []
        while first_half != [] and second_half != []:
            if first_half[0] > second_half[0]:
                sorted_list.append(second_half[0])
                second_half.pop(0)
                
            elif first_half[0] < second_half[0]:
                sorted_list.append(first_half[0])
                first_half.pop(0)
            else:
                sorted_list.append(first_half[0])
                first_half.pop(0)
                second_half.pop(0)
                
        if first_half == []:
            sorted_list += second_half
        elif second_half == []:
            sorted_list += first_half
            
        return sorted_list
    
    sorted_list = merge_sort(l2)
    return sorted_list[-10:]
    # Run Time O(nlogn)

################ Solution 2 (Use Recursion to find Max 10) ####################
    
    # Unfinished, i don't know how to find 
    # the 2nd or 3th or 4th...largest number
    # this piece of code can ony find the largest number.
    # i know the problem is that i do not delete the largetst number i already 
    # found in the list
    # but i don't know how to pass an edited list whose largest number already 
    # been deleted
#    def find_max(lst):
#        
#        if len(lst) == 1:
#            return lst[0]
#            
#            
#        else:
#            if lst[0] > find_max(lst[1:]):
#                return lst[0]
#                
#            else:
#                return find_max(lst[1:])
#        
#                
#    max_10 = []
#    for _ in range(10):
#        max_num = find_max(l2)
#        max_10.append(max_num)
#    return max_10

    


print(largest_ten([9,8,6,4,22,68,13,45,778,356,45,2,1,5,78,5,7,3,6,8,10]))

