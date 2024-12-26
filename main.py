from genetic import GeneticAlgorithm
from scoring import get_letter_score

if __name__ == "__main__":
    ga = GeneticAlgorithm(
        population_size=100,
        mutation_rate=0.01,
        elite_size=2
    )
    
    best_solution, best_fitness = ga.evolve(get_letter_score, generations=10000)
    print(f'Best letter: {best_solution}')
    print(f'Best score: {best_fitness}')