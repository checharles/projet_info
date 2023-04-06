from graph import catalog_from_file
import trajet_truck 
from realistic_solution import knapsack_greedy_realistic, cost_traject_realistic



B = 25*10**9


result = trajet_truck.knapsack_greedy(1,1, 25*10**9)
print(result[0]) 
print(result[3])

print(trajet_truck.knapsack_hill_climbing(1,1, B)[0])
