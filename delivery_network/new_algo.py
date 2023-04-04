import sys
sys.path.append("/opt/mamba/lib/python3.10/site-packages")
import numpy as np
import pandas as pd
import random 
from random import randint
import matplotlib.pyplot as plt
from statistics import mean

sys.path.pop()
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import Graph, graph_from_file, catalog_from_file
import trajet_truck

data_path = "/home/onyxia/projet_info/input/"

"""the budget, which is a contraint"""

B = 25*10**9


def cost_traject_gen(nb_road, nb_truck):
	"""
    This function defines the value of a travel and the cost of the truck to use it

    Parameters:
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file

    Outputs:
    -----------
    utility : dictionary
        Utility is a dictionary, whose keys are the number of the road. It gets the value of the road and the cost 
        of the truck to use it. The list is (value, cost of ten trucks, model of the truck, ratio cost/profit)

    nb_travel : int
        the number of possible traject
	"""

	time_road = f"route.{nb_road}.out"
	truck_model = f"trucks.{nb_truck}.in"
	route_name = f"routes.{nb_road}.in"

	cost_and_power_truck = catalog_from_file(data_path + truck_model)
    
	# Creation of the weight and value list

	value = []
	weight = []
	list_travels = []
	list_travel = {}

	with open(data_path + route_name, 'r') as f:
		nb_travel = int(f.readline())
		content = f.readlines()
		for line in content:
			value.append(float(line.split()[2]))
			list_travels.append((int(line.split()[0]), float(line.split()[1])))

	with open(data_path + time_road, 'r') as f:
        
		content = f.readlines()
		key_travel = 0
		for line in content:
			i = 0 
			min_power = float(line.split()[0])
			while cost_and_power_truck[i][0] < min_power:
				i = i+1
        
			cost_travel = cost_and_power_truck[i][1]
			weight.append(cost_travel)
			list_travel[key_travel] = (list_travels[key_travel], i+1)
			key_travel = key_travel + 1

	return value, weight, nb_travel, list_travels

def close_solution_with_greedy(nb_road, nb_truck,nb_travel, B) :
	_,allocation, _, _, _ = trajet_truck.knapsack_greedy(nb_road, nb_truck, B)

	individu = [0]*nb_travel
	for travel in allocation : 
		individu[travel[2] - 1] = 1
	
	return individu

def generate_population(nb_road, nb_truck, size, nb_travel, B):
	population = []
	nb_super_individu = int(0.2*size)
	for individu in range(size - 1- nb_super_individu):
		genes = [0,0,0,0,1]
		chromosome = []
		for i in range(nb_travel):
			chromosome.append(random.choice(genes))

		population.append(chromosome)
	fat_individu = [1] * nb_travel
	population.append(fat_individu)
	super_individu = close_solution_with_greedy(nb_road, nb_truck, nb_travel, B)
	for i in range(nb_super_individu): 
		population.append(super_individu)

	print("Generated a random population of size", size)
	return population

def calculate_fitness(chromosome, weight, value, B):
	total_weight = 0
	total_value = 0
	for i in range(len(chromosome)):
		if chromosome[i] == 1:
			total_weight += weight[i]
			total_value += value[i]
	if total_weight > B:
		return 0
	else:
		return total_value

def probability_reproduction(population, weight, value, B) : 
	fitness_values = []
	for parent in population:
		fitness_values.append(calculate_fitness(parent, weight, value, B))
	
	fitness_values = [float(i)/(sum(fitness_values)) for i in fitness_values]
	return fitness_values

def select_parent(population, fitness_values):
	
	parent1 = random.choices(population, weights=fitness_values, k=1)[0]
	parent2 = random.choices(population, weights=fitness_values, k=1)[0]
	
	return parent1, parent2

def crossover(parent1, parent2, nb_travel):
	crossover_point = random.randint(0, nb_travel -1)
	child1 = parent1[0:crossover_point] + parent2[crossover_point:]
	child2 = parent2[0:crossover_point] + parent1[crossover_point:]
	
	return child1, child2

def mutate(child, mutation_probabilty, nb_travel):
    for i in range (int(mutation_probabilty*nb_travel)):
        mutation_point = random.randint(0, nb_travel-1)
        if child[mutation_point] == 0:
            child[mutation_point] = 1
        else:
            child[mutation_point] = 0
    return child

def selection_elitist(population, fitness_values, n_elites):
	# Sort the population and fitness_values lists by fitness value in descending order
	sorted_population = [x for _, x in sorted(zip(fitness_values, population), reverse=True)]
	sorted_fitness = sorted(fitness_values, reverse=True)
	# Select the n_elites best chromosomes
	elites = sorted_population[:n_elites]
	
	return elites

def	remplacement(population, fitness_values, n_elites, elites): 
	sorted_population = [x for _, x in sorted(zip(fitness_values, population), reverse=True)]
	population[-n_elites:] = elites
	# Return the updated population
	return population

def get_best(population,weight,value,B):
	fitness_values = []
	for individu in population:
		fitness_values.append(calculate_fitness(individu, weight, value, B))

	max_value = max(fitness_values)
	max_index = fitness_values.index(max_value)
	return population[max_index]

def simulation(nb_road, nb_truck, size_population, mutation_probability, number_generation, percentage_elitism, B):

	print("the search has begun")
	value, weight, nb_travel, list_travel = cost_traject_gen(nb_road, nb_truck)
	
	n_elites = int(nb_travel*percentage_elitism)
	population = generate_population(nb_road, nb_truck, size_population, nb_travel, B)



	for generation in range(number_generation):
		print("une nouvelle génération a commencé")
		fitness_values = probability_reproduction(population, weight, value, B)
		elites = selection_elitist(population, fitness_values, n_elites)
		new_population = []

		for child in range(size_population//2): 
			
			parent1, parent2 = select_parent(population, fitness_values)
			
			child1, child2 = crossover(parent1, parent2, nb_travel)
			new_population.append(child2)

			child1 = mutate(child1, mutation_probability, nb_travel)

			new_population.append(child1)
			
		

		
		fitness_values = probability_reproduction(new_population, weight, value, B)
		population = grand_remplacement(new_population, fitness_values, n_elites, elites)
		the_chosen_one = get_best(population, weight, value, B)
		
			
	total_value = 0
	total_weight = 0
	
	allocation	 = []
	nb_travels = 0
	for i in range(nb_travel):
		if the_chosen_one[i] == 1:
			total_value += the_chosen_one[i]*value[i]
			total_weight += the_chosen_one[i]*weight[i]
			allocation.append(list_travel[i])
			nb_travels += 1
	return total_value, allocation, nb_travels, total_weight



B = 25*10**9

result = simulation(3, 2, 100, 0.01, 100, 0.01, B)
result_control = trajet_truck.knapsack_greedy(3	, 2, B)
print(result[0])
print(result_control[0])
print(result[2])
print(result_control[3])
print(100*result[3]/B)
print(100*result_control[4]/B)
print("a")








