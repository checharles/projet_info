"""this file contains a programm creating the file needed for the realistic_solution programm"""


"""importation and creation of the outputfile"""
from statistics import mean
from graph import Graph, graph_from_file, catalog_from_file
data_path = "/home/onyxia/projet_info/input/network_importation/"
import sys 
sys.path.pop()
sys.path.append("/home/onyxia/projet_info/delivery_network/")


"""opening each file and calcuting the time """


for  i in range(1,11): 

    file_name = f"network.{i}.in"
    route_name = f"routes.{i}.in"
    power_road = f"routes_power.{i}.out"
    dist_road = f"route_dist.{i}.out"
    ratio_road = f"route_ratio.{i}.out"
    edge_road = f"route_edge.{i}.out"

    g = graph_from_file(data_path + file_name)

    


    g_mst_dist = Graph.kruskal_dist(g)

    depths, parents = Graph.search_parent(g_mst_dist)

    with open(data_path + dist_road, 'w') as f:
        with open(data_path + route_name, 'r') as file: 
            nb_travel = int(file.readline())
            content = file.readlines()
              

            for line in content :
                src = int(line.split()[0])
                dest = int(line.split()[1])
                a = Graph.find_path_with_distance(parents, depths, src, dest)[1]
                b = len(Graph.find_path_with_distance(parents, depths, src, dest)[0])
                c = Graph.find_path_with_distance(parents, depths, src, dest)[2]
                f.write(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')

        
    g_mst_ratio = Graph.kruskal_ratio(g)

    depths, parents = Graph.search_parent(g_mst_ratio)

        
    with open(data_path + ratio_road, 'w') as f:
        with open(data_path + route_name, 'r') as file: 
            nb_travel = int(file.readline())
            print("il y a ", nb_travel, "trajets")
            content = file.readlines()
                

            for line in content :
                src = int(line.split()[0])
                dest = int(line.split()[1])
                a = Graph.find_path_with_distance(parents, depths, src, dest)[1]
                b = len(Graph.find_path_with_distance(parents, depths, src, dest)[0])
                c = Graph.find_path_with_distance(parents, depths, src, dest)[2]
                f.write(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')

    g_mst_edge = Graph.kruskal_edge(g)

    depths, parents = Graph.search_parent(g_mst_edge)

        
    with open(data_path + edge_road, 'w') as f:
        with open(data_path + route_name, 'r') as file: 
            nb_travel = int(file.readline())
            print("il y a ", nb_travel, "trajets")
            content = file.readlines()
                

            for line in content :
                src = int(line.split()[0])
                dest = int(line.split()[1])
                a = Graph.find_path_with_distance(parents, depths, src, dest)[1]
                b = len(Graph.find_path_with_distance(parents, depths, src, dest)[0])
                c = Graph.find_path_with_distance(parents, depths, src, dest)[2]
                f.write(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
                    
    print("Le calcul est fini pour le graphe", {i})
