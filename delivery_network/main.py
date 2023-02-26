from graph import Graph

data_path = "/home/onyxia/projet_info/input/"
file_name = "network.04.in"
g = Graph.graph_from_file(data_path + file_name)
print(g)
print(Graph.connected_components(g))
print(Graph.get_path_with_power(g, 1,2, 5))
print(Graph.min_power(g, 1, 3))
print(Graph.kruskal(g))