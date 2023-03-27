// Created with help of ChatGPT

#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

// Define the number of chromosomes in the population
const int POPULATION_SIZE = 100;

// Define the length of each chromosome (number of genes)
const int CHROMOSOME_LENGTH = 10;

// Define the maximum number of generations to run the algorithm
const int MAX_GENERATIONS = 100;

// Define the probability of a mutation occurring
const double MUTATION_PROBABILITY = 0.01;

// Define the fitness function to be optimized (in this example, we will maximize a function that takes a vector of doubles as input)
double fitness_function(std::vector<double> genes)
{
    double sum = 0;
    for (double x : genes) {
        sum += x;
    }
    return sum;
}

// Define a chromosome as a vector of genes (doubles)
typedef std::vector<double> chromosome;

// Define a population as a vector of chromosomes
typedef std::vector<chromosome> population;

// Generate a random double between min and max
double random_double(double min, double max)
{
    static std::default_random_engine generator(std::chrono::system_clock::now().time_since_epoch().count());
    std::uniform_real_distribution<double> distribution(min, max);
    return distribution(generator);
}

// Generate a random chromosome with genes between min and max
chromosome generate_chromosome(double min, double max)
{
    chromosome c;
    for (int i = 0; i < CHROMOSOME_LENGTH; i++) {
        c.push_back(random_double(min, max));
    }
    return c;
}

// Generate a population of random chromosomes
population generate_population(double min, double max)
{
    population p;
    for (int i = 0; i < POPULATION_SIZE; i++) {
        p.push_back(generate_chromosome(min, max));
    }
    return p;
}

// Calculate the fitness of each chromosome in the population and return the best chromosome
chromosome get_best_chromosome(population& p)
{
    double best_fitness = -1;
    chromosome best_chromosome;
    for (chromosome& c : p) {
        double fitness = fitness_function(c);
        if (fitness > best_fitness) {
            best_fitness = fitness;
            best_chromosome = c;
        }
    }
    return best_chromosome;
}

// Select two parents from the population using tournament selection
void tournament_selection(population& p, chromosome& parent1, chromosome& parent2)
{
    static std::default_random_engine generator(std::chrono::system_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> distribution(0, POPULATION_SIZE - 1);
    parent1 = p[distribution(generator)];
    parent2 = p[distribution(generator)];
    while (parent1 == parent2) {
        parent2 = p[distribution(generator)];
    }
}

// Perform crossover on two parent chromosomes to create two child chromosomes
void crossover(chromosome& parent1, chromosome& parent2, chromosome& child1, chromosome& child2)
{
    static std::default_random_engine generator(std::chrono::system_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> distribution(0, CHROMOSOME_LENGTH - 1);
    int crossover_point = distribution(generator);
    for (int i = 0; i < CHROMOSOME_LENGTH; i++) {
        if (i < crossover_point) {
            child1[i] = parent1[i];
            child2[i] = parent2[i];
       
