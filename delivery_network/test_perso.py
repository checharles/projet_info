from graph import catalog_from_file
import trajet_truck 
from realistic_solution import knapsack_greedy_realistic, cost_traject_realistic
data_path = "/home/onyxia/projet_info/"
c = catalog_from_file(data_path + "input/trucks.0.in")
print(len(c))
print(c)

B = 25*10**9

print("a")
print(trajet_truck.knapsack_greedy(10, 2, 25*10**9)[0])
print(trajet_truck.knapsack_greedy(10, 2, 25*10**9)[2])

print(trajet_truck.knapsack_greedy(10, 2, 25*10**9)[3]/(25*10**9))

#print(knapsack_greedy_realistic(1, 1, B)[0])
print("a")
#print(trajet_truck.knapsack_heuristic(2, 2, B, max_iter=10))



"""print(trajet_truck.knapsack_heuristic(2, 1, B, max_iter=1))"""
print("b")
