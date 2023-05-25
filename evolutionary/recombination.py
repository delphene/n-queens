"""
My collection of recombination methods

Student number: 20095996
Student name: Brian Herman
"""

#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    #choose slice
    slice = random.randint(1,6)
    ins = slice
    #get first section
    offspring1 = parent1[:slice]
    offspring2 = parent2[:slice]
    #get second section from opposite parent
    offspring1Skip = 0
    offspring2Skip = 0
    board_length = len(parent1)
    for i in range(ins, board_length):
        if(parent2[ins] not in offspring1):
            offspring1.append(parent2[ins])
        else:
            offspring1Skip += 1
        if(parent1[ins] not in offspring2):
            offspring2.append(parent1[ins])
        else:
            offspring2Skip += 1

        ins += 1
    #fill empty space from first parent choice
    for i in range(offspring1Skip):
        while parent2[i] in offspring1:
            i += 1
        offspring1.append(parent2[i])
            
    for i in range(offspring2Skip):
        while parent1[i] in offspring2:
            i += 1
        offspring2.append(parent1[i])
    # student code end
    
    return offspring1, offspring2
