"""
My collection of initialization methods for different representations

Student number: 20095996
Student name: Brian Herman
"""

#imports
import numpy as np

def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    # student code begin
    population = []
    perm = range(1, chrom_length+1)
    for ind in range(pop_size):
        population.append(np.random.permutation(perm).tolist())
    
    #student code end
    
    return population                     

