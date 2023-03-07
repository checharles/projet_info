import osmnxpython  as ox

# Obtenez le graphique OSMnx pour la France
place_name = "Aulan , France"

graph = ox.graph_from_place(place_name, network_type='drive')

ox.plot_graph(graph)