from graph import catalog_from_file
import trajet_truck 
from realistic_solution import knapsack_greedy_realistic, cost_traject_realistic

c = catalog_from_file(data_path + "input/trucks.0.in")
print(len(c))
print(c)

B = 25*10**9


result = trajet_truck.knapsack_greedy(3,1, 25*10**9)
print(result[0]) 

print(trajet_truck.knapsack_hill_climbing(3,1, B)[0])
