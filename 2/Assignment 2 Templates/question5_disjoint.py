def three_way_disjoint(l1, l2, l3):
    '''
    @l1: first list of elements
    @l2: second list of elements
    @l3: third list of elements

    @return True if l1,l2,l3 are disjoint.
    False if l1,l2,l3 are not disjoint.
    '''
    l4 = l1+l2+l3
    
    def merge_sort(lst):
        
        if len(lst) == 1:
            return lst
        
        length = len(lst)
        mid = length // 2
        first_half = merge_sort(lst[:mid])
        second_half = merge_sort(lst[mid:])
        
        sorted_list = []
        while first_half != [] and second_half != []:
            if first_half[0] > second_half[0]:
                sorted_list.append(second_half[0])
                second_half.pop(0)
            elif first_half[0] == second_half[0]:
                sorted_list.append(first_half[0])
                sorted_list.append(second_half[0])
                first_half.pop(0)
                second_half.pop(0)
            else:
                sorted_list.append(first_half[0])
                first_half.pop(0)
        if first_half == []:
            sorted_list += second_half
        else:
            sorted_list += first_half
            
        return sorted_list

    sorted_list = merge_sort(l4)
    target = 1
    count = 1
    while target < len(sorted_list):
        
        if sorted_list[target] != sorted_list[target-1]:
            count = 1
            target += 1
        elif sorted_list[target] == sorted_list[target-1]:
            count += 1
            target += 1
            
            if count > 2:
                return False
            
    return True

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10,11,12]
l3 = [5,13,14,15,16]
l4 = [5,6,7,8,9,10,11]

print(three_way_disjoint(l1,l2,l3))
print(three_way_disjoint(l1,l4,l3))
print(three_way_disjoint(l2,l4,l3))

