from graph import Graph, graph_from_file
#import graphviz

data_path = "/home/onyxia/projet_info/input/"
file_name = "network.04.in"
g = graph_from_file(data_path + file_name)
print(g)
print(Graph.connected_components_set(g))
#print(Graph.get_path_with_power(g, 1, 2, 1000))
#print(Graph.min_power(g, 1, 2)[0])


print(Graph.kruskal(g))

#print(Graph.min_power_greedy(g, 1, 3))


Graph.display_graph(g)
Graph.display_path(g, 1, 3)
