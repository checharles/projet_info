"question18 : différente méthode"

from graph import Graph, graph_from_file, catalog_from_file
import random

data_path = "/home/onyxia/projet_info/input/network_importation/"
truck_path = "/home/onyxia/projet_info/input/truck/"

"""the budget, which is a contraint"""


def cost_traject(nb_road, nb_truck):
    """this function define the value of a travel and  the cost of the truck to use it

    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file

    Outputs
    -----------
    utility : dictionnary
        Utility is dictionnary, which key are the number of the road. It gets the value of the road and the cost 
        of the truck to use it. the list is (value, cost of ten rauck, model of the truck, ratio cost/profit)

    nb_travel : int
        the number of possible traject
    """

    """Load of the needed value"""
    time_road = f"route.{nb_road}.out" #this file contains the min power to travel on the paths"""
    truck_model = f"trucks.{nb_truck}.in" #this file contains the truck catalog"""
    route_name = f"routes.{nb_road}.in" #this file contain the value of the paths"""

    """define the final truck catalog : useful trucks and their cost"""
    cost_and_power_truck = catalog_from_file(truck_path + truck_model)

    """Utility is dictionnary, which key are the number of the road. It gets the value of the road and the cost and the model of the truck to use it"""
    utility = {}
    travel = {}
    key_travel = 0


    """Finding of the road value"""
    with open(data_path + route_name, 'r') as f:
        nb_travel = int(f.readline())
        content = f.readlines() 
        
        for line in content :
            key_travel = key_travel + 1
            utility[key_travel] = float(line.split()[2])
            travel[key_travel] = (int(line.split()[0]), int(line.split()[1]))
             
    """findng the truck cost"""

    with open(data_path + time_road, 'r') as f:
        
        content = f.readlines()
        utility_final = {}
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])

            """finf the truck with the minimal power to travel along the path"""
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            value = float(utility[key_travel]) 
            ratio = value/cost_travel
            utility_final[key_travel] = (value, cost_travel, int(i + 1), ratio, key_travel, travel[key_travel])
            

    return utility_final, nb_travel


def knapsack_dynamic_programming(nb_road, nb_truck, B):
    """This function uses dynamic programming 
    use for trucks.1.in and truck.0.in
    
    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file
    B : int
        the budget to buy the trucks

    Outputs
    -----------
    value : int
        the value of the allocation

    selected_travels : list
        the list of the selected trajets for the allocation
    """

    """Considering that the cost of all truck are mutiple of 10 000, we can scale B accordingly"""
    B = B // 10**4

    """Compute the cost and utility of each traject"""
    travels, nb_travel = cost_traject(nb_road, nb_truck)

    """Update the cost of each traject by reducing it by a factor of 10^4"""
    for i in range(1, nb_travel+1):
        travels[i] = (travels[i][0], travels[i][1] // 10**4)

    """Initialize the dynamic programming table"""
    dp = [[0 for _ in range(B+1)] for _ in range(nb_travel+1)]

    """Fill in the dynamic programming table"""
    for i in range(1, nb_travel+1):
        for j in range(1, B+1):
            value, weight = travels[i]
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

    """Backtrack to find the optimal allocation"""
    selected_travels = []
    j = B
    for i in range(nb_travel, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected_travels.append(i)
            j -= travels[i][1]

    """Compute the total value of the allocation"""
    value  = dp[nb_travel][B]

    """Return the total value and the list of selected travels in reverse order"""
    return value, selected_travels[::-1]


def knapsack_greedy(nb_road, nb_truck, B):
    """this algorithm uses the greedy method to find an allocation close to the best allocation. It firt classes the travel using a ratio  value/cost and takes the one with the 
    best ratio, until the budget is completely used.    
    
    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file
    B : int
        the budget to buy the trucks

    Outputs : 
    -----------
    total_value : int
        the value of the allocation    
     allocation : list
        a list of the allocation, with the form (src, dest, model of the truck)
     selected_travels : list
        the list of travels of the allocation
    nb_trajets: int
        the number of trajets in the allocation
    total_weight: int
        the budget used
    
    """

    
    """The possible tajects are define to find their cost (=weight) and their value  = (utility)"""
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    list_travels = list(travels.values())

    """initilization of the values"""
    total_value = 0
    total_weight = 0
    selected_travels = []
    nb_trajets = 0
    allocation = []

    """a greedy algorythm is used to add the travels with the best ratio"""
    for travel in sorted(list_travels, key=lambda x: x[3], reverse=True):        
        if total_weight + travel[1] <= B:
            total_value += travel[0]
            total_weight += travel[1]
            allocation.append((travel[5], int(travel[2]), travel[4]))
            selected_travels.append(travel)
            nb_trajets = nb_trajets + 1

    return total_value, allocation, selected_travels, nb_trajets, total_weight


import random

def knapsack_hill_climbing(nb_road, nb_truck, B, max_iterations=1000, num_neighbors=10):
    """this algorithm uses the greedy method to find an allocation close to the best allocation. It firt classes the travel using a ratio  value/cost and takes the one with the 
    best ratio, until the budget is completely used. A local search using hill climbing is then used
    
    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file
    B : int
        the budget to buy the trucks

    Outputs : 
    -----------
    total_value : int
        the value of the allocation    
     allocation : list
        a list of the allocation, with the form (src, dest, model of the truck)
     selected_travels : list
        the list of travels of the allocation
    nb_trajets: int
        the number of trajets in the allocation
    total_weight: int
        the budget used
    
    """

    """Generate an initial allocation using the greedy algorithm"""
    total_value, allocation, selected_travels, nb_trajets, total_weight = knapsack_greedy(nb_road, nb_truck, B)
    best_allocation = allocation
    best_value = total_value
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    """Evaluate the quality of the initial allocation"""
    current_allocation = allocation
    current_value = total_value
    
    """Perform hill climbing"""
    for i in range(max_iterations):
        """Generate a set of neighboring allocations"""
        neighbors = []
        for j in range(num_neighbors):
            """Randomly change a small number of travels in the allocation"""
            new_allocation = current_allocation[:]
            num_changes = random.randint(1, 3)
            for k in range(num_changes):
                index = random.randint(0, len(new_allocation)-1)
                travel = selected_travels[index]
                new_travel = random.choice(list(travels.values()))
                new_allocation[index] = (new_travel[5], int(new_travel[2]), new_travel[4])
            neighbors.append(new_allocation)
        
        """Evaluate the quality of each neighboring allocation"""
        neighbor_values = []
        for neighbor in neighbors:
            value = 0
            for travel in neighbor:
                value += travels[travel[2]][0]
            neighbor_values.append(value)
        
        """Select the best neighboring allocation"""
        best_neighbor_index = neighbor_values.index(max(neighbor_values))
        best_neighbor_value = neighbor_values[best_neighbor_index]
        best_neighbor_allocation = neighbors[best_neighbor_index]
        
        """Compare the quality of the best neighboring allocation to the quality of the current allocation"""
        if best_neighbor_value > current_value:
            current_allocation = best_neighbor_allocation
            current_value = best_neighbor_value
            if current_value > best_value:
                best_allocation = current_allocation
                best_value = current_value
        else:
            break
    
    """Return the best allocation found during the hill climbing search"""
    return best_value, best_allocation, selected_travels, nb_trajets, total_weight
