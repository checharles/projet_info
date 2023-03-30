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
        self.assertEqual(Graph.search_parent(g_mst)[1],{2: (1, 2, 6312.0), 3: (2, 5, 6891.0), 13: (2, 8, 7816.0), 19: (13, 1, 5082.0), 15: (19, 27, 3013.0), 5: (1, 2, 1209.0), 14: (1, 11, 231.0), 7: (14, 15, 4757.0), 16: (7, 13, 1315.0), 10: (16, 37, 4618.0), 8: (1, 13, 5452.0), 11: (8, 1, 8542.0), 4: (8, 8, 7291.0), 12: (4, 5, 4713.0), 9: (12, 9, 3330.0), 20: (8, 11, 3351.0), 17: (20, 14, 5459.0), 18: (17, 11, 8087.0), 6: (17, 15, 9883.0)})

if __name__ == '__main__':
    unittest.main()