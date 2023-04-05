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
            self.assertEqual(trajet_truck.knapsack_dynamic_programming(1,0, B)[1], 675755.0 )
            self.assertEqual(trajet_truck.knapsack_dynamic_programming(1,1, B)[1], 675755.0)
            self.assertEqual(trajet_truck.knapsack_dynamic_programming(1,2, B)[1], 675755.0)
            


if __name__ == '__main__':
    unittest.main()