import time
from graph import Graph
from math import factorial
data_path = "/home/onyxia/projet_info/input/"

"""opening each file and calcuting the time """
for i in range(1,11):
    file_name = f"routes.{i}.in"
    g = Graph.graph_from_file(data_path + file_name)

    """there are nb_edges edges, so total number of possible trajects is nb_edges!"""
    nb_trajet_possible = factorial(nb_edges)
    print("il y a ", nb_trajet_possible)
    time_list = ()

    """Calculating the time to find a traject through a sample of trajects """
    for j in range (100):
        src=int(rand()*g.nb_edges+1)
        dest = int(rand()*g.nb_edges)
        
        start_time = time.perf_counter()

        Graph.min_power(g, src, dest)

        end_time = time.perf_counter()


        execution_time = end_time - start_time
        time_list.append(execution_time)
    
    execution_time_mean  = mean(time_list)
    total_time = execution_time_mean*nb_trajects_possible 
    print("Le temps d'exécution moyen est de :", execution_time_mean/3600, "heures" )
    print("Le temps total pour calculer l'ensemble des trajets  du graphe""",{i}, "est : """, total_time/3600, "heures" )

    
