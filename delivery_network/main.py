"""It is an illustration  of the class graph and its methods"""
import os
os.chdir('/home/onyxia/projet_info/result')
print(os.getcwd())

import sys

sys.path.append("/opt/mamba/lib/python3.10/site-packages")
import graphviz 

sys.path.pop()
sys.path.append("/home/onyxia/projet_info/delivery_network")
from graph import Graph, graph_from_file




data_path = "/home/onyxia/projet_info/input/"
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

Graph.display_graph(g_mst)
Graph.display_path(g_mst, 11, 6)

