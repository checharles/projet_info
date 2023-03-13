import graphviz
from graph import Graph, graph_from_file
import time


data_path = "/home/onyxia/projet_info/input/"
file_name = "network.02.in"
g = graph_from_file(data_path + file_name)

#print(g)


#print(g)
#print(Graph.connected_components_set(g))
#print(Graph.get_path_with_power(g, 1, 2, 1000))
#print(Graph.min_power(g, 1, 2)[0])
"""
print("a")
g_mst = Graph.kruskal(g)

start_time = time.perf_counter()

print(Graph.min_power_greedy(g_mst, 37816, 77493))
#print(Graph.min_power_greedy(g_mst, 6, 11))
end_time = time.perf_counter()

time = (end_time - start_time)
print(time)"""
Graph.display_graph(g)
Graph.display_path(g, 1, 3)
