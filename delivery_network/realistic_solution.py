from graph import Graph, graph_from_file, catalog_from_file


data_path = "/home/onyxia/projet_info/input/"

"""the budget, which is a contraint"""
B = 25*10**9


from statistics import mean

data_path = "/home/onyxia/projet_info/input/"

"""opening each file and calcuting the time """


def cost_traject_realistic(nb_road, nb_truck):

   
    file_name = f"network.{nb_road}.in"
    route_name = f"routes.{nb_road}.in"
    power_road = f"routes_power.{nb_road}.out"
    dist_road = f"route_dist.{nb_road}.out"
    ratio_road = f"route_ratio.{nb_road}.out"
    truck_model = f"trucks.{nb_truck}.in"

    cost_and_power_truck = catalog_from_file(data_path + truck_model)

    utility_power = {}
    utility_dist = {}
    utility_ratio = {}
    utility = {}
    
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

    with open(data_path + power_road, 'r') as f:
        
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])

            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility_power[key_travel] = (utility_power[key_travel]*((0.001)**lenght_path) - dist*0.01, cost_travel,i + 1)


    with open(data_path + dist_road, 'r') as f:
        
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])

            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility_dist[key_travel] = (utility_dist[key_travel]*((0.001)**lenght_path) - dist*0.01, cost_travel,i + 1)

    with open(data_path + ratio_road, 'r') as f:
        
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            dist = float(line.split()[2])
            lenght_path = int(line.split()[1])

            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility_ratio[key_travel] = (max(utility_ratio[key_travel]*((0.999)**lenght_path) - dist*0.01, 0), cost_travel, i + 1)



    for k in range(1, nb_travel + 1):

        listes = [utility_power[k], utility_dist[k], utility_ratio[k]]
        utility[k] = max(listes, key=lambda x: x[0])

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


