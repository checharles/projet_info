"""this program implement a realistic solution to the problem; using a gredy algorythm"""


from graph import Graph, graph_from_file, catalog_from_file


data_path = "/home/onyxia/projet_info/input/"

"""the budget, which is a contraint"""
B = 25*10**9


from statistics import mean

data_path = "/home/onyxia/projet_info/input/realistic_file"

"""opening each file and calcuting the time """


def cost_traject_realistic(nb_road, nb_truck):
    """this function is used to solve a more realistic approach of the problem. Using different-weighted Kruskal algorithms, it first generates  minimum power to travel between two
    nodes using different paths. It then calculates the real cost of each possible paths and keeps the one with the best ratio value/utility

    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file

    Outputs
    -----------
    utility : dictionnary
        Utility is dictionnary, which keys are the number of the road. It gets the value of the road and the cost 
        of the truck to use it. The list is (value, cost of the truck, model of the truck, (source node, destination node))

    nb_travel : int
        the number of possible trajects
    """

    """initialisation of the files"""
    file_name = f"network.{nb_road}.in"
    route_name = f"routes.{nb_road}.in"
    power_road = f"routes_power.{nb_road}.out"
    dist_road = f"route_dist.{nb_road}.out"
    ratio_road = f"route_ratio.{nb_road}.out"
    truck_model = f"trucks.{nb_truck}.in"

    cost_and_power_truck = catalog_from_file(data_path + truck_model)


    """initialisation of the different utilities"""
    utility_power = {}
    utility_dist = {}
    utility_ratio = {}
    utility = {}
    list_travel
    key_travel = 0



    with open(data_path + route_name, 'r') as f:
        nb_travel = int(f.readline())
        content = f.readlines() 
        
        for line in content:
            key_travel = key_travel + 1
            utility_power[key_travel] = float(line.split()[2])
            utility_dist[key_travel] = float(line.split()[2])
            utility_ratio[key_travel] = float(line.split()[2])
            utility[key_travel] = float(line.split()[2])
            src = float(line.split()[0])
            dest = float(line.split()[1])
            travel = (src, dest)
            list_travel.append(travel)


    with open(data_path + power_road, 'r') as f:

        """we  read the file with a MST where the weight is the minimun power. The minimun power is found and so the price of the truck. The realistic solition is then found 
        according the distance the number of edges crossed and the cost of the truck. 
        """
        
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 

            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])

            """The model of the truck is find and its price is calculated"""
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
            cost_travel = cost_and_power_truck[i][1]
            
            utility_power[key_travel] = (max(utility_power[key_travel]*((0.001)**lenght_path), 0) - dist*0.01, cost_travel,i + 1)


    with open(data_path + dist_road, 'r') as f:
        
        """we  read the file with a MST where the weight is the distance of the edge. The minimun power is found and so the price of the truck. The realistic solition is 
        then found according the distance the number of edges crossed and the cost of the truck. 
        """
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])

            """The model of the truck is find and its price is calculated"""
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility_dist[key_travel] = (utility_dist[key_travel]*((0.001)**lenght_path) - dist*0.01, cost_travel, i + 1, max(utility_dist[key_travel]*((0.999)**lenght_path) - dist*0.01, 0)/cost_travel )

    with open(data_path + ratio_road, 'r') as f:
        
        """we  read the file with a MST where the weight is the ratio between the minimun power and the distance of the edge. The minimun power is found and so the price 
        of the truck. The realistic solition is then found according the distance the number of edges crossed and the cost of the truck. 
        """
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])
            
            """The model of the truck is find and its price is calculated"""
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility_ratio[key_travel] = (max(utility_ratio[key_travel]*((0.999)**lenght_path) - dist*0.01, 0), cost_travel, i + 1, max(utility_ratio[key_travel]*((0.999)**lenght_path) - dist*0.01, 0)/cost_travel )

    with open(data_path + edge_road, 'r') as f:
        

        """we  read the file with a MST where the weight is the distance, which value is always 1. So the path between two nodes has the fewer possible number of edges. 
        The minimun power is found and so the price 
        of the truck. The realistic solition is then found according the distance the number of edges crossed and the cost of the truck. 
        """
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])

            """The model of the truck is find and its price is calculated"""
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility_edge[key_travel] = (max(utility_edge[key_travel]*((0.999)**lenght_path) - dist*0.01, 0), cost_travel, i + 1, max(utility_edge[key_travel]*((0.999)**lenght_path) - dist*0.01, 0)/cost_travel)


    """Eventually the travel with the best ratio value/realistic cost is chosen"""

    for k in range(1, nb_travel + 1):

        listes = [utility_power[k], utility_dist[k], utility_ratio[k]]
        utility[k] = max(listes, key=lambda x: x[3])

        """the nodes connected are added to the possible allocation"""
        utility[k].append(list_travel[k-1])

    return utility, nb_travel



def knapsack_greedy_realistic(nb_road, nb_truck, B):
    travels, nb_travel = cost_traject_realistic(nb_road, nb_truck)
    
    ratios = [(travels[i][0] / travels[i][1], i) for i in range(1, nb_travel + 1)]
    ratios.sort(reverse=True)
    total_value = 0
    total_weight = 0
    selected_travels = []
    nb_trajets = 0
    for ratio, i in ratios:
        if total_weight + travels[i][1] <= B:
            total_value += travels[i][0]
            total_weight += travels[i][1]
            selected_travels.append((i, travels[i][2]))
            nb_trajets = nb_trajets + 1

    return total_value, selected_travels, nb_trajets, total_weight


