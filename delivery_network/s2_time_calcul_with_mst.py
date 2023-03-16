import time
from graph import Graph, graph_from_file
import random
from statistics import mean




data_path = "/home/onyxia/projet_info/input/"

"""opening each file and calcuting the time """

i =1 

#for  i in range(1,11): 

if i == 1: 

    file_name = f"network.{i}.in"
    route_name = f"routes.{i}.in"
    time_road = f"route.{i}.out"
    g = graph_from_file(data_path + file_name)
    g_mst = Graph.kruskal(g)

    depths, parents = Graph.search_parent(g_mst)

    start_time = time.perf_counter()
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



print("a")

    
    

    
