# This will work if ran from the root folder.

"""this test the function graph_from file"""
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

import unittest 
from graph import Graph, graph_from_file
import trajet_truck


class Test_knappsack_greedy_HP(unittest.TestCase):

    def test_network1(self): 
        B = 25*10**9
        self.assertGreaterEqual(trajet_truck.knapsack_hill_climbing(1,0, B)[0],trajet_truck.knapsack_greedy(1,0,B)[0])
        self.assertGreaterEqual(trajet_truck.knapsack_hill_climbing(1,1, B)[0], trajet_truck.knapsack_greedy(1,1, B)[0])
        self.assertGreaterEqual(trajet_truck.knapsack_hill_climbing(1,2, B)[0], trajet_truck.knapsack_greedy(1,2, B)[0])
        
    def test_network3(self): 
        B = 25*10**9
        self.assertGreaterEqual(trajet_truck.knapsack_hill_climbing(3,1,B)[0], trajet_truck.knapsack_greedy(3,1,B)[0])

    def test_network10(self): 
        B = 25*10**9
        self.assertGreaterEqual(trajet_truck.knapsack_hill_climbing(10,1, B)[0], trajet_truck.knapsack_greedy(10,1, B)[0])



if __name__ == '__main__':
    unittest.main()