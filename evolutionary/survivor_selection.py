"""
My collection of survivor selection methods

Student number: 20095996
Student name: Brian Herman
"""

#imports
import random

def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []
    
    # student code starts
    population = current_pop + offspring
    fitness = current_fitness + offspring_fitness
    mu = len(current_pop)
    fitness, population = (list(l) for l in zip(*sorted(zip(fitness, population))))
    fitness = fitness[-mu:]
    population = population[-mu:]
    # student code ends
    
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    current_fitness, current_pop = (list(l) for l in zip(*sorted(zip(current_fitness, current_pop))))
    for i in range(len(offspring)):
        current_pop[i] = offspring[i]
        current_fitness[i] = offspring_fitness[i]

    population = current_pop
    fitness = current_fitness
    # student code ends
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts
    num_of_offspring = len(offspring)
    sample = random.sample(range(len(current_pop)), num_of_offspring)
    for index in range(len(sample)):
        current_pop[sample[index]] = offspring[index]
        current_fitness[sample[index]] = offspring_fitness[index]
    population = current_pop
    fitness = current_fitness
    # student code ends
    
    return population, fitness

