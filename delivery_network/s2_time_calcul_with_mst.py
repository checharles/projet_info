import time
from graph import Graph, graph_from_file
import random
from statistics import mean




data_path = "/home/onyxia/projet_info/input/network_importation"

"""opening each file and calcuting the time. This time tehre is a preprocessing in the form of the creation of a minimun spanning tree within the graph. A very effective solution 
can now be used to find the minimun power required to travel between two nodes. the results of the minimun power are written in a text file, called route.{i}.out, i being the number 
of the graph """

for i in range(1,11): 

    """creation of the files"""
    file_name = f"network.{i}.in"
    route_name = f"routes.{i}.in"
    time_road = f"route.{i}.out"
    g = graph_from_file(data_path + file_name)

    """the preprocess consists in creating a MST and finding in this MST the depth and parents of each nodes"""
    g_mst = Graph.kruskal(g)
    depths, parents = Graph.search_parent(g_mst)

    start_time = time.perf_counter()

    """the minimun power is found and writen for each trajet found in the file routes.i.in"""
    with open(data_path + time_road, 'w') as f:
        with open(data_path + route_name, 'r') as file: 
            nb_travel = int(file.readline())
            print("il y a ", nb_travel, "trajets")
            content = file.readlines()
            

            for line in content :
                src = int(line.split()[0])
                dest = int(line.split()[1])
                a = Graph.find_path(parents, depths, src, dest)[1]
                f.write(str(a) + '\n')
                  
              
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("Le temps total pour calculer l'ensemble des trajets du graphe ", {i}, "en utilisant un arbre couvrant est : """, execution_time, "secondes")


    
    

    
