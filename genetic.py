"""Simple genetic algorithm (with Claude help)"""
"""Assuming each letter is 162 characters (max) long"""

import random
import string

class GeneticAlgorithm:
    def __init__(self, 
                 population_size = 100,
                 mutation_rate = 0.01,
                 elite_size = 2):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size
        self.valid_chars = list(string.ascii_letters + '.!?')
        
    def create_individual(self):
        return ''.join(random.choice(self.valid_chars) for _ in range(162))
    
    def initialize_population(self):
        return [self.create_individual() for _ in range(self.population_size)]
    
    def mutate(self, individual):
        chars = list(individual)
        for i in range(len(chars)):
            if random.random() < self.mutation_rate:
                chars[i] = random.choice(self.valid_chars)
        return ''.join(chars)
    
    def crossover(self, parent1, parent2):
        child = ''
        for p1, p2 in zip(parent1, parent2):
            child += p1 if random.random() < 0.5 else p2
        return child
    
    def select_parent(self, population, scores):
        tournament_size = 3
        tournament = random.sample(list(enumerate(population)), tournament_size)
        winner = max(tournament, key=lambda x: scores[x[0]])
        return winner[1]
    
    def evolve(self, get_score, generations = 1000):
        population = self.initialize_population()
        best_individual = None
        best_score = float('-inf')
        
        for generation in range(generations):
            scores = [get_score(ind) for ind in population]
            
            current_best = max(scores)
            if current_best > best_score:
                best_score = current_best
                best_individual = population[scores.index(current_best)]
                # print(f"Generation {generation}: New best score = {best_score}")
            
            pop_sorted = [x for _, x in sorted(zip(scores, population), 
                                             key=lambda pair: pair[0],
                                             reverse=True)]
            
            new_population = pop_sorted[:self.elite_size]
            
            while len(new_population) < self.population_size:
                parent1 = self.select_parent(population, scores)
                parent2 = self.select_parent(population, scores)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            
            population = new_population
            if generation % (generations // 10) == 0:
                print(f'Best score: {best_score} (Generation {generation}/{generations})')
        return best_individual, best_score