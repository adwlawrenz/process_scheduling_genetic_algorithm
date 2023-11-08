# Optimizing Process Scheduling with a Genetic Algorithm

## Idea/Abstract:
> Since the inception of central processing units (CPU), operating systems (OS) have used many different implementations of process scheduling algorithms, which each seek to improve the performance and efficiency of task execution. With the new modern standard of CPU’s consisting of multiple cores with varying performance benefits, this problem is becoming harder than ever to solve. This study does not attempt to solve this problem for a specific real-life system, but it does try to show that genetic algorithms (GA) could be used to optimize task scheduling for multicore systems in general. Optimization in the study is based on the total run time and average wait time of the processes. The GA implementation shows promising results in these categories, when compared against other scheduling algorithms like FCFS and SJF. 

## Introduction to Process Scheduling and Genetic Algorithms
>Task/process scheduling plays a significant factor in the overall performance of a computer system. Proper or optimal scheduling allows for tasks to be completed in a timely manner, where both the total run time of a set of processes is low and the average wait time per process in that set is low. Decreasing these time based factors allows for higher throughput in the system and shorter wait times for task execution. Task scheduling is usually carried out by the OS, so different OS’s will have varying scheduling algorithms. There are several existing algorithms out there, and the most well known are first come first serve (FCFS) and shortest job first (SJF). SJF uses a heuristic that gives execution priority to the shortest tasks in the queue. Whereas, FCFS’s heuristic assigns execution priority according to when the task entered the process queue. These algorithms both have their benefits. SJF has the shortest average wait time for tasks out of all non-preemptive scheduling algorithms. And, FCFS allows for sequential task execution, meaning tasks are run in the order that they arrive at the CPU. Unfortunately though, neither of them can optimize for multicore systems. For traditional single core CPU’s, task scheduling only has to consider what process to run next on the single core. But, for multicore CPU’s, task scheduling is concerned with what process to run next and which core to run it on. In this study, the simulated computer system in question has a two-core processor with one efficiency core and one performance core. The performance core runs 20 percent faster than that of the efficiency core. This is similar to many new CPU’s on the market, which include distinct cores with differing execution speeds. Because of this difference in core performance, it must be noted that the total runtime of a set of processes could be optimized/significantly reduced by allocating certain processes to certain cores. 
> Genetic algorithms, if not known, mimic that of a biological system with a unique survival of the fittest/natural selection type heuristic guiding the outcome of the system. Because of this, they serve as a great way of finding solutions to optimization problems. And, for that reason, a GA is used to solve the problem discussed in this paper. Similar to the processes of evolution, genetic algorithms include individuals with genetic representations/genotypes, and these genotypes are manipulated upon. Over multiple generations of these manipulations and selections of only desired individuals, the genes of individuals in later generations start to converge on more desired representations. This study is concerned with the non-preemptive scheduling of 15 different processes on the two core system mentioned above. In the case of my GA, individuals in each generation are represented by certain orderings of these 15 processes on the two cores of the system. Individuals/orderings with a lower total runtime and average process wait time will be selected to move onto the next generation. Genetic manipulations on these individuals will consist of changing the ordering of processes and altering which CPU core they run on. More information on the implementation of this genetic algorithm and its methods will be provided in subsequent sections.

## Approach and Implementation:

> The first thing to decide when implementing a GA is how individuals in the population will be represented; what will their genotype look like? For my GA, each individual in the population has two strings of “DNA”. The first string is an ordered list of the processes to be run on the 20% faster performance core, and the second string is an ordered list of the processes to be run on the slower efficiency core. Because there are only 15 processes in question, the max amount of processes that either of the two strings can have is 10. Each of the 15 processes must exist in one of the strings and may not be listed more than once. Each generation of the population is made up of 20 individuals. All individuals in the initial population have a randomly generated ordering of the processes in their two strings.

> For every generation after the initial, individuals for that generation are chosen or created using three differing techniques: fitness selection, genetic crossover, and mutation. The five individuals with the lowest/best fitness score from the previous generation are automatically selected to move onto the next generation. A fitness score is a heuristic that serves to measure how well an individual meets the system’s intended goal. For this problem, I use the fitness function (1) below:

>> Fitness(X) = ((i = 115Wi)15)+T
>>> X is some individual, Wi is the waiting time of some process i that exists in the 15 total processes, and T is the total runtime of all the processes. The left hand side of the sum represents the average waiting time for each process.

> The five individuals originally chosen for the next generation perform a genetic crossover with one another, which creates ten more individuals for the same generation. Genetic crossover is similar to that of sexual reproduction in the real world. Two individuals pair up and perform a genetic crossover. The result is a new individual with an amalgamation of the two involved individuals’ genotypes, or strings in this case. A genetic crossover for my GA, happens as is shown in the steps shown below:

>> Step 1: Assume that individual X’s string is used initially as the new individual’s string. If there exists a process in individual X’s fast core string that is a process in individual Y’s slow core string, then move that process into the slow core string of the new individual; only do this for one such process though. The process being moved from the fast core string to the slow core string is placed at the same index in the slow core string as it was in the fast core string. If that index does not exist in the slow core string, the process is simply moved to the end of the slow core string.
>>> Individual X:
>>>String for fast core: [0, 1, 3, 5, 6, 10, 12, 11, 14]
>>>String for slow core: [2, 4, 7, 9, 8, 13]
>>>Individual Y:
>>>String for fast core: [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 14]
>>>String for slow core: [9, 7, 11, 13]
>>>New Individual Z From Step 1:
>>>String for fast core: [0, 1, 3, 5, 6, 10, 12, 14]
>>>String for slow core: [2, 4, 7, 9, 8, 13, 11]

>> Step 2: Assume the new individual’s string is now the resulting string from step 1. If there exists a process in individual X’s slow core string that is a process in individual Y’s fast core string, then move that process into the fast core string of the new individual; only do this for one such process though. The process being moved from the slow core string to the fast core string is placed at the same index in the fast core string as it was in the slow core string. If that index does not exist in the fast core string, the process is simply moved to the end of the fast core string.
>>>Individual X:
>>>String for fast core: [0, 1, 3, 5, 6, 10, 12, 11, 14]
>>>String for slow core: [2, 4, 7, 9, 8, 13]
>>>Individual Y:
>>>String for fast core: [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 14]
>>>String for slow core: [9, 7, 11, 13]
>>>New Individual Z From Step 2:
>>>String for fast core: [0, 1, 2, 3, 5, 6, 10, 12, 14]
>>>String for slow core: [4, 7, 9, 8, 13, 11]

> The last five individuals included in the new generation have the same genotypes as the original five individuals that are selected from the prior generation, but their genotypes have random mutations in their strings. Each mutation takes place like so:

>>Step 1: Pick an occupied index in the fast core string of Individual X at random, move the process at that index into the slow core string at some random index.
>>>Individual X From Original 5:
>>>String for fast core: [0, 1, 2, 3, 5, 6, 10, 12, 14]
>>>String for slow core: [9, 7, 11, 13, 4, 8]
>>>Mutated Version of Individual X:
>>>String for fast core: [0, 1, 2, 3, 5, 10, 12, 14]
>>>String for slow core: [9, 7, 11, 13, 4, 6, 8]

>> Step 2: Pick an occupied index in the slow core string of Individual X at random, move the process at that index into the fast core string at some random index.
>>>Individual X From Original 5:
>>>String for fast core: [0, 1, 2, 3, 5, 10, 12, 14]
>>>String for slow core: [9, 7, 11, 13, 4, 6, 8]
>>>Mutated Version of Individual X:
>>>String for fast core: [0, 1, 2, 7, 3, 5, 10, 12, 14]
>>>String for slow core: [9, 11, 13, 4, 6, 8]

>> Step 3: Assume that we are now mutating on the genotype from step 2. Randomly shuffle the ordering of the elements in both the fast core and slow core strings.
>>>Mutated Version From Step 2:
>>>String for fast core: [0, 1, 2, 7, 3, 5, 10, 12, 14]
>>>String for slow core: [9, 11, 13, 4, 6, 8]
>>>Mutated Version From Step 3:
>>>String for fast core: [14, 7, 10, 3, 0, 1, 5, 2, 12]
>>>String for slow core: [8, 4, 9, 11, 6, 13]

> These genetic manipulations of mutation and crossover, along with the fitness function allow for the implementation of the actual genetic algorithm. The functions for the mutation and crossover are not shown, because they are described in depth above.

## Running the Algorithm:
> Running the GeneticAlgorithm.py script creates 3 different test cases, each with a random list of 15 processes to schedule on a "CPU". Each of these test cases are run on the genetic algorithm with 10000  generations. The technical results, such as the average wait time and the total run time, of the genetic algorithm's optimized process schedule are printed out alongside the results of the standard Shortest Job First and First Come First Serve process schedule algorithms for comparison. 

> command: python3 GeneticAlgorithm.py 
