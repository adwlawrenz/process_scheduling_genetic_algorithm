import random

class Individual:

    def __init__(self):
        self.fastCoreString = [] # list of tuples that contain: (<process number>, <process length>)
        self.slowCoreString = [] # list of tuples that contain: (<process number>, <process length>)
        self.avgWaitTime = 0
        self.totalRunTime = 0
        self.fitness = 0

    def deepCopy(self, individual):
        self.setFastCoreString(individual.fastCoreString)
        self.setSlowCoreString(individual.slowCoreString)
        self.avgWaitTime = individual.avgWaitTime
        self.totalRunTime = individual.totalRunTime
        self.fitness = individual.fitness

    def setFastCoreString(self, coreString):
        for proc in coreString:
            self.fastCoreString.append(proc)

    def setSlowCoreString(self, coreString):
        for proc in coreString:
            self.slowCoreString.append(proc)

    def getFastCoreString(self):
        return self.fastCoreString

    def getSlowCoreString(self):
        return self.slowCoreString

    def getAvgWaitTime(self):
        self.avgWaitTime = 0
        coreAvg = 0
        i = 0
        for p, l in self.fastCoreString:
            coreAvg += i
            i += l * 0.80

        i = 0
        for p, l in self.slowCoreString:
            coreAvg += i
            i += l

        self.avgWaitTime = coreAvg / (len(self.fastCoreString) + len(self.slowCoreString))
        return self.avgWaitTime

    def getTotalRunTime(self):
        self.totalRunTime = 0
        fastCoreRunTime = 0
        slowCoreRunTime = 0

        for p, l in self.fastCoreString:
            fastCoreRunTime += l * 0.80
        for p, l in self.slowCoreString:
            slowCoreRunTime += l

        if fastCoreRunTime > slowCoreRunTime:
            self.totalRunTime = fastCoreRunTime
        else:
            self.totalRunTime = slowCoreRunTime
        return self.totalRunTime

    def getFitness(self):
        self.fitness = 0
        self.getTotalRunTime()
        self.getAvgWaitTime()
        self.fitness = self.avgWaitTime + self.totalRunTime
        return self.fitness

    def mutate(self):
        # switch a process from fast core string to slow core string
        # and switch a process from slow core string to fast core string
        fastRandNum = int(random.random() * 100000000000) % len(self.fastCoreString)
        slowRandNum = int(random.random() * 100000000000) % len(self.slowCoreString)
        fastTemp = self.fastCoreString[fastRandNum]
        slowTemp = self.slowCoreString[slowRandNum]
        del self.fastCoreString[fastRandNum]
        del self.slowCoreString[slowRandNum]
        self.fastCoreString.insert(int(random.random() * 10000000) % len(self.fastCoreString), slowTemp)
        self.slowCoreString.insert(int(random.random() * 10000000) % len(self.slowCoreString), fastTemp)
        # shuffle the fastCoreString and slowCoreString
        random.shuffle(self.fastCoreString)
        random.shuffle(self.slowCoreString)

    def geneticCrossover(self, individual_1, individual_2):
        self.setFastCoreString(individual_1.fastCoreString)
        self.setSlowCoreString(individual_1.slowCoreString)

        changeDetected = False
        for i in range(len(self.fastCoreString)):
            for x in range(len(individual_2.slowCoreString)):
                if self.fastCoreString[i] == individual_2.slowCoreString[x]:
                    changeDetected = True
                    del self.fastCoreString[i]
                    if x >= len(self.slowCoreString):
                        self.slowCoreString.insert(len(self.slowCoreString), individual_2.slowCoreString[x])
                    else:
                        self.slowCoreString.insert(x, individual_2.slowCoreString[x])
                    break
            if changeDetected == True:
                break

        changeDetected = False
        for i in range(len(self.slowCoreString)):
            for x in range(len(individual_2.fastCoreString)):
                if self.slowCoreString[i] == individual_2.fastCoreString[x]:
                    changeDetected = True
                    del self.slowCoreString[i]
                    if x >= len(self.fastCoreString):
                        self.fastCoreString.insert(len(self.fastCoreString), individual_2.fastCoreString[x])
                    else:
                        self.fastCoreString.insert(x, individual_2.fastCoreString[x])
                    break
            if changeDetected == True:
                break

if __name__ == '__main__':
    person = Individual()
    fastCoreString = []
    slowCoreString = []

    for i in range(10):
        fastCoreString.append((i, i))
    person.setFastCoreString(fastCoreString)
    for i in range(10, 15):
        slowCoreString.append((i, i))
    person.setSlowCoreString(slowCoreString)

    # Individual Class Tests:
    print(person.getFastCoreString())
    print(person.getSlowCoreString())
    print(person.getAvgWaitTime())
    print(person.getTotalRunTime())
    print(person.getFitness())
    person.mutate()
    print(person.getFastCoreString())
    print(person.getSlowCoreString())

    # Individual Class Helper Function Tests:
    person1 = Individual()
    fastCoreString = []
    slowCoreString = []
    newPerson = Individual()

    for i in range(10):
        fastCoreString.append((i, i))
    person1.setFastCoreString(fastCoreString)
    for i in range(10, 15):
        slowCoreString.append((i, i))
    person1.setSlowCoreString(slowCoreString)

    newPerson.geneticCrossover(person, person1)
