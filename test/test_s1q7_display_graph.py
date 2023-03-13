"""this script allow to display a graph and a path with the grapph"""


import graphviz 
from graph import Graph, graph_from_file


data_path = "/home/onyxia/projet_info/input/"
file_name = "network.04.in"

g = graph_from_file(data_path + file_name)


Graph.display_graph(g)
Graph.display_path(g, 1, 3)