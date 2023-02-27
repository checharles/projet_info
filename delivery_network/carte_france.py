import osmnx as ox
import numpy as np
from graph import Graph
import pandas as pd




# Télécharger la carte de France avec OSMnx
place_name = "France"
G = ox.graph_from_place(place_name, network_type='drive')

#Téléacherger les donnés de l'INSEE 
df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/1b6d98f1-d8f9-4527-bfe2-25617f7bfa3c')
# Extraire les villes de plus de 100 000 habitants
cities = []
for node, data in G.nodes(data=True):
    if 'population' in data and data['population'] >= 100000:
        cities.append(node)

print(cities)
# Extraire un sous-graphe contenant uniquement les nœuds et les arêtes correspondant aux villes sélectionnées
subgraph = G.subgraph([node for cities in G.nodes if G.nodes[node]['name'] in villes])
ox.plot_graph('subgraph')

"""
# Calculer les profits pour chaque trajet entre deux villes
profits = {}
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        city1 = cities[i]
        city2 = cities[j]
        profit = min(G.nodes[city1]['population'], G.nodes[city2]['population'])
        profits[(city1, city2)] = profit
        profits[(city2, city1)] = profit

# Créer un objet Graph et ajouter des noeuds et des arêtes
map_france = Graph()
for node, data in G.nodes(data=True):
    if node in cities:
        map_france.add_node(node, data)
for u, v, data in G.edges(data=True):
    if u in cities and v in cities:
        p = np.inf
        if 'highway' in data:
            if data['highway'] == 'motorway':
                p = 3
            elif data['highway'] == 'trunk':
                p = 2
            else:
                p = 1
        dist = data['length']
        time = data['length'] / data['maxspeed']
        graph.add_edge(u, v, dist=dist, time=time, p=p)

# Utiliser le graphe pour la suite de l'exercice
...
"""