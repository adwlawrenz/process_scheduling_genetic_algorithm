import Individual
import random
import copy

def geneticAlgorithm(procInfo, numGenerations):
    individuals = []
    fastCoreString = []
    slowCoreString = []

    # Create initial population
    for x in range(20):
        fastCoreString.clear()
        slowCoreString.clear()

        individuals.append(Individual.Individual())
        randNum = (int(random.random() * 100000000000) % 6) + 5
        for i in range(randNum):
            fastCoreString.append(procInfo[i])
        individuals[x].setFastCoreString(fastCoreString)
        for i in range(randNum, 15):
            slowCoreString.append(procInfo[i])
        individuals[x].setSlowCoreString(slowCoreString)
        individuals[x].mutate()

    # Run genetic algorithm
    for x in range(numGenerations):
        bestIndividuals = []

        # Gets the 5 individuals with the highest fitness
        for i in range(20):
            if i < 5:
                bestIndividuals.append(individuals[i])
            else:
                lowFitness = bestIndividuals[0].getFitness()
                lowFitnessIdx = 0
                for y in range(1, 5):
                    if bestIndividuals[y].getFitness() > lowFitness:
                        lowFitness = bestIndividuals[y].getFitness()
                        lowFitnessIdx = y
                if individuals[i].getFitness() < lowFitness:
                        bestIndividuals[lowFitnessIdx] = individuals[i]
        individuals.clear()
        individuals.extend(bestIndividuals)

        # Creates mutated versions of the original 5 individuals
        for i in range(5):
            individuals.append(Individual.Individual())
            individuals[i + 5].deepCopy(individuals[i])
            individuals[i + 5].mutate()

        # Creates 10 individuals with genetic crossover between the original 5
        for i in range(10):
            individuals.append(Individual.Individual())
        individuals[10].geneticCrossover(individuals[0], individuals[1])
        individuals[11].geneticCrossover(individuals[0], individuals[2])
        individuals[12].geneticCrossover(individuals[0], individuals[3])
        individuals[13].geneticCrossover(individuals[0], individuals[4])
        individuals[14].geneticCrossover(individuals[1], individuals[2])

        individuals[15].geneticCrossover(individuals[1], individuals[3])
        individuals[16].geneticCrossover(individuals[1], individuals[4])
        individuals[17].geneticCrossover(individuals[2], individuals[3])
        individuals[18].geneticCrossover(individuals[2], individuals[4])
        individuals[19].geneticCrossover(individuals[3], individuals[4])

    bestIndividual = individuals[0]
    bestIndividualFitness = individuals[0].getFitness()
    for i in range(1, 20):
        if individuals[i].getFitness() < bestIndividualFitness:
            bestIndividualFitness = individuals[i].getFitness()
            bestIndividual = individuals[i]
    print("Best individual's fast core string: ", bestIndividual.getFastCoreString())
    print("Best individual's slow Core string: ", bestIndividual.getSlowCoreString())
    print("Best individual's avg wait time: ", bestIndividual.getAvgWaitTime())
    print("Best individual's total run time: ", bestIndividual.getTotalRunTime())
    print()

def firstComeFirstServe(procInfo):
    individual = Individual.Individual()
    fastCoreString = []
    slowCoreString = []
    for i in range(15):
        if (i % 2) == 0:
            slowCoreString.append(procInfo[i])
        else:
            fastCoreString.append(procInfo[i])

    individual.setFastCoreString(fastCoreString)
    individual.setSlowCoreString(slowCoreString)
    print("FCFS fast core string: ", individual.getFastCoreString())
    print("FCFS slow Core string: ", individual.getSlowCoreString())
    print("FCFS avg wait time: ", individual.getAvgWaitTime())
    print("FCFS total run time: ", individual.getTotalRunTime())
    print()

def shortestJobFirst(procInfo):
    individual = Individual.Individual()
    fastCoreString = []
    slowCoreString = []
    for i in range(15):
        shortestProc = procInfo[0]
        shortestProcIdx = 0
        for x in range(len(procInfo)):
            if procInfo[x][1] < shortestProc[1]:
                shortestProc = procInfo[x]
                shortestProcIdx = x
        del procInfo[shortestProcIdx]
        if (i % 2) == 0:
            slowCoreString.append(shortestProc)
        else:
            fastCoreString.append(shortestProc)

    individual.setFastCoreString(fastCoreString)
    individual.setSlowCoreString(slowCoreString)
    print("SJF fast core string: ", individual.getFastCoreString())
    print("SJF slow Core string: ", individual.getSlowCoreString())
    print("SJF avg wait time: ", individual.getAvgWaitTime())
    print("SJF total run time: ", individual.getTotalRunTime())
    print()

if __name__ == '__main__':
    test1 = []
    test2 = []
    test3 = []
    for i in range(15):
        test1.append((i, (int(random.random() * 100000000000) % 25) + 1))
        test2.append((i, (int(random.random() * 100000000000) % 25) + 1))
        test3.append((i, (int(random.random() * 100000000000) % 25) + 1))
    print("Test 1 Values: ", test1)
    geneticAlgorithm(test1, 10000)
    firstComeFirstServe(test1)
    shortestJobFirst(test1)

    print("Test 2 Values: ", test2)
    geneticAlgorithm(test2, 10000)
    firstComeFirstServe(test2)
    shortestJobFirst(test2)

    print("Test 3 Values: ", test3)
    geneticAlgorithm(test3, 10000)
    firstComeFirstServe(test3)
    shortestJobFirst(test3)
