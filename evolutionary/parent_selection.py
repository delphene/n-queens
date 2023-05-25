"""
My collection of parent selection methods

Student number: 20095996
Student name: Brian Herman
"""

# imports
import random

def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    current_member = 1
    i = 1
    r = random.uniform(0,1/mating_pool_size)
    a = []
    total = 0
    for ind in fitness:
        total += ind
        a.append(total)
    step = (1/mating_pool_size)*total
    r = random.uniform(0,step)
    while (current_member <= mating_pool_size):
        while (r <= a[i]):
            selected_to_mate.append(i)
            r = r + step
            current_member = current_member + 1
        i += 1
    # student code ends
    
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []

    # student code starts
    
    # with replacement (perm)
    current_member = 1
    while (current_member <= mating_pool_size):
        tournament = random.sample(range(len(fitness)),tournament_size)
        winner = -1
        most_fit = -1
        for i in tournament:
            if fitness[i] > most_fit:
                winner = i
        selected_to_mate.append(winner)
        current_member += 1
    # without replacement (comb)
    # current_member = 1
    # while (current_member <= mating_pool_size):
    #     tournament = []
    #     for i in range(len(tournament_size)):
    #         tournament.append(random.randint(0,len(fitness) - 1))
    #     winner = -1
    #     most_fit = -1
    #     for i in tournament:
    #         if fitness[i] < most_fit:
    #             winner = i
    #     selected_to_mate.append(winner)
    #     current_member += 1
    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts
    selected_to_mate = random.sample(range(population_size),mating_pool_size)
    # student code ends
    
    return selected_to_mate