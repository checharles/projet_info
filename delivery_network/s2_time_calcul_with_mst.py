import time
from graph import Graph, graph_from_file
import random
from statistics import mean


data_path = "/home/onyxia/projet_info/input/"

"""opening each file and calcuting the time """
for i in range(1 ,11):
    file_name = f"network.{i}.in"
    route_name = f"routes.{i}.in"
    g = graph_from_file(data_path + file_name)
    g_mst = Graph.kruskal(g)
    with open(data_path + route_name, 'r') as file: 
        nb_travel = int(file.readline())
        print("il y a ", nb_travel, "trajets")
        content = file.readlines()
        time_list = list()

        """Calculating the time to find a path through a sample of travel """
        for j in range(5):
            nb_ligne = random.randrange(nb_travel) + 1
            src = content[nb_ligne].split()[0]
            dest = content[nb_ligne].split()[1]
                                
            start_time = time.perf_counter()

            path = g_mst.get_path_with_power(src, dest)

            power_max = float('-inf')
            
            for i in range(len(path)):  
                sorted(g_mst.graph[path[i]] , key=lambda neighbor: neighbor[1])
                power_max = max(power_max, g_mst.graph[path[i + 1]])
                print(power_max)
            

            end_time = time.perf_counter()

            execution_time = end_time - start_time
            time_list.append(execution_time)
    
        execution_time_mean = mean(time_list)
        total_time = execution_time_mean*nb_travel
        print("Le temps d'exécution moyen est de :", execution_time_mean/60, "minutes")
        print("Le temps total pour calculer l'ensemble des trajets du graphe ", {i}, "en utilisant un arbre couvrant est : """, total_time/3600, "heures")

    
