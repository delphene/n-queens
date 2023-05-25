"""
My collection of fitness evaluation methods

Student number: 20095996
Student name: Brian Herman
"""

#imports


def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    fitness = 0
    # student code begin
    length = len(individual)
    for queen in range(length):
        for comp in range(queen+1, length):
            pos = abs(individual[queen] - individual[comp])
            neg = abs(queen - comp)
            # if(pop[individual][queen] == pop[individual][comp] or pos == neg): # not possible
            if(pos == neg):
                fitness += 1
    max_conflicts = ((len(individual) - 1)*len(individual))/2
    fitness = max_conflicts - fitness
    # student code end
    
    return fitness