"question18 : différente méthode"

from graph import Graph, graph_from_file, catalog_from_file
import random
import multiprocessing
data_path = "/home/onyxia/projet_info/input/"

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
    cost_and_power_truck = catalog_from_file(data_path + truck_model)

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

    selected_travels : lis
        the list of the selected trajets for the allocation
    """

    """Considering that the cost of all truck are mutiple of 10 000, we can scale B accordingly"""
    B = B // 10**4
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    for i in range(1, nb_travel+1):
        travels[i] = (travels[i][0], travels[i][1] // 10**4)

    dp = [[0 for _ in range(B+1)] for _ in range(nb_travel+1)]
    
    """Dynamic programming is now used"""
    for i in range(1, nb_travel+1):
        for j in range(1, B+1):
            value, weight = travels[i]
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
    
    selected_travels = []
    j = B
    for i in range(nb_travel, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected_travels.append(i)
            j -= travels[i][1]
    
    value  = dp[nb_travel][B]
    return value, selected_travels[::-1]

    

def knapsack_greedy(nb_road, nb_truck, B):
    """this algorithm uses the greddy method to find an allocation close to the best allocation. It firt classes the travel using a ratio  value/cost and takes the one with the 
    best ratio, until the budget is completely used
    
    

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


def knapsack_greedy_local_search_random(nb_road, nb_truck, B, max_iterations):

    """this algorithm uses the greedy method to find an allocation close to the best allocation. It firt classes the travel using a ratio  value/cost and takes the one with the 
    best ratio, until the budget is completely used. it then used a random search to improve the solution.
    


    Parameters :
    -----------
    nb_road: int
        the number of the network studied
    
    nb_truck: int
        the number of the studied truck file
    B: int
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

    
    """The possible trajects are defined to find their cost (=weight) and their value = (utility)"""
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    list_travels = list(travels.values())

    """Initialization of the values"""
    total_value, allocation, selected_travels, total_weight, nb_trajets = knapsack_greedy(nb_road, nb_truck, B)
    new_value = total_value
    print("initialization")

    """Perform local search"""
    list_travels_sorted = sorted(list_travels, key=lambda x: x[1])
    
    for iteration in range(max_iterations):
        
        """choose a random item to remove from the knapsack"""
        item = random.choice(selected_travels)
        selected_travels.remove(item)
        allocation.remove((item[5],item[2], item[4]))
        total_value -= item[0]
        total_weight -= item[1]
        print("step1")
        
        """evaluate all feasible items and choose the best one to add to the knapsack"""
        remaining_weight = B - total_weight
        feasible_items = list(t for t in list_travels_sorted if t not in selected_travels and t[1] <= remaining_weight)

        better_item = random.choice(feasible_items)
        new_total_weight = total_weight + better_item[1]
        if new_total_weight <= B and better_item[0] + total_value > new_value:
                best_item = better_item
                new_value = better_item[0] + total_value
        
        """if a better item was found, add it to the knapsack"""
        if better_item is not None:
            allocation.append((better_item[5],better_item[2], better_item[4]))
            total_value = new_value
            total_weight += better_item[1]
              
    return total_value, allocation, selected_travels,nb_trajets, total_weight


    

def eval_modified_solution(args):
    selected_travels_set, feasible_item, travels, B = args
    
    """Find the travel with the lowest value/weight ratio"""
    item = min(selected_travels_set, key=lambda x: travels[x[2]][0] / travels[x[2]][1])
    
    """Remove the travel with the lowest value/weight ratio"""
    selected_travels_set.remove(item)
    
    """Add the feasible item"""
    selected_travels_set.add(feasible_item)
    
    """Check if the modified solution is feasible"""
    total_weight = sum(travels[item[2]][1] for item in selected_travels_set)
    
    if total_weight > B:
        return (float("-inf"), None, None, None, None)
    
    """Calculate the total value of the modified solution"""
    total_value = sum(travels[item[2]][0] for item in selected_travels_set)
    
    return (total_value, feasible_item, item, feasible_item, total_weight)


def knapsack_greedy_local_search_smart(nb_road, nb_truck, B, max_iterations):
    
    """this algorithm uses the greedy method to find an allocation close to the best allocation. It firt classes the travel using a ratio  value/cost and takes the one with the 
    best ratio, until the budget is completely used. it then used a smart local search to improve the solution. The smart local search involved a better selction of possible tracels and parallazideed solution
    


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
    
    """The possible trajects are defined to find their cost (=weight) and their value (=utility)"""
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    list_travels = list(travels.values())

    """Initialization of the values"""
    total_value, allocation, selected_travels, nb_trajets, total_weight = knapsack_greedy(nb_road, nb_truck, B)
    new_value = total_value
    
    """Convert selected_travels to a set for faster operations"""
    selected_travels_set = set(selected_travels)
    
    """Perform local search"""
    feasible_items = [t for t in list_travels if t not in selected_travels_set]
    for iteration in range(max_iterations):
        
        """Remove the travel with lowest ratio of value to weight"""
        item = min(selected_travels_set, key=lambda x: travels[x[2]][0] / travels[x[2]][1])
        selected_travels_set.remove(item)
        allocation.remove((item[5],item[2], item[4]))
        total_value -= travels[item[2]][0]
        total_weight -= travels[item[2]][1]

        remaining_weight = B - total_weight
        
        """Sort feasible items by decreasing ratio of value to weight"""
        feasible_items = sorted(feasible_items, key=lambda x: x[0] / x[1], reverse=True)
        for item in feasible_items:
            if item[1] <= remaining_weight:
                selected_travels_set.add(item)
                total_value += item[0]
                total_weight += item[1]
                remaining_weight = B - total_weight
                
                """Evaluate the modified solution using multiprocessing"""
                with multiprocessing.Pool() as pool:
                    results = pool.map(eval_modified_solution, [(selected_travels_set, t, travels, B) for t in feasible_items])
                
                """Update the best solution"""
                for i, result in enumerate(results):
                    if result[0] > new_value:
                        new_value = result[0]
                        feasible_items.pop(i)
                        feasible_items.append(result[1])
                        selected_travels_set.remove(result[2])
                        allocation.remove((result[2][5],result[2][2], result[2][4]))
                        selected_travels_set.add(result[3])
                        allocation.append((result[3][5],result[3][2], result[3][4]))
                        total_value = result[0]
                        total_weight = result[4]
                        break
                        
                break
    
    """Convert selected_travels_set back to a list for consistency"""
    selected_travels = list(selected_travels_set)
    
    
    return total_value, allocation, selected_travels, nb_trajets, total_weight