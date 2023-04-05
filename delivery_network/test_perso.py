from graph import catalog_from_file
import trajet_truck 
from realistic_solution import knapsack_greedy_realistic, cost_traject_realistic
data_path = "/home/onyxia/projet_info/"
c = catalog_from_file(data_path + "input/trucks.0.in")
print(len(c))
print(c)

B = 25*10**9







print("a")
result = trajet_truck.knapsack_greedy(1, 2, 25*10**9)
print(result[0])
print(result[3])
#print(trajet_truck.knapsack_dynamic_programming(1, 1, B))

print(100*result[4]/(25*10**9))
print((trajet_truck.knapsack_greedy_local_search_random(1, 2, B, 10))[0])





#print((trajet_truck.knapsack_greedy_local_search_random(1, 2, B, 10))[0])

"""
#print(trajet_truck.knapsack_greedy_local_search(2, 0, 25*10**9, max_iterations=1)[0])
print(trajet_truck.knapsack_dynamic_programming(1, 1, B))
print((trajet_truck.knapsack_greedy_local_search_random(2, 1, B, 10))[0])
#print((trajet_truck.knapsack_greedy_local_search_smart(2, 1, B, 10))[0])
#print(knapsack_greedy_realistic(1, 1, B)[0])
print("a")
#print(trajet_truck.knapsack_heuristic(2, 2, B, max_iter=10))



print(trajet_truck.knapsack_heuristic(2, 1, B, max_iter=1))
print("b")
"""