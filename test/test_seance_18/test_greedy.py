# This will work if ran from the root folder.

"""this test the function graph_from file"""
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

import unittest 
from graph import Graph, graph_from_file
import trajet_truck


class Test_knappsack_DP(unittest.TestCase):

    def test_network1(self): 
        B = 25*10**9
        self.assertEqual(trajet_truck.knapsack_greedy(1,0, B)[0], 675755.0 )
        self.assertEqual(trajet_truck.knapsack_greedy(1,0, B)[4], 28000000)
        self.assertEqual(trajet_truck.knapsack_greedy(1,0, B)[3], 140)
        self.assertEqual(trajet_truck.knapsack_greedy(1,1, B)[0], 675755.0)
        self.assertEqual(trajet_truck.knapsack_greedy(1,1, B)[4], 7000000)
        self.assertEqual(trajet_truck.knapsack_greedy(1,1, B)[3], 140)


    def test_network2(self): 
        B = 25*10**9
        self.assertEqual(trajet_truck.knapsack_greedy(2,0, B)[0], 499692266.0 )
        self.assertEqual(trajet_truck.knapsack_greedy(2,0, B)[3], 100000)
        self.assertEqual(trajet_truck.knapsack_greedy(2,0, B)[4], 20000000000.0)
        self.assertEqual(trajet_truck.knapsack_greedy(2,1, B)[0], 499692266.0)
        self.assertEqual(trajet_truck.knapsack_greedy(2,1, B)[4], 5000000000)
        self.assertEqual(trajet_truck.knapsack_greedy(2,1, B)[3], 100000)

if __name__ == '__main__':
    unittest.main()