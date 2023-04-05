# À compléter

# This will work if ran from the root folder.

"""this test the function graph_from file"""
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

import unittest 
from graph import Graph, graph_from_file

data_path = "/home/onyxia/projet_info/"


class Test_GraphLoading(unittest.TestCase):
    
    def test_network1(self):
        g = graph_from_file(data_path + "input/network_importation/network.01.in")
        self.assertEqual(g.graph[1][0][1], 1)
            
    def test_network4(self):
        g = graph_from_file(data_path + "input/network_importation/network.04.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertEqual(g.graph[4][0][2], 2)
        self.assertEqual(g.graph[1][1][2], 89)
        self.assertEqual(g.graph[1][0][2], 6)

    def test_network5(self):
        g = graph_from_file(data_path + "input/network_importation/network.05.in")
        self.assertEqual(g.nb_nodes, 4)
        self.assertEqual(g.nb_edges, 6)
        self.assertEqual(g.graph[2][1][2], 1)
    
    def test_network5bis(self):
        g = graph_from_file(data_path + "input/network_importation/network.05.in")
        self.assertEqual(g.nb_nodes, 4)
        self.assertEqual(g.nb_edges, 6)
        self.assertEqual(g.graph[1][2][1], 4)

if __name__ == '__main__':
    unittest.main()
