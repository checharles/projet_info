# This will work if ran from the root folder.

"""this function tests the mofify function get_path_with_power (q3 + q5 )""" 
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

data_path = "/home/onyxia/projet_info/"


class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file(data_path + "input/network.00.in")
        self.assertEqual(g.get_path_with_power(1, 4, 11), [1, 2, 3, 4])
        self.assertEqual(g.get_path_with_power(1, 4, 10), None)

    def test_network2(self):
        g = graph_from_file(data_path + "input/network.02.in")
        self.assertIn(g.get_path_with_power(1, 2, 11), [[1, 2], [1, 4, 3, 2]])
    
    def test_network3(self):
        g = graph_from_file(data_path + "input/network.03.in")
        self.assertIn(g.get_path_with_power(1, 4, 10), [[1, 4], [1, 2, 3, 4]])

    def test_network4(self):
        g = graph_from_file(data_path + "input/network.04.in")
        self.assertIn(g.get_path_with_power(1, 2, 11), [[1, 2], [1, 4, 3, 2]])

    def test_network5(self):
        g = graph_from_file(data_path + "input/network.05.in")
        self.assertIn(g.get_path_with_power(1, 4, 8), [[1, 4], [1, 2, 3, 4], [1, 3, 2, 4], ])


if __name__ == '__main__':
    unittest.main()
