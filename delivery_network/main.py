from graph import Graph
import graphviz

data_path = "/home/onyxia/projet_info/input/"
file_name = "network.01.in"
g = Graph.graph_from_file(data_path + file_name)
print(g)
print(Graph.connected_components(g))
print(Graph.get_path_with_power(g, 1, 4, 1000))
print(Graph.min_power(g, 1, 4))

print('a')
Graph.display_graph(g)
print('a')
"""print('1')
print(Graph.kruskal(g))
print('2')
print(Graph.min_power_greedy(g, 1, 3))"""

