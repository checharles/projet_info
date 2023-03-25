from graph import catalog_from_file
import trajet_truck 
from realistic_solution import knapsack_greedy_realistic, cost_traject_realistic
data_path = "/home/onyxia/projet_info/"
c = catalog_from_file(data_path + "input/trucks.2.in")
print(len(c))

B = 25*10**9

#print(trajet_truck.knapsack(2, 2, B))


print(trajet_truck.knapsack_greedy(3, 2, B)[0])
print(knapsack_greedy_realistic(3, 2, B)[0])
print("a")
#print(trajet_truck.knapsack_heuristic(2, 2, B, max_iter=10))



"""print(trajet_truck.knapsack_heuristic(2, 1, B, max_iter=1))"""
print("b")
