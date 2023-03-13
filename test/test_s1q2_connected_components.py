# This will work if ran from the root folder.

"""this function test the fucntion connected_componennts"""
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import Graph, graph_from_file
import unittest   # The test framework

data_path = "/home/onyxia/projet_info/"


class Test_GraphCC(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file(data_path + "input/network.00.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})})

    def test_network1(self):
        g = graph_from_file(data_path + "input/network.01.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})})
    
    def test_network2(self):
        g = graph_from_file(data_path + "input/network.02.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4}), frozenset({5}), frozenset({6}), frozenset({7}), frozenset({8}), frozenset({9}), frozenset({10})})
    
    def test_network5(self):
        g = graph_from_file(data_path + "input/network.05.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4})})

if __name__ == '__main__':
    unittest.main()
