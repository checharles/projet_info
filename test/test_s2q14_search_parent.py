# This will work if ran from the root folder.

"""this function test the function search_parent in a tree created by Graph.kruskal """


import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import Graph, graph_from_file
import unittest   # The test framework

data_path = "/home/onyxia/projet_info/"

class Test_search_parent(unittest.TestCase):

    def test_network1(self):
        g = graph_from_file(data_path + "input/network.1.in")
        g_mst = g.kruskal()
        self.assertEqual(Graph.search_parent(g_mst)[0],{1: 0, 2: 1, 3: 2, 4: 2, 5: 1, 6: 4, 7: 2, 8: 1, 9: 4, 10: 4, 11: 2, 12: 3, 13: 2, 14: 1, 15: 4, 16: 3, 17: 3, 18: 4, 19: 3, 20: 2})
        self.assertEqual(Graph.search_parent(g_mst)[1],{2: (1, 2), 3: (2, 5), 13: (2, 8), 19: (13, 1), 15: (19, 27), 5: (1, 2), 14: (1, 11), 7: (14, 15), 16: (7, 13), 10: (16, 37), 8: (1, 13), 11: (8, 1), 4: (8, 8), 12: (4, 5), 9: (12, 9), 20: (8, 11), 17: (20, 14), 18: (17, 11), 6: (17, 15)})

if __name__ == '__main__':
    unittest.main()