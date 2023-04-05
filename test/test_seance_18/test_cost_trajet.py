# This will work if ran from the root folder.

"""this test the function graph_from file"""
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

import unittest 
from graph import Graph, graph_from_file
import trajet_truck


class Test_cost_travel(unittest.TestCase):

    def test_network1(self): 
        self.assertEqual(trajet_truck.cost_traject(1,0)[0][1],(9664.0, 200000, 1, 0.04832, 1, (6, 11)))
        self.assertEqual(trajet_truck.cost_traject(1,0)[1], 140 )
        self.assertEqual(trajet_truck.cost_traject(1,1)[0][1],(9664.0, 50000, 1, 0.19328, 1, (6, 11)) )
        self.assertEqual(trajet_truck.cost_traject(1,2)[0][1], (9664.0, 99, 1, 97.61616161616162, 1, (6, 11)))

    def test_network2(self): 
        self.assertEqual(trajet_truck.cost_traject(2,0)[0][1],(2650.0, 200000, 1, 0.01325, 1, (37816, 77493)) )
        self.assertEqual(trajet_truck.cost_traject(2,0)[1], 100000 )
        self.assertEqual(trajet_truck.cost_traject(2,1)[0][1],(2650.0, 50000, 1, 0.053, 1, (37816, 77493)) )
        self.assertEqual(trajet_truck.cost_traject(2,2)[0][1], (2650.0, 6465, 20, 0.4098994586233565, 1, (37816, 77493)))
        




if __name__ == '__main__':
    unittest.main()