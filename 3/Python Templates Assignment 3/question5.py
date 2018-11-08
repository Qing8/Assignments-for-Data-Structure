import copy
'''
@casts: list of casts
@number_of_casts: choose how many casts
@result_list: Additional list parameter for recursion
@position: Additional index parameter for recursion

# Base case 1: we get enough person in the result_list.
# Base case 2: we have checked all the casts.

# Create two branches
# Branch 1 add current person to result_list
# Branch 2 does not add current person to result_list(copy)
# Move on to the next person


# Don't print anything if you want to submit on gradescope!


@return: List of all combinations of casts
'''

result = []
def generateBillboard_driver(names, team_size):
    return generateBillboard(names, team_size, [], 0)
    
def generateBillboard(casts, number_of_casts, result_list, position):
    global result
    
    if len(casts) == number_of_casts:
        return [casts]
    
    if (number_of_casts) == 1:
        
        for i in casts:
            result_list.append([i])
        return result_list
    
    alone = casts[0]
    minus_one_combination = generateBillboard(casts[1:],number_of_casts-1,result_list,position)
    for i in minus_one_combination:
        if len(i)<number_of_casts:
            i.append(alone)
 
    return minus_one_combination +  generateBillboard(casts[1:], number_of_casts, [], position)

casts = ["Johnny Depp", "Al Pacino", "Robert De Niro", "Kevin Spacey", "Denzel Washington", "Russell Crowe", "Brad Pitt"]
#print(generateBillboard_driver(casts, 2))  # Choose 4 out of 7

#print(generateBillboard_driver([1,2,3,4], 2))


    
    

    
