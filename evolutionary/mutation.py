"""
My colleciton of mutation methods

Student number: 20095996
Student name: Brian Herman
"""

# imports
import random

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts
    swaps = random.sample(range(len(individual)),2)
    mutant[swaps[0]] = individual[swaps[1]]
    mutant[swaps[1]] = individual[swaps[0]]
    # student code ends
    
    return mutant
