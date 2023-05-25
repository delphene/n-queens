import numpy as np
import random

def print_board(board):
    # Prints a formated version of the board that supports and size list
    print(end='[')
    length = len(board) - 1
    for i in range(length):
        if i != length:
            print(i,end=', ')
    print(board[-1],end=']')

def generatePopulation(boardSize, popSize):
    pop = []
    perm = range(1, boardSize+1)
    for ind in range(popSize):
        #i dont want a numpy array i want a normal array
        pop.append(np.random.permutation(perm).tolist())
    
    return pop

def nQueens(boardSize, popSize, genSize):
    #generate random initial population
    pop = generatePopulation(boardSize, popSize)
    popRange = range(popSize)
    boardRange = range(boardSize)
    gen = genSize
    
    #set fitness 
    fit = []
    for individual in range(popSize):
        conflicts = 0
        for queen in range(boardSize):
            for comp in range(queen+1, boardSize):
                pos = abs(pop[individual][queen] - pop[individual][comp])
                neg = abs(queen - comp)
                # if(pop[individual][queen] == pop[individual][comp] or pos == neg): # not possible
                if(pos == neg):
                    conflicts += 1

        fit.append(28 - conflicts)
        if conflicts == 0:
            return pop[individual]

    while(gen > 0):
        print("generation number", genSize - gen + 1, "\n")

        print('population')
        for i in range(popSize):
            print("board #" + str(i), pop[i], fit[i])

        #parent selection
        sampleIndex = random.sample(popRange,5)

        sample = []
        for i in range(5):
            sample.append((sampleIndex[i], fit[sampleIndex[i]]))

        first = [0, -1]
        second = [0, -1]
        for i in sample:
            if (i[1] > second[1]):
                if (i[1] >= first[1]):
                    second = first
                    first = i
                else:
                    second = i

        print("\nparents")
        parentOne = pop[first[0]]
        parentTwo = pop[second[0]]
        print(parentOne)
        print(parentTwo)

        #recombination
        slice = random.randint(1,6)
        childOne = parentOne[:slice]
        childTwo = parentTwo[:slice]
        ins = slice
        childOneSkip = 0
        childTwoSkip = 0
        for i in range(ins, boardSize):
            #child 1
            if(parentTwo[ins] not in childOne):
                childOne.append(parentTwo[ins])
            else:
                childOneSkip += 1
            #child 2
            if(parentOne[ins] not in childTwo):
                childTwo.append(parentOne[ins])
            else:
                childTwoSkip += 1

            ins += 1
        
        for i in range(childOneSkip):
            childOne.append(parentTwo[i])

        for i in range(childTwoSkip):
            childTwo.append(parentOne[i])

        #mutation
        #child 1
        swaps = random.sample(boardRange,2)
        temp = childOne[swaps[0]]
        childOne[swaps[0]] = childOne[swaps[1]]
        childOne[swaps[1]] = temp
        #child 2
        swaps = random.sample(boardRange,2)
        temp = childTwo[swaps[0]]
        childTwo[swaps[0]] = childTwo[swaps[1]]
        childTwo[swaps[1]] = temp

        print("\nchildren")
        print(childOne)
        print(childTwo)

        #get fitness of new boards
        
        # conflicts = 0
        # for queen in range(boardSize):
        #     for comp in range(queen+1, boardSize):
        #         pos = abs(childOne[queen] - childOne[comp])
        #         neg = abs(queen - comp)
        #         if (pos == neg):
        #             conflicts += 1
        # childOneFit = 28 - conflicts

        # conflicts = 0
        # for queen in range(boardSize):
        #     for comp in range(queen+1, boardSize):
        #         pos = abs(childTwo[queen] - childTwo[comp])
        #         neg = abs(queen - comp)
        #         if (pos == neg):
        #             conflicts += 1
        # childTwoFit = 28 - conflicts

        childFit = []
        for child in [childOne, childTwo]:
            conflicts = 0
            for queen in range(boardSize):
                for comp in range(queen+1, boardSize):
                    pos = abs(child[queen] - child[comp])
                    neg = abs(queen - comp)
                    # if(pop[individual][queen] == pop[individual][comp] or pos == neg): # not possible
                    if(pos == neg):
                        conflicts += 1
                        
            if conflicts == 0:  # termination santa clause
                return child

            childFit.append(28 - conflicts)

        #survivor selection
        low1 = 29
        low2 = 29
        ind1 = 0.1
        ind2 = 0.1
        for i in range(len(fit)):
            if (fit[i] < low2):
                if (fit[i] <= low1):
                    low2 = low1
                    ind2 = ind1
                    low1 = fit[i]
                    ind1 = i
                else:
                    low2 = fit[i]
                    ind2 = i

        print(low1, ind1, low2, ind2)

        gen -= 1

    r = "no solution found within", genSize, "generation"
    return r

print(nQueens(8, 5, 1))

def two_of_five_selection(population_size, fitness):
    sampleIndex = random.sample(range(population_size),5)

    sample = []
    for i in range(5):
        sample.append((sampleIndex[i], fitness[sampleIndex[i]]))

    first = [0, -1]
    second = [0, -1]
    for i in sample:
        if (i[1] > second[1]):
            if (i[1] >= first[1]):
                second = first
                first = i
            else:
                second = i
    
    return first[0], second[0]