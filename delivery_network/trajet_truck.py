from graph import Graph, graph_from_file, catalog_from_file


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
    key_travel = 0


    """Finding of the road value"""
    with open(data_path + route_name, 'r') as f:
        nb_travel = int(f.readline())
        content = f.readlines() 
        
        for line in content :
            key_travel = key_travel + 1
            utility[key_travel] = float(line.split()[2])

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
            utility_final[key_travel] = (value, cost_travel, i + 1, ratio, key_travel)
            

    return utility_final, nb_travel


def knapsack_dynamic_programming(nb_road, nb_truck, B):
    """This function uses dynamic programming 
    use for trucks.1.in and truck.0.in"""

    """Considering that the cost of all truck are mutiple of 10 000, we can scale B accordingly"""
    B = B // 10**4
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    for i in range(1, nb_travel+1):
        travels[i] = (travels[i][0], travels[i][1] // 10**4)

    dp = [[0 for _ in range(B+1)] for _ in range(nb_travel+1)]
    
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
    
    return dp[nb_travel][B], selected_travels[::-1]

    

def knapsack_greedy(nb_road, nb_truck, B):
    
    """The possible tajects are define to find their cost (=weight) and their value  = (utility)"""
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    list_travels = list(travels.values())

    """initilization of the values"""
    total_value = 0
    total_weight = 0
    selected_travels = []
    nb_trajets = 0

    """a grededy algorythm is used to add the travels with the best ratio"""
    for travel in sorted(list_travels, key=lambda x: x[3], reverse=True):        
        if total_weight + travel[1] <= B:
            total_value += travel[0]
            total_weight += travel[1]
            selected_travels.append((travel[4], travel[2]))
            nb_trajets = nb_trajets + 1

    return total_value, selected_travels, nb_trajets, total_weight


def knapsack_heuristic(nb_road, nb_truck, B, max_iter=10):
    # Initialize solution
    solution = set()
    best_value = 0
    
    
    for i in range(max_iter):
        # Step 2: Sort items by value per unit of weight
        travels, nb_travel = cost_traject(nb_road, nb_truck)
        ratios = [(travels[i][0] / travels[i][1], i) for i in range(1, nb_travel + 1)]
        ratios.sort(reverse=True)

        # Step 3: Select items until max capacity is reached
        current_weight = 0
        current_value = 0
        nb_trajets = 0 
        for ratio, i in ratios:
            if current_weight + travels[i][1] <= B:
                current_value += travels[i][0]
                current_weight += travels[i][1]
                solution.add(i)

        # Step 4: Local search to improve solution
        if current_value > best_value:
            improved = True
            while improved:
                improved = False
                for item in solution:
                    for j in range(1, nb_travel + 1):
                        if j not in solution and current_weight + travels[j][1] <= B:
                            new_solution = solution.copy()
                            new_solution.remove(item)
                            new_solution.add(j)
                            new_value = sum(travels[k][0] for k in new_solution)
                            new_weight = sum(travels[k][1] for k in new_solution)
                            if new_value > current_value and new_weight <= B:
                                solution = new_solution
                                current_value = new_value
                                current_weight = new_weight
                                improved = True
                                break
                    if improved:
                        break
        
        # Step 5: Check if stopping criterion is reached
        if current_value > best_value:
            best_value = current_value
        else:
            break

    return best_value, list(solution)



