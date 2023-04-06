"""It is an illustration  of the class graph and its methods"""
"""definition of the input file"""
import os
os.chdir('/home/onyxia/projet_info/result/graph_display')
print(os.getcwd())

import sys

sys.path.append("/opt/mamba/lib/python3.10/site-packages")
import graphviz 

sys.path.pop()
sys.path.append("/home/onyxia/projet_info/delivery_network/")
from graph import Graph, graph_from_file
import trajet_truck
import algo_gen
import realistic_solution

data_path = "/home/onyxia/projet_info/input/network_importation/"
file_name = "network.1.in"
g = graph_from_file(data_path + file_name)

print(g)

print(Graph.connected_components_set(g))

print(Graph.get_path_with_power(g, 6, 11, 1000))
print(Graph.get_path_with_power(g, 6, 11, 2))

print(Graph.min_power(g, 1, 2)[0])


g_mst = Graph.kruskal(g)
print(g_mst)

print(Graph.min_power_greedy(g_mst, 6, 11))
print("a")
print(Graph.search_parent(g_mst))
depths, parents = Graph.search_parent(g_mst)
print(Graph.find_path(parents, depths, 11, 6))
print(parents)
print(Graph.find_path_with_distance(parents, depths, 13, 20))

Graph.display_graph(g_mst,)
Graph.display_path(g_mst, 11 , 6)

B  = 25*10*10*9
print(trajet_truck.knapsack_dynamic_programming(1, 1, B))
print(trajet_truck.knapsack_greedy(1, 1, B))
print(trajet_truck.knapsack_hill_climbing(1, 1, B))
print(algo_gen.simulation(1, 1, 100, 0.1, 50, 0.1, B))
print(realistic_solution. )



