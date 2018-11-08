import copy

result = []    # You can use a global list to get result easier.
def generateBillboard_driver(names, team_size):
    generateBillboard(names, team_size, [], 0)

def generateBillboard(casts, number_of_casts, result_list, position):
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
    
    
    pass

    
casts = ["Johnny Depp", "Al Pacino", "Robert De Niro", "Kevin Spacey", "Denzel Washington", "Russell Crowe", "Brad Pitt"]
generateBillboard_driver(casts, 4)   # Choose 4 out of 7
#print(result)