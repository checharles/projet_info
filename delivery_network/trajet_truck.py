from graph import Graph, graph_from_file, catalog_from_file




data_path = "/home/onyxia/projet_info/input/"

"""the budget, which is a contraint"""
B = 25*10**9



def cost_traject(nb_road, nb_truck):

    time_road = f"route.{nb_road}.out"
    truck_model = f"trucks.{nb_truck}.in"
    route_name = f"routes.{nb_road}.in"

    cost_and_power_truck = catalog_from_file(data_path + truck_model)
    utility = {}

    with open(data_path + route_name, 'r') as f:
        nb_travel = int(file.readline())

        utility[key_travel][0] = 

    with open(data_path + time_road, 'r') as f:
        
        content = f.readlines()
        key_road = 0
        for line in content:
            key_road = key_road + 1
            i = 0 
            min_power = float(line.split()[0])
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility[key_travel][1] = cost_travel

    return cost








def knapsack(nb_truck, nb_road, B) : 
    
    weight_travel = cost_traject(nb_road, nb_truck)

    


