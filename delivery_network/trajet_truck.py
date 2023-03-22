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
    key_travel = 0

    with open(data_path + route_name, 'r') as f:
        nb_travel = int(f.readline())
        content = f.readlines() 
        
        for line in content :
            key_travel = key_travel + 1
            utility[key_travel]= int(line.split()[2])

    with open(data_path + time_road, 'r') as f:
        
        content = f.readlines()
        key_travel = 0
        for line in content:
            key_travel = key_travel + 1
            i = 0 
            min_power = float(line.split()[0])
            while cost_and_power_truck[i][0] < min_power:
                i = i+1
        
            cost_travel = cost_and_power_truck[i][1]
            
            utility[key_travel] = (utility[key_travel], cost_travel)

    return utility, nb_travel


def knapsack(nb_road, nb_truck, B):
    """use for truck 1 and truck 0"""
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
    travels, nb_travel = cost_traject(nb_road, nb_truck)
    
    ratios = [(travels[i][0] / travels[i][1], i) for i in range(1, nb_travel + 1)]
    ratios.sort(reverse=True)
    total_value = 0
    total_weight = 0
    for ratio, i in ratios:
        if total_weight + travels[i][1] <= B:
            total_value += travels[i][0]
            total_weight += travels[i][1]
    return total_value


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



