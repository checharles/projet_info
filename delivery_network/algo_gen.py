from graph import Graph, graph_from_file, catalog_from_file
import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
from statistics import mean

data_path = "/home/onyxia/projet_info/input/"

"""the budget, which is a contraint"""
B = 25*10**9


def cost_traject_gen(nb_road, nb_truck):
    """this function define the value of a travel and  the cost of the truck to use it

    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file

    Outputs
    -----------
    utility : dictionnary
        Utility is dictionnary, which key are the number of the road. It gets the value of the road and the cost 
        of the truck to use it. the list is (value, cost of ten rauck, model of the truck, ratio cost/profit)

    nb_travel : int
        the number of possible traject
    """

    time_road = f"route.{nb_road}.out"
    truck_model = f"trucks.{nb_truck}.in"
    route_name = f"routes.{nb_road}.in"

    cost_and_power_truck = catalog_from_file(data_path + truck_model)
    
    """Creation of the weight and value list"""
    value = list()
    weight = list()
  
    with open(data_path + route_name, 'r') as f:
        nb_travel = int(f.readline())
        content = f.readlines()
        for line in content:
            value.append(float(line.split()[2]))

    with open(data_path + time_road, 'r') as f:
        
        content = f.readlines()
        for line in content:
            i = 0 
            min_power = float(line.split()[0])
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            weight.append(cost_travel)

    return value, weight, nb_travel



def cal_fitness(weight, value, population, B):
    fitness = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        S1 = np.sum(population[i] * value)
        S2 = np.sum(population[i] * weight)
        if S2 <= B:
            fitness[i] = S1
        else :
            fitness[i] = 0 
    return fitness.astype(int) 



def selection(fitness, num_parents, population):
    fitness = list(fitness)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        parents[i,:] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return parents



def crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1]/2)
    crossover_rate = 0.5
    i=0
    while (parents.shape[0] < num_offsprings):
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
        offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
        i=+1
    return offsprings 
    
def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = 0.1
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i,:] = offsprings[i,:]
        if random_value > mutation_rate:
            continue
        int_random_value = randint(0,offsprings.shape[1]-1)    
        if mutants[i,int_random_value] == 0 :
            mutants[i,int_random_value] = 1
        else :
            mutants[i,int_random_value] = 0
    return mutants   

def GA_KP(weight, value, population, pop_size, num_generations, B):

    

    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    num_offsprings = pop_size[0] - num_parents 
    for i in range(num_generations):
        fitness = cal_fitness(weight, value, population, B)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossover(parents, num_offsprings)
        mutants = mutation(offsprings)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants
        
        #print('Last generation: \n{}\n'.format(population)) 
        fitness_last_gen = cal_fitness(weight, value, population, B)      
        #print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
        max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
        parameters.append(population[max_fitness[0][0],:])
        return parameters, fitness_history


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################


value, weight, nb_travel = cost_traject(2, 2)
item_number = np.arange(1,nb_travel + 1)

solutions_per_pop = 1000

"""initilisation de la pop"""

pop_size = (solutions_per_pop, nb_travel)
print('Population size = {}'.format(pop_size))
result = list()
total_value  = 0
initial_population = np.random.randint(2, size = pop_size)
initial_population = initial_population.astype(int)
num_generations = 100
total_weight = 0
parameters, fitness_history = GA_KP(weight, value, initial_population, pop_size, num_generations,B)
#print('The optimized parameters for the given inputs are: \n{}'.format(parameters))
selected_items = item_number * parameters
for i in range(selected_items.shape[1]):
    if selected_items[0][i] != 0:
        result.append(item_number[i])
        total_value = total_value + value[i]
        total_weight = total_weight + weight[i]
#print(result)
print(total_value)
a = 100*total_weight/B
print(a)