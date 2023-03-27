// Created with help of ChatGPT

import random
import matplotlib.pyplot as plt

# Define the number of chromosomes in the population
POPULATION_SIZE = 100

# Define the length of each chromosome (number of genes)
CHROMOSOME_LENGTH = 10

# Define the maximum number of generations to run the algorithm
MAX_GENERATIONS = 100

# Define the probability of a mutation occurring
MUTATION_PROBABILITY = 0.01

# Define the fitness function to be optimized (in this example, we will maximize a function that takes a list of floats as input)
def fitness_function(genes):
    return sum(genes)

# Generate a random float between min and max
def random_float(min, max):
    return random.uniform(min, max)

# Generate a random chromosome with genes between min and max
def generate_chromosome(min, max):
    return [random_float(min, max) for i in range(CHROMOSOME_LENGTH)]

# Generate a population of random chromosomes
def generate_population(min, max):
    return [generate_chromosome(min, max) for i in range(POPULATION_SIZE)]

# Select two parents from the population using tournament selection
def tournament_selection(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    while parent1 == parent2:
        parent2 = random.choice(population)
    return parent1, parent2

# Perform crossover on two parent chromosomes to create two child chromosomes
def crossover(parent1, parent2):
    crossover_point = random.randint(0, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Perform mutation on a chromosome by randomly changing one of its genes
def mutation(chromosome, min, max):
    if random.random() < MUTATION_PROBABILITY:
        index = random.randint(0, CHROMOSOME_LENGTH - 1)
        chromosome[index] = random_float(min, max)

# Run the genetic algorithm and return the best chromosome
def run_genetic_algorithm(min, max):
    population = generate_population(min, max)
    best_fitnesses = []
    for i in range(MAX_GENERATIONS):
        parents = [tournament_selection(population) for i in range(POPULATION_SIZE // 2)]
        children = [crossover(parent1, parent2) for parent1, parent2 in parents]
        population = [child1 + child2 for child1, child2 in children]
        for chromosome in population:
            mutation(chromosome, min, max)
        fitnesses = [fitness_function(chromosome) for chromosome in population]
        best_fitness = max(fitnesses)
        best_fitnesses.append(best_fitness)
    best_chromosome = population[fitnesses.index(best_fitness)]
    return best_chromosome, best_fitnesses

# Run the genetic algorithm and plot the results
best_chromosome, best_fitnesses = run_genetic_algorithm(0, 1)
plt.plot(best_fitnesses)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()
