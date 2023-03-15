"""this script allow to display a graph and a path with the graph"""
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
file_name = "network.05.in"

g = graph_from_file(data_path + file_name)
g  = Graph.kruskal(g)

Graph.display_graph(g)
